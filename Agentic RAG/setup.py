from setuptools import setup, find_packages

setup(
    name="agentic-rag",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "langgraph",
        "langchain",
        "langchain-openai",
        "langchain-community",
        "langchain-anthropic",
        "faiss-cpu",
        "graphrag",
        "tavily-python",
        "exa_py",
        "linkup-sdk",
        "beautifulsoup4",
        "markdownify",
        "azure-search-documents",
        "duckduckgo-search",
    ],
    python_requires=">=3.8",
)