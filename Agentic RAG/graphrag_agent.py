from __future__ import annotations

import os
import asyncio
from pathlib import Path
from typing import Literal, Dict, Any

import pandas as pd
from langchain.chat_models import init_chat_model
from langchain.schema import BaseMessage
from langchain.tools import BaseTool
from langchain.tools import tool
from langgraph.graph import MessagesState, StateGraph, START, END
from langgraph.prebuilt import ToolNode, tools_condition
from pydantic import BaseModel, Field

# ---------------------------------------------------------------------------
# GraphRAG data & config -----------------------------------------------------
# ---------------------------------------------------------------------------
PROJECT_DIRECTORY = Path("./graphrag_mcp")

from graphrag.config.load_config import load_config
import graphrag.api as api

cfg = load_config(PROJECT_DIRECTORY)
entities = pd.read_parquet(PROJECT_DIRECTORY / "output/entities.parquet")
communities = pd.read_parquet(PROJECT_DIRECTORY / "output/communities.parquet")
community_reports = pd.read_parquet(PROJECT_DIRECTORY / "output/community_reports.parquet")
text_units = pd.read_parquet(PROJECT_DIRECTORY / "output/text_units.parquet")
relationships = pd.read_parquet(PROJECT_DIRECTORY / "output/relationships.parquet")

# ---------------------------------------------------------------------------
# LLM models -----------------------------------------------------------------
# ---------------------------------------------------------------------------
MODEL_NAME = "gpt-4o"
model = init_chat_model(model=MODEL_NAME, model_provider="openai")
grader_model = init_chat_model(model=MODEL_NAME, model_provider="openai")

# ---------------------------------------------------------------------------
# GraphRAG Retriever Tool ----------------------------------------------------
# ---------------------------------------------------------------------------
@tool
async def graphrag_search(query: str) -> str:
    """
    调用GraphRAG进行知识库检索，根据query检索相关有用内容。
    """
    response, _ = await api.global_search(
        config=cfg,
        entities=entities,
        communities=communities,
        community_reports=community_reports,
        community_level=2,
        dynamic_community_selection=False,
        response_type="Multiple Paragraphs",
        query=query,
    )
    return response

# ---------------------------------------------------------------------------
# Prompts --------------------------------------------------------------------
# ---------------------------------------------------------------------------
SYSTEM_INSTRUCTION = (
    "You are an assistant for the MCP technical practical course. "
    "Note: In this context, MCP stands for **Model Context Protocol**, an open framework for enabling LLMs to call external tools and interact with structured APIs. "
    "Do NOT interpret MCP as Microsoft Certified Professional.\n\n"
    "You should answer ONLY questions related to the content of the MCP technical course, including tool invocation, LangGraph workflows, streaming agents, tool registration, and best practices. "
    "If the user question is NOT related to the course, reply exactly: '我不能回答与 MCP 技术实战公开课无关的问题。' "
    "You may call the provided tool `graphrag_search` when additional context from the course materials is required. "
    "Please respond in detailed, structured Markdown format, using examples, diagrams (if referenced), and code snippets when appropriate."
)

GRADE_PROMPT = (
    "You are a grader assessing the relevance of a retrieved document to a user question within the MCP (Model Context Protocol) practical course.\n"
    "Retrieved document:\n{context}\n\nUser question: {question}\n"
    "Return 'yes' if relevant, otherwise 'no'."
)


REWRITE_PROMPT = (
    "You are rewriting user questions to make them more relevant to the MCP technical practical course.\n"
    "Note: In this context, MCP means **Model Context Protocol**, not Microsoft Certified Professional.\n"
    "Your goal is to refine the question so it aligns better with the course topics such as streaming HTTP servers, LangGraph workflows, tool invocation, and multi-agent coordination.\n\n"
    "Original question:\n{question}\nImproved question:"
)

ANSWER_PROMPT = (
    "You are an assistant for answering questions related to the MCP (Model Context Protocol) technical practical course. "
    "Use the provided context to give a detailed, accurate, and helpful answer.\n\n"
    "Whenever relevant, include:\n"
    "- Examples\n"
    "- Code blocks (use triple backticks)\n"
    "- Image references from the source context (e.g. `![Alt Text](image_url)`)\n"
    "- Structured Markdown (headings, lists, etc)\n\n"
    "If the answer is not available or uncertain, reply: '我不知道。'\n\n"
    "Question: {question}\nContext: {context}"
)


# ---------------------------------------------------------------------------
# LangGraph Nodes ------------------------------------------------------------
# ---------------------------------------------------------------------------
async def generate_query_or_respond(state: MessagesState):
    """LLM decides to answer directly or call GraphRAG tool."""
    response = await model.bind_tools([graphrag_search]).ainvoke(
        [{"role": "system", "content": SYSTEM_INSTRUCTION}, *state["messages"]]
    )
    return {"messages": [response]}


class GradeDoc(BaseModel):
    binary_score: str = Field(description="Relevance score 'yes' or 'no'.")


async def grade_documents(state: MessagesState) -> Literal["generate_answer", "rewrite_question"]:
    question = state["messages"][0].content
    ctx = state["messages"][-1].content
    prompt = GRADE_PROMPT.format(question=question, context=ctx)
    res = await grader_model.with_structured_output(GradeDoc).ainvoke([
        {"role": "user", "content": prompt}
    ])
    return "generate_answer" if res.binary_score.lower().startswith("y") else "rewrite_question"


async def rewrite_question(state: MessagesState):
    question = state["messages"][0].content
    resp = await model.ainvoke([
        {"role": "user", "content": REWRITE_PROMPT.format(question=question)}
    ])
    return {"messages": [{"role": "user", "content": resp.content}]}


async def generate_answer(state: MessagesState):
    question = state["messages"][0].content
    ctx = state["messages"][-1].content
    resp = await model.ainvoke([
        {"role": "user", "content": ANSWER_PROMPT.format(question=question, context=ctx)}
    ])
    return {"messages": [resp]}

# ---------------------------------------------------------------------------
# Build graph ----------------------------------------------------------------
# ---------------------------------------------------------------------------
workflow = StateGraph(MessagesState)
workflow.add_node("generate_query_or_respond", generate_query_or_respond)
workflow.add_node("retrieve", ToolNode([graphrag_search]))
workflow.add_node("rewrite_question", rewrite_question)
workflow.add_node("generate_answer", generate_answer)

workflow.add_edge(START, "generate_query_or_respond")
workflow.add_conditional_edges("generate_query_or_respond", tools_condition, {"tools": "retrieve", END: END})
workflow.add_conditional_edges("retrieve", grade_documents)
workflow.add_edge("generate_answer", END)
workflow.add_edge("rewrite_question", "generate_query_or_respond")

graphrag_agent = workflow.compile(name="graphrag_agent")