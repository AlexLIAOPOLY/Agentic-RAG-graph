clarify_with_user_instructions = """
以下是用户为请求报告而进行的对话内容：
<Messages>
{messages}
</Messages>

请返回“一个”有针对性的问题，以澄清报告的范围。
重点关注以下方面：技术深度、目标受众、需要强调的具体方面。
例如：“我应该侧重于技术实现细节，还是侧重于高层次的商业价值？” 
"""

report_planner_query_writer_instructions = """
你正在为一篇报告进行资料研究。

以下是用户为请求报告而进行的对话内容：
<Messages>
{messages}
</Messages>

报告应遵循以下结构组织：
<Report organization>
{report_organization}
</Report organization>

<Task>
你的目标是生成 {number_of_queries} 条网页搜索查询，用于收集规划报告章节所需的信息。

这些搜索查询应当：

1. 与报告主题相关；
2. 有助于满足报告结构中指定的需求。

搜索查询应具体、明确，以便获取高质量的、相关性强的资料，同时涵盖报告结构所需的广度。
</Task>

<Format>
调用 Queries 工具
</Format>

今天是 {today}
"""

report_planner_instructions = """
我需要一份简洁且重点突出的报告结构规划。

以下是用户为请求报告而进行的对话内容：
<Messages>
{messages}
</Messages>

报告应遵循以下结构组织：
<Report organization>
{report_organization}
</Report organization>

以下是可用于规划报告章节的上下文资料：
<Context>
{context}
</Context>

<Task>
请为该报告生成一个章节列表。你的结构规划应紧凑且重点突出，避免章节重叠或无意义的填充内容。

例如，一个优秀的报告结构可能如下：
1/ 引言  
2/ 主题 A 的概述  
3/ 主题 B 的概述  
4/ A 与 B 的对比  
5/ 结论

每个章节应包含以下字段：

- Name（名称）：该章节的名称；
- Description（描述）：该章节所涵盖主要主题的简要概述；
- Research（是否研究）：是否需要为该章节进行网页研究。⚠️ 注意：主体章节（非引言/结论）必须设置为 Research=True。一个实用的报告至少应包含 2-3 个需要研究的章节；
- Content（内容）：该章节的内容，目前请留空。

集成指导原则：
- 在主体章节中包含示例与实现细节，而不是分成独立章节；
- 确保每个章节都有明确的目的，且无内容重叠；
- 合并相关概念，而非将其分开；
- 关键：每个章节必须与主报告主题直接相关；
- 避免出现与主题关系不大的边缘性章节。

在提交前，请检查你的结构安排，确保没有冗余章节，并且结构逻辑清晰合理。
</Task>

<Feedback>
以下是审阅者对报告结构的反馈（如有）：
{feedback}
</Feedback>

<Format>
调用 Sections 工具
</Format>
"""

query_writer_instructions = """
你是一位专业的技术写作者，正在为撰写技术报告的某一章节构建有针对性的网页搜索查询，以收集全面信息。

以下是用户为请求报告而进行的对话内容：
<Messages>
{messages}
</Messages>

<Section topic>
{section_topic}
</Section topic>

<Task>
你的目标是生成 {number_of_queries} 条搜索查询，用于围绕上述章节主题收集全面的信息。

这些搜索查询应：

1. 与主题相关；
2. 涉及该主题的不同方面。

请确保查询足够具体，以便找到高质量、相关性强的资料。
</Task>

<Format>
调用 Queries 工具
</Format>

今天是 {today}
"""

section_writer_instructions = """
撰写一份研究报告的某个章节。

<Task>
1. 仔细阅读关于报告请求、章节名称和章节主题的消息；
2. 如果已有章节内容，请一并阅读；
3. 阅读提供的参考资料（Source material）；
4. 决定要使用哪些参考资料来撰写报告章节；
5. 撰写该章节内容，并在末尾列出参考来源。
</Task>

<Writing Guidelines>
- 如果现有章节内容为空，则从头开始撰写；
- 如果已有内容存在，请将其与参考资料融合撰写；
- 严格控制在 150-200 字之间；
- 使用简洁、清晰的语言；
- 每段不超过 2-3 句话，保持短小精炼；
- 使用 Markdown 格式中的 `##` 标记章节标题；
- 切勿在文中以第一人称提及自己。该报告应保持专业性，不应出现“我”或任何自我描述语言；
- 不要描述你正在做什么，只需直接写报告正文，避免写出类似“我正在写这一部分”之类的话。
</Writing Guidelines>

<Citation Rules>
- 每个唯一的 URL 在正文中只能分配一个引用编号；
- 报告结尾处以 `### Sources` 开头列出每个引用；
- 重要：引用编号必须连续（1,2,3,4...），中间不得跳号，无论是否使用了所有参考资料；
- 强制换行：每一条引用请使用换行（`\\n`）显示；
- 示例格式：
  [1] 资源标题：URL  
  [2] 资源标题：URL
</Citation Rules>

<Final Check>
1. 核实报告中“所有”论点都有提供的参考资料支撑；
2. 每个 URL 在参考列表中只能出现一次；
3. 确认引用编号为连续数字（1,2,3...）且无遗漏；
4. 切勿在章节中加入任何作者评论。只需提供该章节内容，不要说“我正在撰写本章节”或“我会修改这一部分”等等。
</Final Check>
"""

section_writer_inputs = """ 
以下是用户为请求报告而进行的对话内容：
<Messages>
{messages}
</Messages>

<Section name>
{section_name}
</Section name>

<Section topic>
{section_topic}
</Section topic>

<Existing section content (if populated)>
{section_content}
</Existing section content>

<Source material>
{context}
</Source material>
"""

section_grader_instructions = """
根据指定主题评审某章节的报告内容：

以下是用户为请求报告而进行的对话内容：
<Messages>
{messages}
</Messages>

<Section topic>
{section_topic}
</Section topic>

<Section content>
{section}
</Section content>

<Task>
评估该章节内容是否充分覆盖了其主题。

如果内容未能充分覆盖，请生成 {number_of_follow_up_queries} 条补充搜索查询，以收集缺失的信息。
</Task>

<Format>
调用 Feedback 工具，输出以下结构：

grade: Literal["pass","fail"] = Field(
    description="评估结果，表示本章节内容是否符合要求：'pass' 表示通过，'fail' 表示需要修订。"
)
follow_up_queries: List[SearchQuery] = Field(
    description="补充搜索查询的列表。",
)
</Format>
"""

final_section_writer_instructions = """
你是一位专业的技术写作者，正在撰写一个章节，用以综合整个报告中的信息。

以下是用户为请求报告而进行的对话内容：
<Messages>
{messages}
</Messages>

<Section name>
{section_name}
</Section name>

<Section topic> 
{section_topic}
</Section topic>

<Available report content>
{context}
</Available report content>

<Task>
1. 针对不同章节类型的写作策略：

【引言部分】：
- 使用 `#` 表示报告标题（Markdown 格式）；
- 控制在 50-100 字之间；
- 使用简洁清晰的语言；
- 用 1-2 段阐述报告的核心动机；
- 简要预览正文部分将涉及的具体内容（可提及关键示例、案例研究或发现）；
- 采用清晰的叙述逻辑引入整份报告；
- 不要包含结构性元素（如列表或表格）；
- 不需要参考文献部分。

【结论 / 总结部分】：
- 使用 `##` 表示章节标题（Markdown 格式）；
- 控制在 100-150 字之间；
- 综合并串联正文部分的核心主题、发现与洞察；
- 引用正文中提到的具体示例、案例研究或数据要点；
- 若为对比类报告：
  * 必须包含一个聚焦型对比表格，采用 Markdown 表格语法；
  * 表格应提炼报告中的洞察；
  * 表格条目应清晰简洁；
- 若为非对比类报告：
  * 最多使用一个结构性元素，仅当能有效提炼要点时：
    * 可以是报告中项目的简明对比表（使用 Markdown 表格语法）；
    * 或一个简短列表（使用 Markdown 列表语法）：
      - 无序列表使用 `*` 或 `-`；
      - 有序列表使用 `1.`；
      - 注意缩进和格式整洁；
- 结尾应指出具体的后续行动建议或报告带来的启示；
- 不需要参考文献部分。

3. 写作方法：
- 优先使用具体细节而非笼统陈述；
- 每个字都要有价值；
- 聚焦你最核心的观点。
</Task>

<Quality Checks>
- 引言部分：50-100 字、使用 `#` 标题、不含结构元素、不包含引用；
- 结论部分：100-150 字、使用 `##` 标题、最多一个结构元素、不包含引用；
- 必须使用 Markdown 格式；
- 不要在输出中包含字数统计或引言说明；
- 严禁以第一人称提及自己身份。报告必须专业，不能出现任何“我”或“作为作者”的措辞。
</QualityChecks>
"""


SUMMARIZATION_PROMPT = """你的任务是总结一篇通过网页搜索获得的原始网页内容。目标是创建一个简洁的摘要，保留网页中最重要的信息。这个摘要将由后续的研究智能体使用，因此你必须确保核心信息不被遗漏。

以下是网页的原始内容：

<webpage_content>
{webpage_content}
</webpage_content>

请遵循以下指南完成摘要撰写：

1. 明确网页的主要话题或目的，并保留；
2. 保留关键信息、统计数据和核心数据点；
3. 如有权威人士或专家的引用，请保留关键语句；
4. 若内容具有时间敏感性或是历史事件，保持时间顺序；
5. 若网页中包含列表或步骤指引，请保留这些结构；
6. 包含任何有助于理解内容的时间、地点、人物等关键信息；
7. 精简冗长说明，保留核心要义。

根据不同类型的网页，摘要应关注以下重点：

- 对于新闻文章：聚焦“五个W一个H”（谁、什么、何时、哪里、为什么、如何）；
- 对于科研文章：保留研究方法、结果和结论；
- 对于评论类文章：提炼核心观点及其支撑要点；
- 对于产品页面：保留核心特性、规格、独特卖点。

摘要应显著短于原文，但需足够完整，能单独作为一条信息源使用。目标摘要长度为原始内容的 25%-30%，除非原文本身就非常简洁。

请使用以下格式输出摘要：

```
{{
   "summary": "请在此撰写精炼的摘要，如有必要，可使用段落或项目符号结构",
   "key_excerpts": [
   "第一条重要引用或摘要句子",
   "第二条重要引用或摘要句子",
   "第三条重要引用或摘要句子",
   ...根据需要添加，最多不超过 5 条
   ]
}}
```

以下是两个优秀摘要的示例：

示例 1（新闻文章）：
```json
{{
   "summary": "2023 年 7 月 15 日，美国国家航空航天局（NASA）成功从肯尼迪航天中心发射了 Artemis II 任务。这是自 1972 年阿波罗 17 号以来首个载人登月任务。四人乘组由指令官简·史密斯领导，将绕月飞行 10 天后返回地球。此任务是 NASA 建立月球人类驻点计划的重要步骤。",
   "key_excerpts": [
     "“Artemis II 代表了太空探索新时代的开启。”——NASA 局长 John Doe",
     "“该任务将测试未来月球长期驻留所需的关键系统。”——首席工程师 Sarah Johnson",
     "“我们不仅要重返月球，更是在迈向月球的未来。”——指令官 Jane Smith"
   ]
}}
```

示例 2（科研文章）：
```json
{{
   "summary": "《自然·气候变化》最新研究显示，全球海平面上升速度快于先前预测。研究分析了 1993 至 2022 年间的卫星数据，发现海平面上升的加速度达到了 0.08 mm/年²，主要归因于格陵兰和南极洲冰盖融化。若现有趋势持续，到 2100 年全球海平面可能上升 2 米，严重威胁沿海社区。",
   "key_excerpts": [
      "“我们的研究明确表明海平面上升正在加速，这对沿海规划与适应策略影响深远。”——首席作者 Dr. Emily Brown",
      "“格陵兰和南极的冰盖融化速度自 1990 年代以来已增长三倍。”——研究报告指出",
      "“若不立即大幅减少温室气体排放，本世纪末可能面临灾难性的海平面上升。”——合著者 Professor Michael Green"
   ]
}}
```

请记住，你的目标是为后续研究智能体生成一个易于理解且信息完整的摘要，务必保留最关键内容。"""