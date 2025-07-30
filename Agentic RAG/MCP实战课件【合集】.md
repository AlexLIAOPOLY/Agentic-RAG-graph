# 从零到一MCP快速入门实战

- Anthropic MCP发布通告：https://www.anthropic.com/news/model-context-protocol
- MCP GitHub主页：https://github.com/modelcontextprotocol

## 一、MCP技术体系介绍

### 1. MCP入门介绍

MCP，全称是Model Context Protocol，模型上下文协议，由Claude母公司Anthropic于去年11月正式提出。

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250318201338022.png" alt="image-20250318201338022" style="zoom:50%;" />

MCP刚发布的时候不温不火，直到今年Agent大爆发才被广泛关注。而在今年2月，Cursor正式宣布加入MCP功能支持，一举将MCP推到了全体开发人员面前。从本质上来说，MCP是一种技术协议，一种智能体Agent开发过程中共同约定的一种规范。这就好比秦始皇的“**书同文、车同轨**”，在统一的规范下，大家的**协作效率就能大幅提高**，最终**提升智能体Agent的开发效率**。截止目前，已上千种MCP工具诞生，在强悍的MCP生态加持下， 人人手搓Manus的时代即将到来。

> 7分钟讲清楚MCP是什么？https://www.bilibili.com/video/BV1uXQzYaEpJ/
>
> <img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250318201253260.png" alt="image-20250318201253260" style="zoom:50%;" />

总的来说**，**MCP**解决的最大痛点，就是Agent开发中调用外部工具的技术门槛过高的问题。**

我们都知道，能调用外部工具，是大模型进化为智能体Agent的关键，如果不能使用外部工具，大模型就只能是个简单的聊天机器人，甚至连查询天气都做不到。由于底层技术限制啊，大模型本身是无法和外部工具直接通信的，因此Function calling的思路，就是创建一个外部函数（function）作为中介，一边传递大模型的请求，另一边调用外部工具，最终让大模型能够间接的调用外部工具。

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250318202017508.png" alt="image-20250318202017508" style="zoom:50%;" />

例如，当我们要查询当前天气时，让大模型调用外部工具的function calling的过程就如图所示：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250318202029130.png" alt="image-20250318202029130" style="zoom:50%;" />

Function calling是个非常不错的技术设计，自诞生以来，一直被业内奉为圭臬。但唯一的问题就是，编写这个外部函数的工作量太大了，一个简单的外部函数往往就得上百行代码，而且，为了让大模型“认识”这些外部函数，我们还要额外为每个外部函数编写一个JSON Schema格式的功能说明，此外，我们还需要精心设计一个提示词模版，才能提高Function calling响应的准确率。

而MCP的目标，就是能在Agent开发过程中，让大模型更加便捷的调用外部工具。为此，MCP提出了两个方案，其一，“**车同轨、书同文**”，统一Function calling的运行规范。

首先是先统一名称，MCP把大模型运行环境称作 MCP Client，也就是MCP客户端，同时，把外部函数运行环境称作MCP Server，也就是MCP服务器，

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250318202116026.png" alt="image-20250318202116026" style="zoom:50%;" />

然后，统一MCP客户端和服务器的运行规范，并且要求MCP客户端和服务器之间，也统一按照某个既定的提示词模板进行通信。

“车同轨、书同文”最大的好处就在于，可以避免MCP服务器的重复开发，也就是避免外部函数重复编写。例如，像查询天气、网页爬取、查询本地MySQL数据库这种通用的需求，大家有一个人开发了一个服务器就好，开发完大家都能复制到自己的项目里来使用，不用每个人每次都单独写一套。

这可是促进全球AI开发者共同协作的好事儿，很快，GitHub上就出现了海量的已经开发好的MCP 服务器，从SQL数据库检索、到网页浏览信息爬取，从命令行操作电脑、到数据分析机器学习建模，等等等等，不一而足。

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/888b152a-b366-481e-9de3-244cf5119028.png" alt="888b152a-b366-481e-9de3-244cf5119028" style="zoom:33%;" />

现在，只要你本地运行的大模型支持MCP协议，也就是只要安装了相关的库，仅需几行代码即可接入这些海量的外部工具，是不是感觉Agent开发门槛瞬间降低了呢。

这种“车同轨、书同文”的规范，在技术领域就被称作协议，例如http就是网络信息交换的技术协议。各类技术协议的目标，都是希望**通过提高协作效率来提升开发效率**，而MCP，Model Context Protocol，就是一种旨在提高大模型Agent开发效率的技术协议。

那既然是协议，必然是使用的人越多才越有用。因此，为了进一普及MCP协议，Anthropic还提供了一整套MCP客户端、服务器开发的SDK，也就是开发工具，并且支持Python、TS和Java等多种语言，借助SDK，仅需几行代码，就可以快速开发一个MCP服务器。

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250318202304248.png" alt="image-20250318202304248" style="zoom:50%;" />

然后，你就可以把它接入任意一个MCP客户端来构建智能体，如果愿意，还可以把MCP服务器分享到社区，给有需求的开发者使用，甚至你还可以把你的MCP服务器放到线上运行，让用户付费使用。

而MCP的客户端，不仅支持Claude模型，也支持任意本地模型或者在线大模型，或者是一些IDE。例如，现在Cursor正式接入MCP，代表着Cursor正式成为MCP客户端，在Cursor中，我们不仅能快速编写MCP服务器（外部函数），更能借助Cursor一键连接上成百上千的开源MCP服务器，让大模型快速接入海量工具，从而大幅加快Agent开发进度。

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250318153131024.png" alt="image-20250318153131024" style="zoom:50%;" />

### 2. Function calling技术回顾

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/202412191720637.png" alt="202412191720637" style="zoom:50%;" />

### 3. 大模型Agent开发技术体系回顾

- 参考公开课《零基础Agent智能体开发基础理论详解！》：https://www.bilibili.com/video/BV1CcBJYtEne/

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250318201810976.png" alt="image-20250318201810976" style="zoom:50%;" />

- 更多MCP示意图

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250318185821214.png" alt="image-20250318185821214" style="zoom:50%;" />

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250318185810201.png" alt="image-20250318185810201" style="zoom: 50%;" />

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/115746_nnq5_2720166.webp" alt="115746_nnq5_2720166" style="zoom:50%;" />

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/78513c082775c213a0134cb187b2b069_.png" alt="78513c082775c213a0134cb187b2b069_" style="zoom:50%;" />

## 二、MCP客户端Client开发流程

### 1. uv工具入门使用指南

#### 1.1 uv入门介绍

​	MCP开发要求借助uv进行虚拟环境创建和依赖管理。`uv` 是一个**Python 依赖管理工具**，类似于 `pip` 和 `conda`，但它更快、更高效，并且可以更好地管理 Python 虚拟环境和依赖项。它的核心目标是**替代 `pip`、`venv` 和 `pip-tools`**，提供更好的性能和更低的管理开销。

**`uv` 的特点**：

1. **速度更快**：相比 `pip`，`uv` 采用 Rust 编写，性能更优。
2. **支持 PEP 582**：无需 `virtualenv`，可以直接使用 `__pypackages__` 进行管理。
3. **兼容 `pip`**：支持 `requirements.txt` 和 `pyproject.toml` 依赖管理。
4. **替代 `venv`**：提供 `uv venv` 进行虚拟环境管理，比 `venv` 更轻量。
5. **跨平台**：支持 Windows、macOS 和 Linux。

#### 1.2 uv安装流程

**方法 1：使用 `pip` 安装（适用于已安装 `pip` 的系统）**

```bash
pip install uv
```

**方法 2：使用 `curl` 直接安装**

如果你的系统没有 `pip`，可以直接运行：

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

这会自动下载 `uv` 并安装到 `/usr/local/bin`。

#### 1.3 uv的基本用法介绍

​	安装 `uv` 后，你可以像 `pip` 一样使用它，但它的语法更简洁，速度也更快。注意，以下为使用语法示例，不用实际运行。

- **安装 Python 依赖**

```bash
uv pip install requests
```

与 `pip install requests` 类似，但更快。

- **创建虚拟环境**

```bash
uv venv myenv
```

等效于 `python -m venv myenv`，但更高效。

- **激活虚拟环境**

```bash
source myenv/bin/activate  # Linux/macOS
myenv\Scripts\activate     # Windows
```

- **安装 `requirements.txt`**

```bash
uv pip install -r requirements.txt
```

- **直接运行 Python 项目**

如果项目中包含 `pyproject.toml`，你可以直接运行：

```bash
uv run python script.py
```

这等效于：

```bash
pip install -r requirements.txt
python script.py
```

但 `uv` 速度更快，管理更高效。

> 为什么MCP更推荐使用uv进行环境管理？
>
> MCP 依赖的 Python 环境可能包含多个模块，`uv` 通过 `pyproject.toml` 提供更高效的管理方式，并且可以避免 `pip` 的一些依赖冲突问题。此外，`uv` 的包管理速度远超 `pip`，这对于 MCP 这样频繁管理依赖的项目来说是一个很大的优势。

接下来我们尝试先构建一个 MCP 客户端，确保基本逻辑可用，然后再逐步搭建 MCP 服务器进行联调，这样可以**分阶段排查问题**，避免一上来就涉及太多复杂性。

### 2.MCP极简客户端搭建流程

#### 2.1 创建 MCP 客户端项目

```bash
# 创建项目目录
uv init mcp-client
cd mcp-client
```

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/202503171503701.png" alt="image-20250317150300621" style="zoom:50%;" />

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/202503171503750.png" alt="image-20250317150324701" style="zoom:50%;" />

#### 2.2 创建MCP客户端虚拟环境

```bash
# 创建虚拟环境
uv venv

# 激活虚拟环境
source .venv/bin/activate
```

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/202503171509604.png" alt="image-20250317150947534" style="zoom:50%;" />

这里需要注意的是，相比pip，uv会自动识别当前项目主目录并创建虚拟环境。

然后即可通过add方法在虚拟环境中安装相关的库。

```bash
# 安装 MCP SDK
uv add mcp
```

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/202503171510547.png" alt="image-20250317151039345" style="zoom:50%;" />

#### 2.3 编写基础 MCP 客户端

然后在当前项目主目录中**创建 `client.py` **

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/202503171527863.png" alt="image-20250317152749801" style="zoom:50%;" />

并写入以下代码

```python
import asyncio
from mcp import ClientSession
from contextlib import AsyncExitStack

class MCPClient:
    def __init__(self):
        """初始化 MCP 客户端"""
        self.session = None
        self.exit_stack = AsyncExitStack()

    async def connect_to_mock_server(self):
        """模拟 MCP 服务器的连接（暂不连接真实服务器）"""
        print("✅ MCP 客户端已初始化，但未连接到服务器")

    async def chat_loop(self):
        """运行交互式聊天循环"""
        print("\nMCP 客户端已启动！输入 'quit' 退出")

        while True:
            try:
                query = input("\nQuery: ").strip()
                if query.lower() == 'quit':
                    break
                print(f"\n🤖 [Mock Response] 你说的是：{query}")
            except Exception as e:
                print(f"\n⚠️ 发生错误: {str(e)}")

    async def cleanup(self):
        """清理资源"""
        await self.exit_stack.aclose()

async def main():
    client = MCPClient()
    try:
        await client.connect_to_mock_server()
        await client.chat_loop()
    finally:
        await client.cleanup()

if __name__ == "__main__":
    asyncio.run(main())
```

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/202503171528870.png" alt="image-20250317152812788" style="zoom:50%;" />

这段代码能够初始化 MCP 客户端（但不连接服务器），并提供一个 **交互式 CLI**，可以输入查询（但只返回模拟回复），通过**输入 `quit` 退出程序**。需要注意的是，此时客户端没有关联任何大模型，因此只会重复用户的输入。

#### 2.4 MCP客户端基本代码结构

以下是`client.py` 代码详解，**代码核心功能**：

- **初始化 MCP 客户端**
- *提供一个命令行交互界面
- 模拟 MCP 服务器连接
- 支持用户输入查询并返回「模拟回复」
- **支持安全退出**

代码具体解释如下：首先是**导入必要的库**

```python
import asyncio  # 让代码支持异步操作
from mcp import ClientSession  # MCP 客户端会话管理
from contextlib import AsyncExitStack  # 资源管理（确保客户端关闭时释放资源）
```

📌 **解释**：

- `asyncio`：Python 内置的**异步编程库**，让 MCP 可以**非阻塞地**执行任务（比如聊天、查询）。
- `mcp.ClientSession`：用于**管理 MCP 客户端会话**（但目前我们先不连接 MCP 服务器）。
- `AsyncExitStack`：**自动管理资源**，确保程序退出时正确关闭 MCP 连接。

然后**创建 `MCPClient` 类**

```python
class MCPClient:
    def __init__(self):
        """初始化 MCP 客户端"""
        self.session = None  # 先不连接 MCP 服务器
        self.exit_stack = AsyncExitStack()  # 创建资源管理器
```

📌 **解释**：

- `self.session = None`：**暂时不连接 MCP 服务器**，后续可以修改来真正连接。
- `self.exit_stack = AsyncExitStack()`：**管理 MCP 客户端的资源**，确保程序退出时可以正确释放资源。

紧接着**模拟 MCP 服务器连接**

```python
async def connect_to_mock_server(self):
    """模拟 MCP 服务器的连接（暂不连接真实服务器）"""
    print("✅ MCP 客户端已初始化，但未连接到服务器")
```

📌 **解释**：

- 这个函数**不会真的连接 MCP 服务器**，只是打印一条信息，表示客户端已经初始化。
- `async def`：因为我们用的是 **异步编程**，所以需要用 `async` 关键字。

然后创建**交互式聊天循环**

```python
async def chat_loop(self):
    """运行交互式聊天循环"""
    print("\nMCP 客户端已启动！输入 'quit' 退出")

    while True:  # 无限循环，直到用户输入 'quit'
        try:
            query = input("\nQuery: ").strip()  # 让用户输入问题
            if query.lower() == 'quit':  # 如果用户输入 quit，退出循环
                break
            print(f"\n🤖 [Mock Response] 你说的是：{query}")  # 返回模拟回复
        except Exception as e:  # 发生错误时捕获异常
            print(f"\n⚠️ 发生错误: {str(e)}")
```

📌 **解释**：

1. `while True`：**无限循环**，让用户可以不断输入查询。
2. `query = input("\nQuery: ").strip()`：**获取用户输入的查询**。
3. `if query.lower() == 'quit'`：**如果用户输入 `quit`，退出循环**。
4. `print(f"\n🤖 [Mock Response] 你说的是：{query}")`：**模拟 MCP 服务器的响应**，暂时只是回显用户输入的内容。

🔹 **示例运行**

```plaintext
MCP 客户端已启动！输入 'quit' 退出

Query: 你好
🤖 [Mock Response] 你说的是：你好

Query: 这是什么？
🤖 [Mock Response] 你说的是：这是什么？

Query: quit  # 退出程序
```

最后白那些**释放资源**代码

```python
async def cleanup(self):
    """清理资源"""
    await self.exit_stack.aclose()  # 关闭资源管理器
```

📌 **解释**：

- `aclose()` 确保程序退出时**正确关闭 MCP 连接**（尽管目前没有真正的连接）。

并定义**`main()` 主函数**

```python
async def main():
    client = MCPClient()  # 创建 MCP 客户端
    try:
        await client.connect_to_mock_server()  # 连接（模拟）服务器
        await client.chat_loop()  # 进入聊天循环
    finally:
        await client.cleanup()  # 确保退出时清理资源
```

📌 **解释**：

- `client = MCPClient()`：创建一个 MCP 客户端实例。
- `await client.connect_to_mock_server()`：初始化 MCP 客户端（暂不连接服务器）。
- `await client.chat_loop()`：启动交互式聊天。
- `finally:` 确保 **不管程序是否异常退出，都会正确释放资源**。

以及**运行代码**

```python
if __name__ == "__main__":
    asyncio.run(main())
```

📌 **解释**：

- `if __name__ == "__main__":`：确保代码**只能在 Python 直接运行时执行**（而不是作为库导入时）。
- `asyncio.run(main())`：**启动 `main()`，运行 MCP 客户端**。

MCP中一个基础的客户端代码结构**总结如下**：

| **代码部分**                   | **作用**            |
| ------------------------------ | ------------------- |
| **`MCPClient.__init__()`**     | 初始化 MCP 客户端   |
| **`connect_to_mock_server()`** | 模拟 MCP 服务器连接 |
| **`chat_loop()`**              | 提供交互式聊天界面  |
| **`cleanup()`**                | 释放资源            |
| **`main()`**                   | 启动客户端          |
| **`asyncio.run(main())`**      | 运行程序            |

#### 2.5 **运行 MCP 客户端**

然后尝试运行这个极简的MCP客户端：

```bash
uv run client.py
```

运行效果如下所示：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/202503171529968.png" alt="image-20250317152909867" style="zoom:50%;" />

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/78513c082775c213a0134cb187b2b069_.png" style="zoom:50%;" />

#### 2.6 Jupyter中代码运行效果

此外，MCP客户端也是可以在Jupyter中运行的，此时运行代码如下：

```python
!pip install mcp
```

```python
import asyncio
import nest_asyncio
from mcp import ClientSession
from contextlib import AsyncExitStack

# 解决 Jupyter Notebook 的 asyncio 事件循环冲突
nest_asyncio.apply()
```

```python
class MCPClient:
    def __init__(self):
        """初始化 MCP 客户端"""
        self.session = None
        self.exit_stack = AsyncExitStack()

    async def connect_to_mock_server(self):
        """模拟 MCP 服务器的连接（暂不连接真实服务器）"""
        print("✅ MCP 客户端已初始化，但未连接到服务器")

    async def chat_loop(self):
        """运行交互式聊天循环"""
        print("\n📢 MCP 客户端已启动！输入 'quit' 退出\n")

        while True:
            try:
                # 直接使用 input() 获取用户输入
                query = input("📝 请输入您的问题: ").strip()
                if query.lower() == 'quit':
                    print("\n👋 退出聊天...")
                    break

                # 模拟服务器返回响应
                response = f"🤖 [Mock Response] 你说的是：{query}"
                print(response)

            except Exception as e:
                print(f"\n⚠️ 发生错误: {str(e)}")

    async def cleanup(self):
        """清理资源"""
        await self.exit_stack.aclose()

async def main():
    client = MCPClient()
    try:
        await client.connect_to_mock_server()
        await client.chat_loop()
    finally:
        await client.cleanup()
```

然后即可输入如下代码开启对话：

```python
# 在 Jupyter Notebook 中运行
await main()
```

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250318161253163.png" alt="image-20250318161253163" style="zoom:50%;" />

### 3. MCP客户端接入OpenAI、DeepSeek在线模型流程

​	接下来尝试在客户端中接入OpenAI和DeepSeek等在线模型进行对话。需要注意的是，由于OpenAI和DeepSeek调用方法几乎完全一样，因此这套服务器client代码可以同时适用于GPT模型和DeepSeek哦行。

#### 3.1 新增依赖

​	为了支持调用OpenAI模型，以及在环境变量中读取API-KEY等信息，需要先安装如下依赖：

```bash
uv add mcp openai python-dotenv
```

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/202503171542716.png" alt="image-20250317154224561" style="zoom:50%;" />

#### 3.2 创建.env文件

​	接下来创建.env文件，并写入OpenAI的API-Key，以及反向代理地址。借助反向代理，国内可以无门槛直连OpenAI官方服务器，并调用官方API。

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/202503171539087.png" alt="image-20250317153902986" style="zoom:50%;" />

写入如下内容

```bash
BASE_URL="反向代理地址"
MODEL=gpt-4o
OPENAI_API_KEY="OpenAI-API-Key"
```

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/202503171549042.png" alt="image-20250317154928953" style="zoom:50%;" />

OpenAI注册指南与国内反向代理领取地址：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250318161738753.png" alt="image-20250318161738753" style="zoom:50%;" />

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/78513c082775c213a0134cb187b2b069_.png" style="zoom:25%;" />

而如果是使用DeepSeek模型，则需要在.env中写入如下内容：

```bash
BASE_URL=https://api.deepseek.com
MODEL=deepseek-chat      
OPENAI_API_KEY="DeepSeek API-Key"
```

> 如果要调用deepseek-chat为DeepSeek V3模型，若要调用DeepSeek R1，则需要将其修改为deepseek-reasoner；
>
> DeepSeek快速入门：https://www.bilibili.com/video/BV1JuwVewELc/

#### 3.3 修改client.py代码

接下来修改客户端代码：

```python
import asyncio
import os
from openai import OpenAI
from dotenv import load_dotenv
from contextlib import AsyncExitStack

# 加载 .env 文件，确保 API Key 受到保护
load_dotenv()

class MCPClient:
    def __init__(self):
        
        """初始化 MCP 客户端"""
        self.exit_stack = AsyncExitStack()
        self.openai_api_key = os.getenv("OPENAI_API_KEY")  # 读取 OpenAI API Key
        self.base_url = os.getenv("BASE_URL")  # 读取 BASE YRL
        self.model = os.getenv("MODEL")  # 读取 model
        
        if not self.openai_api_key:
            raise ValueError("❌ 未找到 OpenAI API Key，请在 .env 文件中设置 OPENAI_API_KEY")
            
        self.client = OpenAI(api_key=self.openai_api_key, base_url=self.base_url) 
        

    async def process_query(self, query: str) -> str:
        """调用 OpenAI API 处理用户查询"""
        messages = [{"role": "system", "content": "你是一个智能助手，帮助用户回答问题。"},
                    {"role": "user", "content": query}]
        
        try:
            # 调用 OpenAI API
            response = await asyncio.get_event_loop().run_in_executor(
                None,
                lambda: self.client.chat.completions.create(
                    model=self.model,
                    messages=messages
                )
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"⚠️ 调用 OpenAI API 时出错: {str(e)}"

    async def chat_loop(self):
        """运行交互式聊天循环"""
        print("\n🤖 MCP 客户端已启动！输入 'quit' 退出")

        while True:
            try:
                query = input("\n你: ").strip()
                if query.lower() == 'quit':
                    break
                
                response = await self.process_query(query)  # 发送用户输入到 OpenAI API
                print(f"\n🤖 OpenAI: {response}")

            except Exception as e:
                print(f"\n⚠️ 发生错误: {str(e)}")

    async def cleanup(self):
        """清理资源"""
        await self.exit_stack.aclose()

async def main():
    client = MCPClient()
    try:
        await client.chat_loop()
    finally:
        await client.cleanup()

if __name__ == "__main__":
    asyncio.run(main())
```

#### 3.4 运行client.py

然后即可输入如下命令开始运行对话客户端：

```bash
uv run client.py
```

运行效果如下所示：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250318163852424.png" alt="image-20250318163852424" style="zoom:50%;" />

#### 3.5 clint.py代码解释

**加载 OpenAI API Key**

```python
from dotenv import load_dotenv
import os

# 加载 .env 文件，确保 API Key 受到保护
load_dotenv()

self.openai_api_key = os.getenv("OPENAI_API_KEY")  # 读取 API Key
if not self.openai_api_key:
    raise ValueError("❌ 未找到 OpenAI API Key，请在 .env 文件中设置 OPENAI_API_KEY")
```

📌 **解释**

- **`load_dotenv()`**：自动加载 `.env` 文件，避免在代码中直接暴露 API Key。
- **`os.getenv("OPENAI_API_KEY")`**：从环境变量中读取 `OPENAI_API_KEY`。
- **`raise ValueError(...)`**：如果 API Key 为空，则抛出错误，提醒用户**必须配置 API Key**。

📌 **创建 `.env` 文件（如果还没有的话）**

```bash
touch .env
```

📌 **在 `.env` 文件中添加 API Key**

```plaintext
OPENAI_API_KEY=你的OpenAI API Key
```

**发送用户输入到 OpenAI API**

```python
async def process_query(self, query: str) -> str:
    """调用 OpenAI API 处理用户查询"""
    messages = [
        {"role": "system", "content": "你是一个智能助手，帮助用户回答问题。"},
        {"role": "user", "content": query}
    ]

    try:
        # 调用 OpenAI GPT-4 API
        response = await asyncio.get_event_loop().run_in_executor(
            None,
            lambda: openai.ChatCompletion.create(
                model="gpt-4",
                messages=messages,
                max_tokens=1000,
                temperature=0.7
            )
        )
        return response["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return f"⚠️ 调用 OpenAI API 时出错: {str(e)}"
```

📌 **解释**

- `messages`：创建对话上下文，让 OpenAI 知道如何回答问题：
  - **`system` 角色**：设定 AI 角色（如“你是一个智能助手”）。
  - **`user` 角色**：存储用户输入。

- `openai.ChatCompletion.create(...)`

  - `model="gpt-4"`：使用 OpenAI 的 GPT-4 进行对话。
  - `messages=messages`：提供聊天记录，让 AI 生成回答。
  - `max_tokens=1000`：限制 AI 生成的最大字数。
  - `temperature=0.7`：控制 AI 回答的随机性（越高越随机）。

- `run_in_executor(...)`：
  - **因为 OpenAI API 是同步的，但我们用的是异步代码**
  - 这里用 **`asyncio.get_event_loop().run_in_executor(...)`** **将 OpenAI API 变成异步任务**，防止程序卡顿。

**交互式聊天**

```python
async def chat_loop(self):
    """运行交互式聊天循环"""
    print("\n🤖 MCP 客户端已启动！输入 'quit' 退出")

    while True:
        try:
            query = input("\n你: ").strip()
            if query.lower() == 'quit':
                break

            response = await self.process_query(query)  # 发送用户输入到 OpenAI API
            print(f"\n🤖 OpenAI: {response}")

        except Exception as e:
            print(f"\n⚠️ 发生错误: {str(e)}")
```

📌 **解释**

- **输入查询** `query = input("\n你: ").strip()`，支持多轮对话。
- **调用 `process_query()`**，将用户输入**发送到 OpenAI API 并获取回复**。
- **显示 OpenAI 生成的回复**：`print(f"\n🤖 OpenAI: {response}")`
- **用户输入 `quit` 退出**。

> 需要注意的是，由于MCP的client SDK主要规定了client和server之间的通信方法，因此在没有创建server之前，一个单纯对话的client甚至不需要用到mcp功能。但本段代码的学习仍是有必要的，为了熟悉各类大模型本地调用对话流程。而后我们只需要围绕上述代码稍作修改，即可调用外部的server。

### 4. MCP客户端接入本地ollama、vLLM模型流程

​	接下来，我们继续尝试将ollama、vLLM等模型调度框架接入MCP的client。由于ollama和vLLM均支持OpenAI API风格调用方法，因此上述client.py并不需要进行任何修改，我们只需要启动响应的调度框架服务，然后修改.env文件即可。

> vLLM&ollama调用本地模型教程：https://www.bilibili.com/video/BV1hZRTYUEtR/
>
> <img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/78513c082775c213a0134cb187b2b069_.png" style="zoom:25%;" />

#### 4.1 MCP客户端接入本地ollama

这里以QwQ-32B为例，尝试借助ollama接入MCP客户端。

- 启动ollama

  首先需要启动ollama

  ```bash
  ollama start
  ```

  <img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250318165131319.png" alt="image-20250318165131319" style="zoom:33%;" />

- 测试模型能否调用

  ```bash
  ollama list
  ollama run qwq
  ```

  <img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250318165231968.png" alt="image-20250318165231968" style="zoom:50%;" />

- 修改配置文件

  然后修改`.env`配置文件

  ```bash
  BASE_URL=http://localhost:11434/v1/
  MODEL=qwq 
  OPENAI_API_KEY=ollama
  ```

  <img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250318165402267.png" alt="image-20250318165402267" style="zoom:50%;" />

- 运行client

  然后即可运行MCP client客户端了

  ```bash
  uv run client.py
  ```

  此时是推理模型，因此出现<think>标志：

  <img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250318165551372.png" alt="image-20250318165551372" style="zoom:50%;" />

#### 4.2 MCP客户端接入vLLM

类似的，我们也可以把vLLM接入MCP客户端中。

- 启动vLLM服务

  ```bash
  cd /root/autodl-tmp
  CUDA_VISIBLE_DEVICES=0,1 vllm serve ./QwQ-32B --tensor-parallel-size 2
  ```

  

- 修改配置文件

  ```bash
  BASE_URL=http://localhost:8000/v1
  MODEL=./QwQ-32B
  OPENAI_API_KEY=EMPTY
  ```

  <img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250318165852958.png" alt="image-20250318165852958" style="zoom:50%;" />

- 运行client

  然后即可运行MCP client客户端了

  ```bash
  uv run client.py
  ```

  此时是推理模型，因此出现<think>标志：

  <img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250318170257681.png" alt="image-20250318170257681" style="zoom:50%;" />

此时vLLM后端响应如下：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250318170453956.png" alt="image-20250318170453956" style="zoom: 50%;" />

## 三、MCP天气查询服务器server与使用

### 1. MCP服务器概念介绍

​	根据MCP协议定义，Server可以提供三种类型的标准能力，**Resources、Tools、Prompts**，每个Server可同时提供者三种类型能力或其中一种。

- **Resources：**资源，类似于文件数据读取，可以是文件资源或是API响应返回的内容。
- **Tools：**工具，第三方服务、功能函数，通过此可控制LLM可调用哪些函数。
- **Prompts：**提示词，为用户预先定义好的完成特定任务的模板。

### 2. MCP服务器通讯机制

​	Model Context Protocol（MCP）是一种由 Anthropic 开源的协议，旨在将大型语言模型直接连接至数据源，实现无缝集成。根据 MCP 的规范，当前支持两种传输方式：标准输入输出（stdio）和基于 HTTP 的服务器推送事件（SSE）。而近期，开发者在 MCP 的 GitHub 仓库中提交了一项提案，建议采用“可流式传输的 HTTP”来替代现有的 HTTP+SSE 方案。此举旨在解决当前远程 MCP 传输方式的关键限制，同时保留其优势。 HTTP 和 SSE（服务器推送事件）在数据传输方式上存在明显区别：

- **通信方式**：
  - **HTTP**：采用请求-响应模式，客户端发送请求，服务器返回响应，每次请求都是独立的。
  - **SSE**：允许服务器通过单个持久的 HTTP 连接，持续向客户端推送数据，实现实时更新。
- **连接特性**：
  - **HTTP**：每次请求通常建立新的连接，虽然在 HTTP/1.1 中引入了持久连接，但默认情况下仍是短连接。
  - **SSE**：基于长连接，客户端与服务器之间保持持续的连接，服务器可以在任意时间推送数据。
- **适用场景**：
  - **HTTP**：适用于传统的请求-响应场景，如网页加载、表单提交等。
  - **SSE**：适用于需要服务器主动向客户端推送数据的场景，如实时通知、股票行情更新等。

需要注意的是，SSE 仅支持服务器向客户端的单向通信，而 WebSocket 则支持双向通信。

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250318181056195.png" alt="image-20250318181056195" style="zoom:50%;" />

> 在 Model Context Protocol（MCP）中，**标准输入输出（stdio）模式**是一种用于本地通信的传输方式。在这种模式下，MCP 客户端会将服务器程序作为子进程启动，双方通过标准输入（stdin）和标准输出（stdout）进行数据交换。这种方式适用于客户端和服务器在同一台机器上运行的场景，确保了高效、低延迟的通信。 
>
> 具体而言，客户端通过标准输入发送请求，服务器通过标准输出返回响应。这种直接的数据传输方式减少了网络延迟和传输开销，适合需要快速响应的本地应用。
>
> 相比之下，MCP 还支持基于 HTTP 和服务器推送事件（SSE）的传输方式，适用于客户端和服务器位于不同物理位置的场景。在这种模式下，客户端和服务器通过 HTTP 协议进行通信，利用 SSE 实现服务器向客户端的实时数据推送。 
>
> 总的来说，stdio 模式提供了一种简单、高效的本地通信方式，适用于客户端和服务器在同一环境下运行的情况。而对于分布式或远程部署的场景，基于 HTTP 和 SSE 的传输方式则更为合适。

> 可流式传输的 HTTP PR：https://github.com/modelcontextprotocol/specification/pull/206
>
> <img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250318154457630.png" alt="image-20250318154457630" style="zoom:50%;" />

具体来说，MCP定义了Client与Server进行通讯的协议与消息格式，其支持两种类型通讯机制：标准输入输出通讯、基于SSE的HTTP通讯，分别对应着本地与远程通讯。Client与Server间使用JSON-RPC 2.0格式进行消息传输。

- 本地通讯：使用了stdio传输数据，具体流程Client启动Server程序作为子进程，其消息通讯是通过stdin/stdout进行的，消息格式为JSON-RPC 2.0。
- 远程通讯：Client与Server可以部署在任何地方，Client使用SSE与Server进行通讯，消息的格式为JSON-RPC 2.0，Server定义了/see与/messages接口用于推送与接收数据。

这里我们尝试一个入门级的示例，那就是创建一个天气查询的服务器。通过使用OpenWeather API，创建一个能够实时查询天气的服务器（server），并使用stdio方式进行通信。

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250318171814997.png" alt="image-20250318171814997" style="zoom:50%;" />

> OpenWeather官网：https://openweathermap.org/，更多API获取方法
>
> <img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/78513c082775c213a0134cb187b2b069_.png" style="zoom:25%;" />

测试查询效果

```bash
curl -s "https://api.openweathermap.org/data/2.5/weather?q=Beijing&appid='YOUR_API_KEY'&units=metric&lang=zh_cn"
```

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250318171055694.png" alt="image-20250318171055694" style="zoom:50%;" />

测试无误后，接下来即可进入到创建server的环节中。

### 3. 天气查询服务器Server创建流程

#### 3.1 服务器依赖安装

由于我们需要使用http请求来查询天气，因此需要在当前虚拟环境中添加如下依赖

```bash
uv add mcp httpx
```

#### 3.2 服务器代码编写

接下来尝试创建服务器代码，此时MCP基本执行流程如下：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250318172155677.png" alt="image-20250318172155677" style="zoom:50%;" />

对应server服务器代码如下：

```python
import json
import httpx
from typing import Any
from mcp.server.fastmcp import FastMCP

# 初始化 MCP 服务器
mcp = FastMCP("WeatherServer")

# OpenWeather API 配置
OPENWEATHER_API_BASE = "https://api.openweathermap.org/data/2.5/weather"
API_KEY = "YOUR_API_KEY"  # 请替换为你自己的 OpenWeather API Key
USER_AGENT = "weather-app/1.0"

async def fetch_weather(city: str) -> dict[str, Any] | None:
    """
    从 OpenWeather API 获取天气信息。
    :param city: 城市名称（需使用英文，如 Beijing）
    :return: 天气数据字典；若出错返回包含 error 信息的字典
    """
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric",
        "lang": "zh_cn"
    }
    headers = {"User-Agent": USER_AGENT}

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(OPENWEATHER_API_BASE, params=params, headers=headers, timeout=30.0)
            response.raise_for_status()
            return response.json()  # 返回字典类型
        except httpx.HTTPStatusError as e:
            return {"error": f"HTTP 错误: {e.response.status_code}"}
        except Exception as e:
            return {"error": f"请求失败: {str(e)}"}

def format_weather(data: dict[str, Any] | str) -> str:
    """
    将天气数据格式化为易读文本。
    :param data: 天气数据（可以是字典或 JSON 字符串）
    :return: 格式化后的天气信息字符串
    """
    # 如果传入的是字符串，则先转换为字典
    if isinstance(data, str):
        try:
            data = json.loads(data)
        except Exception as e:
            return f"无法解析天气数据: {e}"

    # 如果数据中包含错误信息，直接返回错误提示
    if "error" in data:
        return f"⚠️ {data['error']}"

    # 提取数据时做容错处理
    city = data.get("name", "未知")
    country = data.get("sys", {}).get("country", "未知")
    temp = data.get("main", {}).get("temp", "N/A")
    humidity = data.get("main", {}).get("humidity", "N/A")
    wind_speed = data.get("wind", {}).get("speed", "N/A")
    # weather 可能为空列表，因此用 [0] 前先提供默认字典
    weather_list = data.get("weather", [{}])
    description = weather_list[0].get("description", "未知")

    return (
        f"🌍 {city}, {country}\n"
        f"🌡 温度: {temp}°C\n"
        f"💧 湿度: {humidity}%\n"
        f"🌬 风速: {wind_speed} m/s\n"
        f"🌤 天气: {description}\n"
    )

@mcp.tool()
async def query_weather(city: str) -> str:
    """
    输入指定城市的英文名称，返回今日天气查询结果。
    :param city: 城市名称（需使用英文）
    :return: 格式化后的天气信息
    """
    data = await fetch_weather(city)
    return format_weather(data)

if __name__ == "__main__":
    # 以标准 I/O 方式运行 MCP 服务器
    mcp.run(transport='stdio')
```

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250318174907749.png" alt="image-20250318174907749" style="zoom: 33%;" />

代码解释如下：

**Part 1. 异步获取天气数据**

- 函数 `fetch_weather(city: str)`
  - 使用 `httpx.AsyncClient()` 发送异步 GET 请求到 OpenWeather API。
  - 如果请求成功，则调用 `response.json()` 返回一个字典。
  - 出现异常时，返回包含错误信息的字典。

**Part 2. 格式化天气数据**

- 函数 `format_weather(data: dict | str)`
  - 首先检查传入的数据是否为字符串，如果是，则使用 `json.loads` 将其转换为字典。
  - 检查数据中是否包含 `"error"` 字段，如果有，直接返回错误提示。
  - 使用 `.get()` 方法提取 `name`、`sys.country`、`main.temp`、`main.humidity`、`wind.speed` 和 `weather[0].description` 等数据，并为可能缺失的字段提供默认值。
  - 将提取的信息拼接成一个格式化字符串，方便阅读。

**Part 3. MCP 工具 `query_weather(city: str)`**

- 函数 `query_weather`
  - 通过 `@mcp.tool()` 装饰器注册为 MCP 服务器的工具，使其能够被客户端调用。
  - 调用 `fetch_weather(city)` 获取天气数据，然后用 `format_weather(data)` 将数据格式化为易读文本，最后返回该字符串。

**Part 4. 运行服务器**

- `if __name__ == "__main__":` 块
  - 调用 `mcp.run(transport='stdio')` 启动 MCP 服务器，采用标准 I/O 通信方式，等待客户端调用。

此外，上述代码有两个注意事项，

1. query_weather函数的函数说明至关重要，相当于是此后客户端对函数进行识别的基本依据，因此需要谨慎编写；

2. **当指定 `transport='stdio'` 运行 MCP 服务器时，客户端必须在启动时同时启动当前这个脚本，否则无法顺利通信**。这是因为 **`stdio` 模式是一种本地进程间通信（IPC，Inter-Process Communication）方式**，它需要服务器作为**子进程**运行，并通过标准输入输出（`stdin`/`stdout`）进行数据交换。

因此，当我们编写完服务器后，并不能直接调用这个服务器，而是需要创建一个对应的能够进行stdio的客户端，才能顺利进行通信。

### 4. 天气查询客户端client创建流程

#### 4.1 代码编写

```python
import asyncio
import os
import json
from typing import Optional
from contextlib import AsyncExitStack

from openai import OpenAI  
from dotenv import load_dotenv

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

# 加载 .env 文件，确保 API Key 受到保护
load_dotenv()

class MCPClient:
    def __init__(self):
        """初始化 MCP 客户端"""
        self.exit_stack = AsyncExitStack()
        self.openai_api_key = os.getenv("OPENAI_API_KEY")  # 读取 OpenAI API Key
        self.base_url = os.getenv("BASE_URL")  # 读取 BASE YRL
        self.model = os.getenv("MODEL")  # 读取 model
        if not self.openai_api_key:
            raise ValueError("❌ 未找到 OpenAI API Key，请在 .env 文件中设置 OPENAI_API_KEY")
        self.client = OpenAI(api_key=self.openai_api_key, base_url=self.base_url) # 创建OpenAI client
        self.session: Optional[ClientSession] = None
        self.exit_stack = AsyncExitStack()        

    async def connect_to_server(self, server_script_path: str):
        """连接到 MCP 服务器并列出可用工具"""
        is_python = server_script_path.endswith('.py')
        is_js = server_script_path.endswith('.js')
        if not (is_python or is_js):
            raise ValueError("服务器脚本必须是 .py 或 .js 文件")

        command = "python" if is_python else "node"
        server_params = StdioServerParameters(
            command=command,
            args=[server_script_path],
            env=None
        )

        # 启动 MCP 服务器并建立通信
        stdio_transport = await self.exit_stack.enter_async_context(stdio_client(server_params))
        self.stdio, self.write = stdio_transport
        self.session = await self.exit_stack.enter_async_context(ClientSession(self.stdio, self.write))

        await self.session.initialize()

        # 列出 MCP 服务器上的工具
        response = await self.session.list_tools()
        tools = response.tools
        print("\n已连接到服务器，支持以下工具:", [tool.name for tool in tools])     
        
    async def process_query(self, query: str) -> str:
        """
        使用大模型处理查询并调用可用的 MCP 工具 (Function Calling)
        """
        messages = [{"role": "user", "content": query}]
        
        response = await self.session.list_tools()
        
        available_tools = [{
            "type": "function",
            "function": {
                "name": tool.name,
                "description": tool.description,
                "input_schema": tool.inputSchema
            }
        } for tool in response.tools]
        # print(available_tools)
        
        response = self.client.chat.completions.create(
            model=self.model,            
            messages=messages,
            tools=available_tools     
        )
        
        # 处理返回的内容
        content = response.choices[0]
        if content.finish_reason == "tool_calls":
            # 如何是需要使用工具，就解析工具
            tool_call = content.message.tool_calls[0]
            tool_name = tool_call.function.name
            tool_args = json.loads(tool_call.function.arguments)
            
            # 执行工具
            result = await self.session.call_tool(tool_name, tool_args)
            print(f"\n\n[Calling tool {tool_name} with args {tool_args}]\n\n")
            
            # 将模型返回的调用哪个工具数据和工具执行完成后的数据都存入messages中
            messages.append(content.message.model_dump())
            messages.append({
                "role": "tool",
                "content": result.content[0].text,
                "tool_call_id": tool_call.id,
            })
            
            # 将上面的结果再返回给大模型用于生产最终的结果
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
            )
            return response.choices[0].message.content
            
        return content.message.content
    
    async def chat_loop(self):
        """运行交互式聊天循环"""
        print("\n🤖 MCP 客户端已启动！输入 'quit' 退出")

        while True:
            try:
                query = input("\n你: ").strip()
                if query.lower() == 'quit':
                    break
                
                response = await self.process_query(query)  # 发送用户输入到 OpenAI API
                print(f"\n🤖 OpenAI: {response}")

            except Exception as e:
                print(f"\n⚠️ 发生错误: {str(e)}")

    async def cleanup(self):
        """清理资源"""
        await self.exit_stack.aclose()

async def main():
    if len(sys.argv) < 2:
        print("Usage: python client.py <path_to_server_script>")
        sys.exit(1)

    client = MCPClient()
    try:
        await client.connect_to_server(sys.argv[1])
        await client.chat_loop()
    finally:
        await client.cleanup()

if __name__ == "__main__":
    import sys
    asyncio.run(main())
```

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/1742291307705.jpg" alt="1742291307705" style="zoom:33%;" />

#### 4.2 测试运行

```bash
# 确认进入到项目目录
cd /root/autodl-tmp/MCP/mcp-client

# 确认激活虚拟环境
source .venv/bin/activate
```

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250318174756635.png" alt="image-20250318174756635" style="zoom:50%;" />

```bash
uv run client.py server.py
```

直接提问`请问北京今天天气如何？`运行结果如下所示：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250318175419960.png" alt="image-20250318175419960" style="zoom:50%;" />

QwQ-32B推理类模型问答效果如下：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250318175842089.png" alt="image-20250318175842089" style="zoom:50%;" />

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/78513c082775c213a0134cb187b2b069_.png" style="zoom:25%;" />

#### 4.3 代码解释

client代码整个MCP服务的核心，以下是这段代码的详细解释。

**导入基本类**

```python
import asyncio
import os
import json
from typing import Optional
from contextlib import AsyncExitStack

from openai import OpenAI  
from dotenv import load_dotenv

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
```

1. 导入必要库
   - `asyncio`：支持异步编程
   - `os` / `json`：读取环境变量、解析 JSON
   - `typing.Optional`：类型提示
   - `contextlib.AsyncExitStack`：用于安全管理异步资源（如 MCP 连接）
   - `openai.OpenAI`：你的自定义 OpenAI Client 类
   - `dotenv.load_dotenv`：从 `.env` 文件加载环境变量（如 API Key）
   - **MCP 相关**：`mcp.ClientSession`, `mcp.client.stdio`, `StdioServerParameters`

```python
load_dotenv()
```

- 从 `.env` 文件中加载环境变量,

  ```plaintext
  OPENAI_API_KEY=sk-xxxxxx
  BASE_URL=...
  MODEL=...
  ```

** `MCPClient` 类创建过程**

```python
class MCPClient:
    def __init__(self):
        """初始化 MCP 客户端"""
        self.exit_stack = AsyncExitStack()
        self.openai_api_key = os.getenv("OPENAI_API_KEY")  # 读取 OpenAI API Key
        self.base_url = os.getenv("BASE_URL")  # 读取 BASE YRL
        self.model = os.getenv("MODEL")  # 读取 model
        if not self.openai_api_key:
            raise ValueError("❌ 未找到 OpenAI API Key，请在 .env 文件中设置 OPENAI_API_KEY")
        self.client = OpenAI(api_key=self.openai_api_key, base_url=self.base_url) # 创建OpenAI client
        self.session: Optional[ClientSession] = None
        self.exit_stack = AsyncExitStack()        
```

1. **`self.exit_stack = AsyncExitStack()`**
   - 用于 **统一管理异步上下文**（如 MCP 连接）的生命周期。
   - 可以在退出（`cleanup`）时自动关闭。
2. **读取环境变量**
   - `openai_api_key`：OpenAI API Key
   - `base_url`：模型请求的 Base URL（如你自建的反代地址）
   - `model`：OpenAI 模型名称
3. **初始化 `OpenAI` 客户端**
   - `OpenAI(api_key=self.openai_api_key, base_url=self.base_url)`
   - 你自定义的 OpenAI 客户端，用来与 OpenAI Chat Completion API 通信。
4. **`self.session`**
   - 用于保存 **MCP 的客户端会话**，默认是 `None`，稍后通过 `connect_to_server` 进行连接。
5. **再次声明 `self.exit_stack = AsyncExitStack()`**
   - 这里两次赋值其实有点冗余（前面已赋值过一次）。不过并不影响功能，等同于覆盖掉前面的对象。可能是手误或调试时多写了一次。

**`connect_to_server(self, server_script_path: str)`**

```python
async def connect_to_server(self, server_script_path: str):
    ...
```

- **负责启动并连接到 MCP 服务器**，并列出可用工具。

```python
is_python = server_script_path.endswith('.py')
is_js = server_script_path.endswith('.js')
if not (is_python or is_js):
    raise ValueError("服务器脚本必须是 .py 或 .js 文件")

command = "python" if is_python else "node"
```

- 判断服务器脚本是 **Python** 还是 **Node.js**，选择对应的运行命令。

```python
server_params = StdioServerParameters(
    command=command,
    args=[server_script_path],
    env=None
)
```

- `StdioServerParameters`：告诉 MCP 客户端如何启动服务器。
  - `command=command`：如 `"python"`
  - `args=[server_script_path]`：如 `["weather_server.py"]`

```python
stdio_transport = await self.exit_stack.enter_async_context(stdio_client(server_params))
self.stdio, self.write = stdio_transport
self.session = await self.exit_stack.enter_async_context(ClientSession(self.stdio, self.write))

await self.session.initialize()
```

1. **`stdio_client(server_params)`**：启动服务器进程，并建立 **标准 I/O** 通信管道。
2. **`self.stdio, self.write = stdio_transport`**：拿到读写流。
3. **`ClientSession(...)`**：创建 MCP 客户端会话，与服务器交互。
4. **`await self.session.initialize()`**：发送初始化消息给服务器，等待服务器就绪。

```python
# 列出 MCP 服务器上的工具
response = await self.session.list_tools()
tools = response.tools
print("\n已连接到服务器，支持以下工具:", [tool.name for tool in tools])
```

- **`list_tools()`**：向 MCP 服务器请求所有已注册的工具（用 `@mcp.tool()` 标记）。
- **打印工具列表**，例如 `["get_forecast", "query_db", ...]`。

**`process_query(self, query: str) -> str`**

```python
async def process_query(self, query: str) -> str:
    """
    使用大模型处理查询并调用可用的 MCP 工具 (Function Calling)
    """
    messages = [{"role": "user", "content": query}]
```

- 收到用户输入后，先把它组装进一个 **`messages` 列表**，目前只包含用户信息（`{"role": "user", "content": query}`）。

```python
response = await self.session.list_tools()
available_tools = [{
    "type": "function",
    "function": {
        "name": tool.name,
        "description": tool.description,
        "input_schema": tool.inputSchema
    }
} for tool in response.tools]
print(available_tools)
```

- 获取服务器上的工具，再转换成 **`available_tools`** 的格式。
- 这里你自定义了一个结构：每个工具对应一个 `{"type": "function", "function": {...}}` 的字典。
- 方便后面发给 OpenAI，告诉它：**可以调用这些工具**。

```python
response = self.client.chat.completions.create(
    model=self.model,            
    messages=messages,
    tools=available_tools     
)
```

- 使用 `OpenAI` 客户端的 

  ```
  chat.completions.create
  ```

   方法发送请求：

  - `model=self.model`：比如 `"gpt-4o"` 或 `"deepseek-chat"`
  - `messages=messages`：聊天上下文
  - `tools=available_tools`：让模型知道有哪些可调用的「函数」。这是你自定义的**“Function Calling”**协议（非官方 JSON schema）。

```python
content = response.choices[0]
if content.finish_reason == "tool_calls":
    # 如果模型想调用工具
    tool_call = content.message.tool_calls[0]
    tool_name = tool_call.function.name
    tool_args = json.loads(tool_call.function.arguments)
    
    # 执行工具
    result = await self.session.call_tool(tool_name, tool_args)
    print(f"\n\n[Calling tool {tool_name} with args {tool_args}]\n\n")
    
    # 将模型返回的调用哪个工具数据和工具执行完成后的数据都存入messages中
    messages.append(content.message.model_dump())
    messages.append({
        "role": "tool",
        "content": result.content[0].text,
        "tool_call_id": tool_call.id,
    })
    
    # 将上面的结果再返回给大模型用于生产最终的结果
    response = self.client.chat.completions.create(
        model=self.model,
        messages=messages,
    )
    return response.choices[0].message.content
    
return content.message.content
```

1. `if content.finish_reason == "tool_calls":`
   - 如果模型的输出表示「想调用工具」，它会在 `content.message.tool_calls` 列表中声明要用哪个函数、参数是什么。
   - 这是你自定义的一种**函数调用机制**，和官方 `function_call` 格式略有不同，但逻辑相似。
2. **取出工具名 `tool_name` 和参数 `tool_args`**，再调用 `self.session.call_tool(tool_name, tool_args)` 执行 MCP 工具。
3. **把工具调用结果以「role=tool」的形式写入 `messages`**。这样相当于把“函数调用结果”再喂给模型。
4. **再次调用 OpenAI**，让模型阅读到这个新上下文，产出最终回答。
5. **如果没有要调用工具**，直接返回 `content.message.content`（模型的文本回答）。

**`chat_loop(self)`**

```python
async def chat_loop(self):
    """运行交互式聊天循环"""
    print("\n🤖 MCP 客户端已启动！输入 'quit' 退出")

    while True:
        try:
            query = input("\n你: ").strip()
            if query.lower() == 'quit':
                break
            
            response = await self.process_query(query)  # 发送用户输入到 OpenAI API
            print(f"\n🤖 OpenAI: {response}")

        except Exception as e:
            print(f"\n⚠️ 发生错误: {str(e)}")
```

**作用**：

- 提供一个简单的 **命令行界面**，反复让用户输入问题。
- 每个问题交给 `process_query`，把结果打印出来。
- 输入 `'quit'` 退出循环。

**`cleanup(self)` 与 `main()`**

```python
async def cleanup(self):
    """清理资源"""
    await self.exit_stack.aclose()
```

- **`self.exit_stack.aclose()`**：异步地关闭所有在 `exit_stack` 中注册的资源（包括 MCP 会话）。

```python
async def main():
    if len(sys.argv) < 2:
        print("Usage: python client.py <path_to_server_script>")
        sys.exit(1)

    client = MCPClient()
    try:
        await client.connect_to_server(sys.argv[1])
        await client.chat_loop()
    finally:
        await client.cleanup()

if __name__ == "__main__":
    import sys
    asyncio.run(main())
```

1. **读取命令行参数**，获取服务器脚本路径（如 `weather_server.py`）。
2. **创建 `MCPClient` 实例**。
3. **调用 `connect_to_server`**，启动并连接服务器。
4. **进入 `chat_loop`** 让用户输入多轮对话。
5. **退出时**调用 `client.cleanup()` 释放资源。

代码总结如下：

1. **MCPClient 的主要职责**：

   - **启动 MCP 服务器**（通过 `StdioServerParameters`）
   - **建立 MCP 会话**，列出可用工具
   - **处理用户输入**，将其发送给 OpenAI 模型
   - **如果模型想调用 MCP 工具（Function Calling）**，就执行 `call_tool`
   - **将结果重新发给模型**，并返回最终回答

2. **Function Calling 逻辑**（你的自定义版）：

   - **`tools=available_tools`**：在 `completions.create` 时告诉模型有哪些工具可用。
   - **模型返回 `finish_reason=="tool_calls"`** → 说明它想用工具。
   - **解析 `tool_calls[0]`**，执行 MCP 工具 → 再次发给模型 → 返回最终答案。

3. **为什么要两次请求？**

   - 第一次：模型根据你的指令，决定要不要用工具
   - 如果需要用工具 → 返回工具名称和参数 → 执行工具 → 把结果作为新的上下文发给模型
   - 第二次：模型基于工具结果给出最终回答

4. **如何运行**：

   ```bash
   python client.py weather_server.py
   ```

   - 这会自动启动 `weather_server.py`（MCP 服务器）并进行 stdio 通讯。

5. **可能需要的改进**：

   - **多轮对话上下文**：把所有消息都存进 `messages`，让模型能记住以前的对话。
   - **错误处理**：当工具调用失败时，给用户提示。

### 5.MCP Inspector功能介绍

​	在实际开发MCP服务器的过程中，Anthropic提供了一个非常便捷的debug工具：Inspector。借助Inspector，我们能够非常快捷的调用各类server，并测试其功能。Inspector具体功能实现流程如下。

- 安装nodejs

```bash
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo bash -
sudo apt install -y nodejs
```

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250318181922651.png" alt="image-20250318181922651" style="zoom:50%;" />

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250318181948098.png" alt="image-20250318181948098" style="zoom:50%;" />

```bash
npx -v
```

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250318182013936.png" alt="image-20250318182013936" style="zoom:50%;" />

- 运行Inspector

```bash
npx -y @modelcontextprotocol/inspector uv run server.py
```

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250318182146754.png" alt="image-20250318182146754" style="zoom:50%;" />

然后即可在本地浏览器查看当前工具运行情况：http://127.0.0.1:5173/#resources

> 注，若是使用AutoDL进行本地映射，则需要将5173和3000两个端口映射到本地
>
> <img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250318183411536.png" alt="image-20250318183411536" style="zoom:40%;" />
>
> <img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/78513c082775c213a0134cb187b2b069_.png" style="zoom:25%;" />

此时浏览器内容如下：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250318183046719.png" alt="image-20250318183046719" style="zoom:50%;" />

然后即可查看当前服务器运行状况：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250318183322326.png" alt="image-20250318183322326" style="zoom:50%;" />

## 四、MCP更多进阶使用

基于我们当前介绍的MCP开发入门，MCP还有诸多待探索的进阶功能。

### 1. MCP服务器Server进阶功能

- 基于SSE传输的MCP服务器功能实现

  ​	除了stdio连接模式外，MCP还提供了可以服务器、客户端异地运行的SSE传输模式，以适用于更加通用的开发情况。若要实现SSE的MCP服务器通信，需要同时修改客户端和服务器代码。

- Resources、Prompt类功能MCP服务器

  ​	除了Tools功能的服务器外，MCP还支持Resources类服务器和Prompt类服务器，其中Resources服务器主要负责提供更多的资源接口，如调用本地文件、数据等，而Prompt类服务器则是用于设置Agent开发过程中各环节的提示词模板。

- 更多通用公开&在线服务器调用指南

  ​	MCP标准通信协议带来的最大价值之一，就是让广大Agent开发者能够基于此进行协作。在MCP推出后的若干时间，已经诞生了数以千计的MCP服务器，允许用户直接下载并进行调用。几个有名的MCP服务器合集(导航站)地址：

  - MCP官方服务器合集：https://github.com/modelcontextprotocol/servers

    <img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250318195013063.png" alt="image-20250318195013063" style="zoom:50%;" />

  - MCP Github热门导航：https://github.com/punkpeye/awesome-mcp-servers

    <img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250318195101093.png" alt="image-20250318195101093" style="zoom:50%;" />

  - MCP集合：https://github.com/ahujasid/blender-mcp

    <img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250318195208729.png" alt="image-20250318195208729" style="zoom:50%;" />

  - MCP导航：https://mcp.so/

    <img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250318195025102.png" alt="image-20250318195025102" style="zoom:50%;" />



### 2. MCP客户端Client进阶功能

此外，除了能在命令行中创建MCP客户端外，还支持各类客户端的调用：https://modelcontextprotocol.io/clients

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250318195407915.png" alt="image-20250318195407915" style="zoom:50%;" />

其中借助对话类客户端，如Claude Destop，我们能够轻易的将各类服务器进行集成，从而拓展Claude Destop的性能：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250318195545673.png" alt="image-20250318195545673" style="zoom:50%;" />

<video src="https://pictes.oss-cn-beijing.aliyuncs.com/7114_1741882779_raw.mp4"></video>

而在一些IDE客户端里，如cline或者Cursor，我们能够直接调用服务器进行开发：

<video src="https://pictes.oss-cn-beijing.aliyuncs.com/20250314002330.mp4"></video>

此外，还有一些为MCP量身定制的Agent开发框架，通过集成MCP来提高Agent开发进度：

https://github.com/lastmile-ai/mcp-agent

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250318200250175.png" alt="image-20250318200250175" style="zoom:50%;" />

<video src="https://pictes.oss-cn-beijing.aliyuncs.com/lastmile-aimcp-agent%20Build%20effective%20agents%20using%20Model%20Context%20Protocol%20and%20simple%20workflow%20patterns.mov"></video>

# MCP快速上手使用指南

## 一、MCP基础技术回顾

### 1. MCP入门介绍

MCP，全称是Model Context Protocol，模型上下文协议，由Claude母公司Anthropic于去年11月正式提出。

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250318201338022.png" alt="image-20250318201338022" style="zoom:50%;" />

MCP刚发布的时候不温不火，直到今年Agent大爆发才被广泛关注。而在今年2月，Cursor正式宣布加入MCP功能支持，一举将MCP推到了全体开发人员面前。从本质上来说，MCP是一种技术协议，一种智能体Agent开发过程中共同约定的一种规范。这就好比秦始皇的“**书同文、车同轨**”，在统一的规范下，大家的**协作效率就能大幅提高**，最终**提升智能体Agent的开发效率**。截止目前，已上千种MCP工具诞生，在强悍的MCP生态加持下， 人人手搓Manus的时代即将到来。

> 7分钟讲清楚MCP是什么？https://www.bilibili.com/video/BV1uXQzYaEpJ/
>
> <img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250318201253260.png" alt="image-20250318201253260" style="zoom:50%;" />

总的来说**，**MCP**解决的最大痛点，就是Agent开发中调用外部工具的技术门槛过高的问题。**

我们都知道，能调用外部工具，是大模型进化为智能体Agent的关键，如果不能使用外部工具，大模型就只能是个简单的聊天机器人，甚至连查询天气都做不到。由于底层技术限制啊，大模型本身是无法和外部工具直接通信的，因此Function calling的思路，就是创建一个外部函数（function）作为中介，一边传递大模型的请求，另一边调用外部工具，最终让大模型能够间接的调用外部工具。

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250318202017508.png" alt="image-20250318202017508" style="zoom:50%;" />

例如，当我们要查询当前天气时，让大模型调用外部工具的function calling的过程就如图所示：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250318202029130.png" alt="image-20250318202029130" style="zoom:50%;" />

Function calling是个非常不错的技术设计，自诞生以来，一直被业内奉为圭臬。但唯一的问题就是，编写这个外部函数的工作量太大了，一个简单的外部函数往往就得上百行代码，而且，为了让大模型“认识”这些外部函数，我们还要额外为每个外部函数编写一个JSON Schema格式的功能说明，此外，我们还需要精心设计一个提示词模版，才能提高Function calling响应的准确率。

而MCP的目标，就是能在Agent开发过程中，让大模型更加便捷的调用外部工具。为此，MCP提出了两个方案，其一，“**车同轨、书同文**”，统一Function calling的运行规范。

首先是先统一名称，MCP把大模型运行环境称作 MCP Client，也就是MCP客户端，同时，把外部函数运行环境称作MCP Server，也就是MCP服务器，

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250318202116026.png" alt="image-20250318202116026" style="zoom:50%;" />

然后，统一MCP客户端和服务器的运行规范，并且要求MCP客户端和服务器之间，也统一按照某个既定的提示词模板进行通信。

现在，只要你本地运行的大模型支持MCP协议，也就是只要安装了相关的库，仅需几行代码即可接入这些海量的外部工具，是不是感觉Agent开发门槛瞬间降低了呢。

这种“车同轨、书同文”的规范，在技术领域就被称作协议，例如http就是网络信息交换的技术协议。各类技术协议的目标，都是希望**通过提高协作效率来提升开发效率**，而MCP，Model Context Protocol，就是一种旨在提高大模型Agent开发效率的技术协议。

那既然是协议，必然是使用的人越多才越有用。因此，为了进一普及MCP协议，Anthropic还提供了一整套MCP客户端、服务器开发的SDK，也就是开发工具，并且支持Python、TS和Java等多种语言，借助SDK，仅需几行代码，就可以快速开发一个MCP服务器。

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250318202304248.png" alt="image-20250318202304248" style="zoom:50%;" />

然后，你就可以把它接入任意一个MCP客户端来构建智能体，如果愿意，还可以把MCP服务器分享到社区，给有需求的开发者使用，甚至你还可以把你的MCP服务器放到线上运行，让用户付费使用。

而MCP的客户端，不仅支持Claude模型，也支持任意本地模型或者在线大模型，或者是一些IDE。例如，现在Cursor正式接入MCP，代表着Cursor正式成为MCP客户端，在Cursor中，我们不仅能快速编写MCP服务器（外部函数），更能借助Cursor一键连接上成百上千的开源MCP服务器，让大模型快速接入海量工具，从而大幅加快Agent开发进度。

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250318153131024.png" alt="image-20250318153131024" style="zoom:50%;" />

- 

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250318185821214.png" alt="image-20250318185821214" style="zoom:50%;" />

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250318185810201.png" alt="image-20250318185810201" style="zoom: 50%;" />

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/115746_nnq5_2720166.webp" alt="115746_nnq5_2720166" style="zoom:50%;" />

> 7分钟讲清楚MCP是什么？https://www.bilibili.com/video/BV1uXQzYaEpJ/
>
> <img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250318201253260.png" alt="image-20250318201253260" style="zoom:50%;" />

>  MCP技术开发入门实战！https://www.bilibili.com/video/BV1NLXCYTEbj/
>
>  <img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250410193755391.png" alt="image-20250410193755391" style="zoom:50%;" />

> MCP企业级智能体开发实战！https://www.bilibili.com/video/BV1n1ZuYjEzf
>
> <img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/1744285192384.jpg" alt="1744285192384" style="zoom:50%;" />

### 2.MCP服务器Server合集

- MCP官方服务器合集：https://github.com/modelcontextprotocol/servers

  <img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250318195013063.png" alt="image-20250318195013063" style="zoom:50%;" />

  MCP Github热门导航：https://github.com/punkpeye/awesome-mcp-servers

  <img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250318195101093.png" alt="image-20250318195101093" style="zoom:50%;" />

  Smithery：https://smithery.ai/

  <img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250410160659176.png" alt="image-20250410160659176" style="zoom:50%;" />

  MCP导航：https://mcp.so/

  <img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250318195025102.png" alt="image-20250318195025102" style="zoom:50%;" />

  阿里云百炼：https://bailian.console.aliyun.com/?tab=mcp

  <img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250410194437818.png" alt="image-20250410194437818" style="zoom:50%;" />

### 3. MCP热门客户端Client

​	除了能在命令行中创建MCP客户端外，还支持各类客户端的调用：https://modelcontextprotocol.io/clients

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250318195407915.png" alt="image-20250318195407915" style="zoom:50%;" />

- 课件领取：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/112dc50ee7397e91ceb7a1350d805ea.png" alt="112dc50ee7397e91ceb7a1350d805ea" style="zoom:50%;" />

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/7ccd9d3f75c4b2d042bbc4e38255241.png" alt="7ccd9d3f75c4b2d042bbc4e38255241" style="zoom:50%;" />

## 二、Cursor接入MCP工具流程

​	Cursor是一款集成了人工智能功能的现代化代码编辑器，旨在提升开发者的编码效率和体验。通过内置的AI助手，Cursor能够提供代码补全、错误检测、优化建议等智能辅助功能，帮助开发者更快速地编写高质量代码。

​	当Cursor接入MCP（Model Context Protocol）后，其功能得到了进一步扩展。MCP是由Anthropic于2024年11月推出的开放标准协议，旨在为AI模型与外部工具或数据源之间建立标准化的接口。通过MCP，Cursor可以与各种外部工具和服务进行交互，例如数据库、文件系统、浏览器等，从而使AI助手具备更强的环境感知和操作能力。

​	例如，开发者可以在Cursor中通过自然语言指令，直接让AI助手访问数据库查询数据、调用浏览器进行网页搜索，甚至控制Blender等专业软件进行3D建模操作。这种深度集成使得开发者无需离开Cursor编辑器，就能完成以往需要在多个工具之间切换才能完成的任务，大大提升了开发效率和工作流的连贯性。 

​	总之，Cursor结合MCP协议，为开发者打造了一个功能强大且高度可扩展的智能编码环境，使AI助手不仅能理解和生成代码，还能与广泛的外部工具和服务协同工作，真正实现了智能化的开发体验。

- cursor中国区官网：https://www.cursor.com/cn

  <img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250410194545407.png" alt="image-20250410194545407" style="zoom:50%;" />

- cursor 0219加入MCP功能更新公告：https://www.cursor.com/cn/changelog/agent-is-ready-and-ui-refresh?utm_source=chatgpt.com

  <img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250410194605483.png" alt="image-20250410194605483" style="zoom:50%;" />

### 1.Cursor安装与Agent模式开启

#### 1.1 Cursor安装流程

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250410155419992.png" alt="image-20250410155419992" style="zoom:50%;" />

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/112dc50ee7397e91ceb7a1350d805ea.png" alt="112dc50ee7397e91ceb7a1350d805ea" style="zoom:50%;" />

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250410155322808.png" alt="image-20250410155322808" style="zoom:50%;" />

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250410155401761.png" alt="image-20250410155401761" style="zoom:50%;" />

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250410155507702.png" alt="image-20250410155507702" style="zoom:50%;" />

#### 1.2 Cursor Agent调用模式

​	Cursor的Agent功能是其编辑器中的一项核心特性，旨在通过深度集成人工智能技术，主动与开发者的代码库交互，提供上下文相关的建议、代码生成和操作支持。Agent模式的设计目标是成为开发者的“智能编程伙伴”，帮助完成复杂任务并提升开发效率。

**Agent模式的主要功能包括：**

- **自动上下文提取**：Agent会自动从代码库中提取相关上下文信息，帮助开发者快速定位问题或生成代码。 citeturn0search0
- **运行终端命令**：无需离开编辑器，即可直接运行命令行操作。 
- **文件操作**：支持文件创建、修改、删除等操作，简化开发流程。
- **语义搜索**：通过代码语义搜索功能，快速找到关键代码片段。

启用Agent模式非常简单，只需使用快捷键 `⌘.`（Mac）或 `Ctrl + .`（Windows/Linux），即可激活Agent功能。在Agent模式下，你可以通过命令行或快捷键执行上下文管理、终端操作和文件交互等操作。 

例如，在代码重构场景中，Agent会根据代码库上下文提供优化建议，并自动生成替代代码。当代码出现错误时，Agent不仅会标注问题，还会提供详细的修复建议，并自动修复。通过Agent模式，Cursor旨在为开发者提供一个智能、高效的编程环境，减少手动操作，提高开发效率。

​	具体开启流程如下所示：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250410155755013.png" alt="image-20250410155755013" style="zoom:50%;" />

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250410195034991.png" alt="image-20250410195034991" style="zoom:50%;" />

然后在当前页面完成订阅：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250410195108295.png" alt="image-20250410195108295" style="zoom:50%;" />

然后即可采用Agent模式进行对话：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/4efa58a44b7f8fc86ac1da46c4d7c62.png" alt="4efa58a44b7f8fc86ac1da46c4d7c62" style="zoom:50%;" />

Cursor 编辑器提供三种对话模式：Ask、Agent 和 Manual，每种模式适用于不同的开发需求。

**1. Ask 模式**： 此模式主要用于探索和了解代码库，而不会对代码进行任何修改。开发者可以在该模式下向 AI 提问，获取关于代码的解释、功能说明或建议。该模式是“只读”的，不会主动更改代码。

**2. Agent 模式**： 这是 Cursor 中最为自主的模式，设计用于处理复杂的编码任务，具有全面的工具访问权限。在该模式下，Agent 可以自主探索代码库、读取文档、浏览网页、编辑文件，并运行终端命令，以高效完成任务。例如，开发者可以指示 Agent 添加新功能或重构代码，Agent 将自动执行相关操作。

**3. Manual 模式**： 此模式允许开发者手动控制 AI 对代码的修改。开发者可以选择特定的代码片段，描述希望进行的更改，AI 将根据描述提供修改建议，开发者可以选择是否应用这些更改。该模式适用于需要精确控制代码修改的场景。

### 2.将新版Cursor接入MCP

​	Cursor接入MCP的方法有很多种，我们首先尝试将更加规范、维护更好的Smithery平台上的MCP工具接入Cursor，然后再接入GitHub MCP工具。

- https://smithery.ai/

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250410160810464.png" alt="image-20250410160810464" style="zoom:50%;" />

Smithery 是一个专门用于管理和分发 MCP（Model Context Protocol）服务器的平台，旨在帮助开发者和 AI 模型轻松发现、安装和管理各种 MCP 服务器。**Smithery 平台上的 MCP 工具与 GitHub 上的 MCP 工具的对比：**

1. **托管方式：**
   - **Smithery 平台：**提供两种模式的 MCP 服务器：
     - **远程（Remote）/ 托管（Hosted）：**这些服务器由 Smithery 在其基础设施上运行，用户通过网络访问。
     - **本地（Local）：**用户可以通过 Smithery 的 CLI 工具将 MCP 服务器安装并运行在本地环境中。
   - **GitHub：**主要提供 MCP 服务器的源代码，开发者需要自行下载、配置并在本地或自有服务器上运行。
2. **安装与管理：**
   - **Smithery 平台：**提供统一的界面和 CLI 工具，简化了 MCP 服务器的发现、安装和管理过程。用户可以通过简单的命令或界面操作完成服务器的部署和配置。 
   - **GitHub：**开发者需要手动克隆仓库、安装依赖项，并根据提供的文档进行配置和运行，过程相对繁琐，需要更多的技术背景知识。
3. **安全性与控制：**
   - **Smithery 平台：**对于托管的 MCP 服务器，Smithery 声明其配置参数（如访问令牌）是临时的，不会长期存储在其服务器上。 然而，用户需信任 Smithery 的数据处理政策。
   - **GitHub：**开发者完全控制 MCP 服务器的代码和运行环境，可以自行审查代码，确保安全性和隐私性。
4. **社区与支持：**
   - **Smithery 平台：**作为 MCP 服务器的集中管理平台，Smithery 聚集了大量的 MCP 服务器，方便开发者查找和使用。
   - **GitHub：**作为全球最大的开源平台，拥有广泛的社区支持，开发者可以在相关仓库的 issue 区域提出问题或贡献代码。

#### 2.1 安装基础依赖

​	MCP 工具依赖于 Node.js 和 npm，我们需要先对其进行安装。Windows下可以在官网上进行下载安装：https://nodejs.org/zh-cn

​	在使用 Model Context Protocol（MCP）时，是否需要安装 Node.js 取决于您所选择的 MCP 服务器的实现方式。MCP 是一个开放协议，允许大型语言模型（LLM）与外部工具和数据源进行标准化交互。不同的 MCP 服务器可以使用多种编程语言实现，包括但不限于 Node.js、Python 和 Java。而目前**Node.js 实现的 MCP 服务器**：许多开发者选择使用 Node.js 来实现 MCP 服务器，主要因为其拥有丰富的包管理生态系统（如 npm），以及在处理异步操作和 I/O 密集型任务方面的高效性。例如，开发者可以使用 Node.js 快速搭建一个 MCP 服务器，以提供特定的功能或工具。

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250410161238050.png" alt="image-20250410161238050" style="zoom:50%;" />

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250410161255454.png" alt="image-20250410161255454" style="zoom:50%;" />

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/112dc50ee7397e91ceb7a1350d805ea.png" alt="112dc50ee7397e91ceb7a1350d805ea" style="zoom:50%;" />

具体安装过程一路点击下一步即可：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250410161215501.png" alt="image-20250410161215501" style="zoom:50%;" />

然后使用pip安装uv：

```bash
 pip install uv
```

安装完成后即可在cursor中查看安装结果：

```bash
node -v
npm -v
 pip show uv
```

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250410161638298.png" alt="image-20250410161638298" style="zoom:50%;" />

#### 2.2 尝试为Cursor添加MCP工具

​	**Sequential Thinking** 是一个基于 Model Context Protocol（MCP）的服务器工具，旨在通过结构化的思维流程，帮助用户动态、反思性地解决复杂问题。 该工具将问题拆解为可管理的步骤，每个步骤都可以建立在先前的见解之上，或对其进行质疑和修正，从而逐步深化对问题的理解，最终形成全面的解决方案。

![image-20250410200113606](https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250410200113606.png)

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250410200143385.png" alt="image-20250410200143385" style="zoom:50%;" />

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250410200219756.png" alt="image-20250410200219756" style="zoom:50%;" />

然后打开cursor：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250410161913241.png" alt="image-20250410161913241" style="zoom:50%;" />

并写入如下内容：

```json
    "server-sequential-thinking": {
      "command": "cmd",
      "args": [
        "/c",
        "npx",
        "-y",
        "@smithery/cli@latest",
        "run",
        "@smithery-ai/server-sequential-thinking",
        "--key",
        "..."
      ]
    }
```

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250410165602159.png" alt="image-20250410165602159" style="zoom:50%;" />

然后回到MCP Servers页面，等待验证：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250410163036544.png" alt="image-20250410163036544" style="zoom:50%;" />

验证通过后，即可开启自动调用工具选项：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250410163147222.png" alt="image-20250410163147222" style="zoom:50%;" />

点击确认：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250410163159268.png" alt="image-20250410163159268" style="zoom:50%;" />

然后进行简单问答测试，查看能否顺利调用工具：

```text
请问strawberry有几个r？请先调用sequential-thinking MCP工具进行思考，然后再回答。
```

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250410165347893.png" alt="image-20250410165347893" style="zoom:50%;" />

#### 2.4 添加Playwright MCP

​	**Playwright Automation** 是一个基于 Model Context Protocol（MCP）的服务器工具，利用 Microsoft 开发的开源浏览器自动化库 [Playwright](https://playwright.dev/)，为大型语言模型（LLMs）和 AI 助手提供与网页交互的能力。 

**主要功能：**

- **网页导航与交互**：自动执行网页导航、点击、表单填写等操作，支持复杂的用户行为模拟。 
- **内容提取与网页抓取**：从网页中提取结构化数据，适用于信息检索和内容分析。
- **截图与可视化**：捕获网页或特定元素的截图，便于调试和结果展示。
- **JavaScript 执行**：在浏览器环境中执行自定义 JavaScript 代码，满足特定的交互需求。

Playwright Automation主页：https://smithery.ai/server/@microsoft/playwright-mcp

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250410201301034.png" alt="image-20250410201301034" style="zoom:50%;" />

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250410201317069.png" alt="image-20250410201317069" style="zoom:50%;" />

然后需要在配置页面写入如下内容： 

```json
    "playwright-mcp": {
      "command": "cmd",
      "args": [
        "/c",
        "npx",
        "-y",
        "@smithery/cli@latest",
        "run",
        "@microsoft/playwright-mcp",
        "--key",
        "......"
      ]
    }
```

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250410165907725.png" alt="image-20250410165907725" style="zoom:50%;" />

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250410165919922.png" alt="image-20250410165919922" style="zoom:50%;" />

然后输入如下问题：

```tex
你好，请帮我查找MCP（Model Context Protocol）技术的相关内容，并制作一份简易的入门级调研报告，MCP官网地址在@https://github.com/modelcontextprotocol 。你可以使用server-sequential-thinking进行思考，并使用playwright-mcp进行网络信息获取。
```

此时MCP工具会自动打开网页进行刘兰兰，然后梳理总结报告内容：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250410200539435.png" alt="image-20250410200539435" style="zoom:50%;" />

#### 2.4 添加FileSystem工具

- FileSystem工具：https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250410200807795.png" alt="image-20250410200807795" style="zoom:50%;" />

**Filesystem MCP** 是一个基于 Model Context Protocol（MCP）的服务器工具，旨在为大型语言模型（LLMs）和 AI 助手提供对本地文件系统的安全、受控访问。

**主要功能：**

- **文件读写**：允许读取和写入文件内容，支持创建新文件或覆盖现有文件。
- **目录管理**：支持创建、列出和删除目录，以及移动文件或目录。
- **文件搜索**：能够在指定路径中搜索匹配特定模式的文件或目录。
- **元数据获取**：提供获取文件或目录的详细元数据，包括大小、创建时间、修改时间、访问时间、类型和权限等信息。

调用过程如下，需要写入如下配置：

```json
    "filesystem": {
      "command": "cmd",
      "args": [
        "/c",
        "npx",
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "run",
        "C:/Users/Administrator/Desktop/最新流量视频/MCP体验课/MCPTest"
      ]
    }
```

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/068d25bf9b566ea9bd52f8c10d7c51c.png" alt="068d25bf9b566ea9bd52f8c10d7c51c" style="zoom:50%;" />

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250410172135358.png" alt="image-20250410172135358" style="zoom:50%;" />

然后进行测试：

```tex
非常好，接下来请把你的这份调研报告，调用filesystem工具，以md格式写入本地文件，并取名为MCP技术初级调研报告
```

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250410172500770.png" alt="image-20250410172500770" style="zoom:50%;" />

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250410172529832.png" alt="image-20250410172529832" style="zoom:50%;" />











## 三、个人助理Cherry Studio接入MCP实现流程

​	**Cherry Studio** 是一款功能强大的桌面客户端，支持与多种大型语言模型（LLM）服务商的无缝集成，包括 OpenAI、Gemini、Anthropic 等，同时兼容本地模型，如通过 Ollama 和 LM Studio 部署的模型。该应用适用于 Windows、Mac 和 Linux 操作系统，提供了丰富的个性化选项和先进的功能，旨在帮助用户在各种场景下提升工作效率。 

**主要功能：**

- **多模型支持**：用户可以快速在不同的 LLM 之间切换，以满足不同的需求。
- **AI 助手与对话**：内置超过 300 个预配置的 AI 助手，并支持自定义助手创建，方便用户根据具体任务定制个性化助手。 
- **文档与数据处理**：支持处理多种文件格式，包括文本、图像、Office 文档和 PDF 等，内置 WebDAV 文件管理和备份功能，方便用户管理和备份文件。
- **实用工具集成**：提供全局搜索、主题管理、AI 驱动的翻译等实用工具，增强用户体验。

**接入 MCP 的优势：**

​	通过集成 Model Context Protocol（MCP），Cherry Studio 的功能得到了进一步扩展。MCP 是一个开放标准协议，旨在为 AI 系统与外部数据源之间建立标准化的接口。通过 MCP，Cherry Studio 能够与各种外部工具和服务进行交互，例如文件系统、浏览器自动化工具等，从而使 AI 助手具备更强的环境感知和操作能力。

​	例如，用户可以在 Cherry Studio 中通过自然语言指令，直接让 AI 助手访问本地文件系统、调用浏览器进行网页搜索，甚至控制其他专业软件进行特定操作。这种深度集成使得用户无需离开 Cherry Studio，就能完成以往需要在多个工具之间切换才能完成的任务，大大提升了工作效率和工作流的连贯性。

- CherryStudio主页：https://github.com/CherryHQ/cherry-studio

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250410173030758.png" alt="image-20250410173030758" style="zoom:50%;" />

### 1.Cherry Studio安装流程

- CherryStudio文档页：https://docs.cherry-ai.com/cherry-studio/download

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250410173212658.png" alt="image-20250410173212658" style="zoom:50%;" />

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250410173310435.png" alt="image-20250410173310435" style="zoom:50%;" />

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/112dc50ee7397e91ceb7a1350d805ea.png" alt="112dc50ee7397e91ceb7a1350d805ea" style="zoom:50%;" />

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250410173328364.png" alt="image-20250410173328364" style="zoom:50%;" />

下载完即可进入对话页面：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250410173425498.png" alt="image-20250410173425498" style="zoom:50%;" />

然后我们可以将模型切换为DeepSeek官方的模型API：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250410173711788.png" alt="image-20250410173711788" style="zoom:50%;" />

然后开启：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250410173810084.png" alt="image-20250410173810084" style="zoom:50%;" />

并尝试进行使用：

![image-20250410173835004](https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250410173835004.png)

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250410173851350.png" alt="image-20250410173851350" style="zoom:50%;" />

同时，为了能顺利调用MCP工具，我们还需要安装uv和bun文件：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250410174056652.png" alt="image-20250410174056652" style="zoom:50%;" />

这里推荐最快速的方法是直接从网盘中进行下载：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250410201652820.png" alt="image-20250410201652820" style="zoom:50%;" />

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/112dc50ee7397e91ceb7a1350d805ea.png" alt="112dc50ee7397e91ceb7a1350d805ea" style="zoom:50%;" />

然后在C:\Users\{用户名}下创建.cherrystudio\bin目录，并将上面三个.exe文件移入即可。

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250410175446175.png" alt="image-20250410175446175" style="zoom:50%;" />

其他操作系统配置详见：https://docs.cherry-ai.com/advanced-basic/mcp/install

### 2. Cherry Studio接入MCP流程

​	接下来尝试接入filesystem MCP工具：https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem 。

需要在编辑MCP配置页面输入如下内容：

```bash
{
  "mcpServers": {
    "filesystem": {
      "isActive": true,
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "C:/Users/Administrator/Desktop/最新流量视频/MCP体验课/MCPTest"
      ],
      "name": "filesystem"
    }
  }
}
```

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250410180511066.png" alt="image-20250410180511066" style="zoom:50%;" />

然后点击开启：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250410180528836.png" alt="image-20250410180528836" style="zoom:50%;" />

然后在对话中开启MCP工具，这里可选一个或者多个工具：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250410180551092.png" alt="image-20250410180551092" style="zoom:50%;" />

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250410180609064.png" alt="image-20250410180609064" style="zoom:50%;" />

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250410180756057.png" alt="image-20250410180756057" style="zoom:50%;" />

同时再尝试接入fetch MCP工具，https://github.com/modelcontextprotocol/servers/tree/main/src/fetch：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250410202128923.png" alt="image-20250410202128923" style="zoom:50%;" />

**Fetch MCP 服务器**是一个遵循模型上下文协议（Model Context Protocol，MCP）的服务器工具，旨在为大型语言模型（LLMs）提供从互联网检索和处理网页内容的能力。通过将网页的 HTML 内容转换为 Markdown 格式，Fetch MCP 使得 LLMs 能够更高效地理解和利用网页信息。 

**主要功能：**

- **网页内容获取与转换**：Fetch MCP 提供了 `fetch` 工具，可从指定的 URL 获取网页内容，并将其提取为 Markdown 格式，方便 LLMs 消化和处理。 
- **支持多种内容格式**：除了 Markdown，Fetch MCP 还支持获取网页的 HTML、JSON 和纯文本格式，满足不同应用场景的需求。 
- **内容截取与分页**：通过 `start_index` 参数，用户可以指定从网页内容的特定位置开始提取，允许模型分段读取网页，直到找到所需信息。

同样我们需要在MCP配置页面写入如下内容 

```bash
  "fetch": {
    "command": "uvx",
    "args": ["mcp-server-fetch"]
  }
```

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250410181114879.png" alt="image-20250410181114879" style="zoom:50%;" />

然后开启工具：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250410181143902.png" alt="image-20250410181143902" style="zoom:50%;" />

并尝试进行调用：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250410181401590.png" alt="image-20250410181401590" style="zoom:50%;" />

## 四、阿里云百炼平台接入MCP

- 阿里云百炼平台：https://bailian.console.aliyun.com/#/home

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250410183112382.png" alt="image-20250410183112382" style="zoom:50%;" />

### 1. 阿里云百炼平台介绍

​	**阿里云百炼平台**是一款一站式的大模型开发及应用构建平台，旨在帮助开发者和业务人员快速设计和构建大模型应用。用户可以通过简洁的界面操作，在短时间内开发出大模型应用或训练专属模型，从而将更多精力专注于应用创新。

​	近期，阿里云百炼平台正式推出了全生命周期的MCP（Model-Connect-Protocol）服务，实现了从资源管理到部署运维的全流程自动化。用户仅需5分钟即可快速创建连接MCP服务的智能体（Agent），将大模型技术转化为生产力工具。首批集成了包括高德地图、无影、Fetch、Notion等50余款阿里巴巴集团及第三方MCP服务，覆盖生活服务、办公协同、内容创作等多个领域。 

**接入MCP的优势：**

1. **快速开发与部署**：通过MCP服务，用户无需管理资源、开发部署和工程运维等复杂工作，可在短时间内搭建并上线智能体应用。 
2. **丰富的生态系统**：百炼平台整合了200多款业界领先的大模型和阿里云函数计算资源，以及众多MCP服务，提供一站式智能体开发解决方案，满足不同场景的应用需求。 
3. **深度场景化定制**：与市场上通用的Agent应用不同，百炼MCP服务支持深度场景化定制。用户无需编写代码，通过简单的可视化配置即可打造具备自主思考、任务拆解和决策执行等能力的专属智能体。
4. **持续扩展的应用边界**：随着MCP协议生态的不断扩展，百炼平台将持续引入更多阿里巴巴集团及第三方应用服务，进一步拓宽智能体的应用边界，推动大模型技术在各行业的落地应用。 

通过接入MCP服务，阿里云百炼平台为用户提供了高效、便捷的大模型应用开发环境，降低了开发门槛，加速了大模型技术的产业化应用进程。

### 2. 阿里云百炼接入MCP流程

然后我们进入MCP服务中心，先选择高德MCP工具进行测试：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250410183230280.png" alt="image-20250410183230280" style="zoom:50%;" />

点击开启服务：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250410183244647.png" alt="image-20250410183244647" style="zoom:50%;" />

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250410183301666.png" alt="image-20250410183301666" style="zoom:50%;" />

**高德地图 MCP 工具**是高德地图基于 MCP 协议构建的服务器，整合了高德开放平台的地图服务与智能算法，为企业及开发者提供全场景的地图服务解决方案。 其 12 项核心功能涵盖了地图服务的方方面面，满足企业开发的多样化需求。

**主要功能：**

- **POI 智能提取**：能够从文字中精准提取 POI（兴趣点）信息，涵盖位置、详情、打卡点、价格等多维度内容。
- **路径规划**：提供驾车、步行、骑行等多种出行方式的路径规划服务，帮助用户选择最优路线。
- **实时路况查询**：实时查询特定道路或区域的拥堵状况及趋势，为出行提供及时参考。
- **天气查询**：通过经纬度信息，获取实时天气情况及未来天气预报，为用户出行计划提供支持。

通过高德地图 MCP 工具，AI 智能体可以直接调用高德地图的各项服务，实现如位置查询、路线规划、实时路况查询等功能，提升用户体验和服务效率。

然后进入应用管理，即可看到当前开启的MCP服务：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250410183342783.png" alt="image-20250410183342783" style="zoom:50%;" />

然后点击创建新的应用，其实也就是新的Agent：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250410183640222.png" alt="image-20250410183640222" style="zoom:50%;" />

点击创建

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250410183654844.png" alt="image-20250410183654844" style="zoom:50%;" />

然后即可进行模型和MCP工具配置了：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250410183724497.png" alt="image-20250410183724497" style="zoom:50%;" />

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250410183748066.png" alt="image-20250410183748066" style="zoom:50%;" />

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250410183809050.png" alt="image-20250410183809050" style="zoom:50%;" />

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250410183823668.png" alt="image-20250410183823668" style="zoom:50%;" />

然后输入系统提示词：你是一名经验丰富的导游，请耐心认真的为用户规划出游行程。

![image-20250410184005617](https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250410184005617.png)

然后测试进行出游路线规划：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250410184123020.png" alt="image-20250410184123020" style="zoom:50%;" />

能够看到规划结果和MCP工具调用流程：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250410184626378.png" alt="image-20250410184626378" style="zoom:50%;" />

### 2. Firecrawl MCP工具

​	**Firecrawl MCP 工具**是一款基于模型上下文协议（MCP）的企业级网页数据采集服务器，由 Mendable.ai 开发，专门针对复杂网页场景设计。它支持 JavaScript 动态渲染、批量数据处理、智能内容搜索和深度网页爬取等高级功能，能够为大型语言模型（LLM）提供强大的网页抓取能力。

**主要功能：**

- **JavaScript 渲染**：能够处理动态网页内容，突破传统抓取工具的局限，获取更全面的数据。
- **批量处理**：支持并行处理和队列管理，提高数据抓取效率。
- **智能限速**：根据网络状况和任务需求智能调整抓取速度，避免对目标网站造成过大压力。
- **多种输出格式**：支持将抓取的内容转换为 Markdown、HTML 等格式，满足不同场景的需求。

通过 Firecrawl MCP 工具，开发者可以高效地从网页提取结构化数据，增强 LLM 在信息检索和内容生成方面的能力。

> **Firecrawl**和**Fetch**都是基于模型上下文协议（MCP）的服务器工具，旨在增强大型语言模型（LLMs）对网页内容的获取和处理能力，但它们在功能和适用场景上存在显著差异。
>
> **Firecrawl MCP 工具：**
>
> - **高级网页抓取**：Firecrawl 专为复杂的网页抓取任务设计，支持 JavaScript 渲染，能够处理动态内容丰富的网站。
> - **批量处理与深度爬取**：具备批量数据处理、URL 发现和深度爬取能力，适用于大规模数据采集任务。
> - **智能内容搜索**：内置智能内容搜索和提取功能，能够高效地从网页中提取结构化数据。 
>
> **Fetch MCP 工具：**
>
> - **网页内容获取与转换**：Fetch 主要用于从指定的 URL 获取网页内容，并将 HTML 转换为 Markdown 格式，便于 LLMs 理解和处理。 
> - **轻量级设计**：Fetch 注重简洁和易用，适合需要快速获取和转换网页内容的场景。

![image-20250410184728546](https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250410184728546.png)

然后需要创建Firecrawl API：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250410184741566.png" alt="image-20250410184741566" style="zoom:50%;" />

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250410184755609.png" alt="image-20250410184755609" style="zoom:50%;" />

点击复制即可：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250410184850789.png" alt="image-20250410184850789" style="zoom:50%;" />

然后开启Firecrawl MCP工具：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250410184930387.png" alt="image-20250410184930387" style="zoom:50%;" />

然后输入系统提示词

```tex
##  角色设定（优化版）
你是一位**内容整理专家**，擅长高效提取网页中的关键信息。
##  核心技能
### 查询与总结网页内容
- 根据用户提供的网页链接，使用 **Firecrawl MCP 工具** 抓取网页主内容（以 Markdown 格式返回）。
- 阅读并理解网页信息，**用中文提炼出关键要点与核心观点**。
- 生成结构清晰、逻辑完整的内容总结，适合直接用于知识管理或随手记录
## 限制要求
1. 所有内容总结必须为**中文**。
2. 每条记录只添加一个标签。
3. 标签书写规范：`#标签`，前缀为 `#`，**无空格**。
```

并尝试爬取网页内容：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250410185859891.png" alt="image-20250410185859891" style="zoom:50%;" />

### 3. 百炼应用API获取与调用

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250410202824450.png" alt="image-20250410202824450" style="zoom:50%;" />

![image-20250410202834203](https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250410202834203.png)

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250410202849677.png" alt="image-20250410202849677" style="zoom:50%;" />

然后我们即可使用API来调用已经创建好的应用：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250410190418532.png" alt="image-20250410190418532" style="zoom:50%;" />

```python
!pip install dashscope 
import os
from http import HTTPStatus
from dashscope import Application

response = Application.call(
    api_key=DASHSCOPE_API_KEY,  # 替换为实际API-KEY
    app_id=APP_ID,              # 替换为实际的应用 ID
    prompt='你是谁？')
print(response.output.text)

prompt = '请帮我详细整理下这个网页里的内容：https://docs.cherry-ai.com/'
response = Application.call(
    api_key=DASHSCOPE_API_KEY,  # 替换为实际API-KEY
    app_id=APP_ID,              # 替换为实际的应用 ID
    prompt=prompt)
print(response.output.text)
```

具体执行效果如图所示：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250410190755768.png" alt="image-20250410190755768" style="zoom:50%;" />

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250410191247311.png" alt="image-20250410191247311" style="zoom:50%;" />

## 五、Open-WebUI接入MCP流程

- Open-WebUI：https://github.com/open-webui/open-webui

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250410203538794.png" alt="image-20250410203538794" style="zoom:50%;" />

​	**Open WebUI** 是一款可扩展、功能丰富且用户友好的自托管 AI 平台，旨在完全离线运行。它支持多种大型语言模型（LLM）运行环境，包括 Ollama 和兼容 OpenAI 的 API。

**主要功能：**

- **多模型支持**：兼容多种 LLM 运行环境，用户可以根据需求选择适合的模型进行部署和交互。 
- **离线运行**：设计上支持完全离线操作，确保数据隐私和安全，适合对数据敏感的应用场景。 
- **用户友好界面**：提供类似 ChatGPT 的交互界面，方便用户与本地或远程部署的语言模型进行对话。
- **自托管部署**：支持通过 Docker 等方式进行自托管部署，方便用户在本地环境中运行和管理。 

### 1. 【可选】借助ollama拉取模型

#### 1.1 ollama安装与部署

​	Open-WebUI原生支持使用Ollama调用本地模型进行推理，Ollama是一款大模型下载、管理、推理、优化集一体的强大工具，可以快速调用各类离线部署的大模型。Ollama官网：https://ollama.com/

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250214143023223.png" alt="image-20250214143023223" style="zoom:50%;" />

- 【安装方案一】Ollama在线安装

  在Linux系统中，可以使用如下命令快速安装Ollama

  ```bash
  curl -fsSL https://ollama.com/install.sh | sh
  ```

  <img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250214143116075.png" alt="image-20250214143116075" style="zoom:50%;" />

  <img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/202501222020849.png" alt="image-20250122202031784" style="zoom:50%;" />

  但该下载流程会受限于国内网络环境，下载过程并不稳定。

- 【安装方案二】Ollama离线安装

  因此，在更为一般的情况下，推荐使用Ollama离线部署。我们可以在Ollama Github主页查看目前Ollama支持的各操作系统安装包：https://github.com/ollama/ollama/releases

  <img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250410203616284.png" alt="image-20250410203616284" style="zoom:50%;" />

  若是Ubuntu操作系统，选择其中`ollama-linux-amd64.tgz`下载和安装即可。

  此外，安装包也可从网盘中下载：

  <img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250410203634009.png" alt="image-20250410203634009" style="zoom:50%;" />

  <img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/112dc50ee7397e91ceb7a1350d805ea.png" style="zoom:50%;" />

  下载完成后，需要先上传至服务器：

  <img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250214120537243.png" alt="image-20250214120537243" style="zoom:50%;" />

  然后使用如下命令进行解压缩

  ```bash
  mkdir ./ollama
  tar -zxvf ollama-linux-amd64.tgz -C ./ollama
  ```

  解压缩后项目文件如图所示：

  <img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250214143624849.png" alt="image-20250214143624849" style="zoom:50%;" />

  而在bin中，可以找到ollama命令的可执行文件。

  <img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250214143654513.png" alt="image-20250214143654513" style="zoom:50%;" />

  此时，我们可以使用如下方式使用ollama：

  ```bash
  cd ./bin
  ./ollama help
  ```

  <img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250214143756130.png" alt="image-20250214143756130" style="zoom:50%;" />

  > 此处若显示没有可执行权限，可以使用如下命令为当前脚本添加可执行权限：
  >
  > ```bash
  > chmod +x ollama
  > ```

  而为了使用命令方便，我们也可以将脚本文件写入环境变量中。我们可以在主目录（root）下找到.bashrc文件：

  ![image-20250214144012447](https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250214144012447.png)

  然后在`.bashrc`文件结尾写入ollama/bin文件路径：

  <img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250214144306637.png" alt="image-20250214144306637" style="zoom:50%;" />

  ```bash
  export PATH=$PATH:/root/autodl-tmp/ollama/bin
  ```

  保存并退出后，输入如下命令来使环境变量生效：

  ```bash
  source ~/.bashrc
  ```

  然后在任意路径下输入如下命令，测试ollama环境变量是否生效

  ```bash
  ollama help
  ```

  <img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250214144523792.png" alt="image-20250214144523792" style="zoom:50%;" />

- 【可选】更换Ollama默认模型权重下载地址

  接下来我们需要使用ollama来下载模型，但默认情况下，ollama会将模型下载到/root/.ollama文件夹中，会占用系统盘空间，因此，若有需要，可以按照如下方法更换模型权重下载地址。

  此外无论是在线还是离线安装的ollama，都可以按照如下方法更换模型权重下载地址。还是需要打开`/root/.bashrc`文件，写入如下代码：

  ```bash
  export OLLAMA_MODELS=/root/autodl-tmp/models
  ```

  <img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250214152148066.png" alt="image-20250214152148066" style="zoom:50%;" />

  > 这里的路径需要改写为自己的文件地址

  保存并退出后，输入如下命令来使环境变量生效：

  ```bash
  source ~/.bashrc
  ```

  测试环境变量是否生效

  ```bash
  echo $OLLAMA_MODELS
  ```

  <img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250214152220067.png" alt="image-20250214152220067" style="zoom:50%;" />

- 启动ollama

  接下来即可启动ollama，为后续下载模型做准备：

  ```bash
  ollama start
  ```

  <img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250214150512236.png" alt="image-20250214150512236" style="zoom:50%;" />

  > 注意，在整个应用使用期间，需要持续开启Ollama。

#### 1.2 下载Gemma-27B模型

```bash
ollama run gemma3:27b
```

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250410185918681.png" alt="image-20250410185918681" style="zoom:50%;" />

```bash
ollama list
```

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250410185950336.png" alt="image-20250410185950336" style="zoom:50%;" />

实际显存占用：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250410190112875.png" alt="image-20250410190112875" style="zoom:50%;" />

### 2. Open-WebUI安装与调用

```bash
pip isntall open-webui
```

​	在准备好了Open-WebUI和一系列模型权重后，接下来我们尝试启动Open-WebUI，并借助本地模型进行问答。

首先需要设置离线环境，避免Open-WebUI启动时自动进行模型下载：

```bash
export HF_HUB_OFFLINE=1
```

然后启动Open-WebUI

```bash
open-webui serve
```

需要注意的是，如果启动的时候仍然报错显示无法下载模型，是Open-WebUI试图从huggingface上下载embedding模型，之后我们会手动将其切换为本地运行的Embedding模型。

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250214154657014.png" alt="image-20250214154657014" style="zoom:50%;" />

然后在本地浏览器输入地址:8080端口即可访问：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250214154949305.png" alt="image-20250214154949305" style="zoom:50%;" />

> 若使用AutoDL，则需要使用SSH隧道工具进行地址代理
>
> <img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250214155045849.png" alt="image-20250214155045849" style="zoom:50%;" />
>
> 更多AutoDL相关操作详见公开课：《AutoDL快速入门与GPU租赁使用指南》|https://www.bilibili.com/video/BV1bxB7YYEST/
>
> <img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250205182609797.png" alt="image-20250205182609797" style="zoom:50%;" />

然后首次使用前，需要创建管理员账号：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250214155158043.png" alt="image-20250214155158043" style="zoom:50%;" />

然后点击登录即可。需要注意的是，此时Open-WebUI会自动检测后台是否启动了ollama服务，并列举当前可用的模型。稍等片刻，即可进入到如下页面：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250214155430327.png" alt="image-20250214155430327" style="zoom:50%;" />

接下来即可进入到对话页面：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250410190311252.png" alt="image-20250410190311252" style="zoom:50%;" />

### 3. Open-WebUI接入MCP流程

- MCP Support：https://docs.openwebui.com/openapi-servers/mcp

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250410191007622.png" alt="image-20250410191007622" style="zoom:50%;" />

最新Open WebUI 提供的 MCP（Model Context Protocol）到 OpenAPI 的代理服务器（mcpo）MCP 到 OpenAPI 的代理服务器让你可以通过标准的 REST/OpenAPI API 来直接使用基于 MCP（模型上下文协议）实现的工具服务器——无需学习或处理任何复杂的自定义协议。

💡 为什么使用 mcpo？

尽管 MCP 工具服务器功能强大、灵活，但它们通常通过标准输入/输出（stdio）进行通信——这意味着它们通常运行在本地，可以方便地访问文件系统、环境变量及其他系统资源。这既是优势，也是一种限制。

因为 MCP 服务器通常依赖于原始的 stdio 通信方式，它：

- 🔓 在跨环境使用时不安全
- ❌ 与大多数现代工具、UI 或平台不兼容
- 🧩 缺乏认证、文档和错误处理等关键特性

而 **mcpo 代理** 自动解决了这些问题：

- ✅ 与现有的 OpenAPI 工具、SDK 和客户端即时兼容
- 🛡 将你的工具包裹为安全、可扩展、基于标准的 HTTP 接口
- 🧠 自动为每个工具生成交互式 OpenAPI 文档，**无需任何配置**
- 🔌 使用纯 HTTP——无需配置 socket、不用管理后台服务或编写平台相关代码

因此，虽然引入 mcpo 表面上看像是“又多了一层”，但实际上它：

 ✅ 简化了集成流程
 ✅ 提升了安全性
 ✅ 强化了可扩展性
 ✅ 让开发者和用户更满意

✨ 有了 mcpo，你本地运行的 AI 工具可以立刻支持云端部署、适配各种 UI，并实现无缝交互——**无需修改工具服务器代码中的任何一行。**

✅ 快速开始：本地运行代理服务器

```bash
pip install uv
pip install mcpo
```

接下来我们可以通过以下命令运行推荐的 MCP 服务器（如 `mcp-server-time`）并同时通过 `mcpo` 代理进行开放：

```bash
uvx mcpo --port 8000 -- uvx mcp-server-time --local-timezone=Asia/Shanghai
```

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250410192320280.png" alt="image-20250410192320280" style="zoom:50%;" />

> <img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250410193307791.png" alt="image-20250410193307791" style="zoom:50%;" />

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250410193401809.png" alt="image-20250410193401809" style="zoom:50%;" />

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250410193420567.png" alt="image-20250410193420567" style="zoom:50%;" />

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250410193343011.png" alt="image-20250410193343011" style="zoom:50%;" />

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250410193450253.png" alt="image-20250410193450253" style="zoom:50%;" />

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250410193517255.png" alt="image-20250410193517255" style="zoom:50%;" />

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250410193606486.png" alt="image-20250410193606486" style="zoom:50%;" />

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250410193623745.png" alt="image-20250410193623745" style="zoom:50%;" />

⚡️ MCP 到 OpenAPI 代理的优势

为什么通过代理使用 MCP 工具服务器是更优选择？Open WebUI 强烈推荐这一方式：

- **用户友好且熟悉的接口**：不需要学习新的客户端，只需使用你熟悉的 HTTP 接口
- **即时集成**：与数千个现有的 REST/OpenAPI 工具、SDK 和服务无缝兼容
- **强大自动文档支持**：Swagger UI 自动生成、准确维护
- **无需新协议开销**：免去直接处理 MCP 协议复杂性和 socket 通信问题
- **稳定安全**：沿用成熟的 HTTPS、认证机制（如 JWT、API key）、FastAPI 的可靠架构
- **面向未来**：使用标准 REST/OpenAPI，长期获得社区支持与发展

# MCP智能体开发实战入门

[toc]

- Anthropic MCP发布通告：https://www.anthropic.com/news/model-context-protocol
- MCP GitHub主页：https://github.com/modelcontextprotocol

## 一、MCP技术体系介绍

### 1. MCP入门介绍

MCP，全称是Model Context Protocol，模型上下文协议，由Claude母公司Anthropic于去年11月正式提出。

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250318201338022.png" alt="image-20250318201338022" style="zoom:50%;" />

MCP刚发布的时候不温不火，直到今年Agent大爆发才被广泛关注。而在今年2月，Cursor正式宣布加入MCP功能支持，一举将MCP推到了全体开发人员面前。从本质上来说，MCP是一种技术协议，一种智能体Agent开发过程中共同约定的一种规范。这就好比秦始皇的“**书同文、车同轨**”，在统一的规范下，大家的**协作效率就能大幅提高**，最终**提升智能体Agent的开发效率**。截止目前，已上千种MCP工具诞生，在强悍的MCP生态加持下， 人人手搓Manus的时代即将到来。

> 7分钟讲清楚MCP是什么？https://www.bilibili.com/video/BV1uXQzYaEpJ/
>
> <img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250318201253260.png" alt="image-20250318201253260" style="zoom:50%;" />

总的来说**，**MCP**解决的最大痛点，就是Agent开发中调用外部工具的技术门槛过高的问题。**

我们都知道，能调用外部工具，是大模型进化为智能体Agent的关键，如果不能使用外部工具，大模型就只能是个简单的聊天机器人，甚至连查询天气都做不到。由于底层技术限制啊，大模型本身是无法和外部工具直接通信的，因此Function calling的思路，就是创建一个外部函数（function）作为中介，一边传递大模型的请求，另一边调用外部工具，最终让大模型能够间接的调用外部工具。

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250318202017508.png" alt="image-20250318202017508" style="zoom:50%;" />

例如，当我们要查询当前天气时，让大模型调用外部工具的function calling的过程就如图所示：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250318202029130.png" alt="image-20250318202029130" style="zoom:50%;" />

Function calling是个非常不错的技术设计，自诞生以来，一直被业内奉为圭臬。但唯一的问题就是，编写这个外部函数的工作量太大了，一个简单的外部函数往往就得上百行代码，而且，为了让大模型“认识”这些外部函数，我们还要额外为每个外部函数编写一个JSON Schema格式的功能说明，此外，我们还需要精心设计一个提示词模版，才能提高Function calling响应的准确率。

而MCP的目标，就是能在Agent开发过程中，让大模型更加便捷的调用外部工具。为此，MCP提出了两个方案，其一，“**车同轨、书同文**”，统一Function calling的运行规范。

首先是先统一名称，MCP把大模型运行环境称作 MCP Client，也就是MCP客户端，同时，把外部函数运行环境称作MCP Server，也就是MCP服务器，

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250318202116026.png" alt="image-20250318202116026" style="zoom:50%;" />

然后，统一MCP客户端和服务器的运行规范，并且要求MCP客户端和服务器之间，也统一按照某个既定的提示词模板进行通信。

“车同轨、书同文”最大的好处就在于，可以避免MCP服务器的重复开发，也就是避免外部函数重复编写。例如，像查询天气、网页爬取、查询本地MySQL数据库这种通用的需求，大家有一个人开发了一个服务器就好，开发完大家都能复制到自己的项目里来使用，不用每个人每次都单独写一套。

这可是促进全球AI开发者共同协作的好事儿，很快，GitHub上就出现了海量的已经开发好的MCP 服务器，从SQL数据库检索、到网页浏览信息爬取，从命令行操作电脑、到数据分析机器学习建模，等等等等，不一而足。

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/888b152a-b366-481e-9de3-244cf5119028.png" alt="888b152a-b366-481e-9de3-244cf5119028" style="zoom:33%;" />

现在，只要你本地运行的大模型支持MCP协议，也就是只要安装了相关的库，仅需几行代码即可接入这些海量的外部工具，是不是感觉Agent开发门槛瞬间降低了呢。

这种“车同轨、书同文”的规范，在技术领域就被称作协议，例如http就是网络信息交换的技术协议。各类技术协议的目标，都是希望**通过提高协作效率来提升开发效率**，而MCP，Model Context Protocol，就是一种旨在提高大模型Agent开发效率的技术协议。

那既然是协议，必然是使用的人越多才越有用。因此，为了进一普及MCP协议，Anthropic还提供了一整套MCP客户端、服务器开发的SDK，也就是开发工具，并且支持Python、TS和Java等多种语言，借助SDK，仅需几行代码，就可以快速开发一个MCP服务器。

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250318202304248.png" alt="image-20250318202304248" style="zoom:50%;" />

然后，你就可以把它接入任意一个MCP客户端来构建智能体，如果愿意，还可以把MCP服务器分享到社区，给有需求的开发者使用，甚至你还可以把你的MCP服务器放到线上运行，让用户付费使用。

而MCP的客户端，不仅支持Claude模型，也支持任意本地模型或者在线大模型，或者是一些IDE。例如，现在Cursor正式接入MCP，代表着Cursor正式成为MCP客户端，在Cursor中，我们不仅能快速编写MCP服务器（外部函数），更能借助Cursor一键连接上成百上千的开源MCP服务器，让大模型快速接入海量工具，从而大幅加快Agent开发进度。

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250318153131024.png" alt="image-20250318153131024" style="zoom:50%;" />

- 

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250318185821214.png" alt="image-20250318185821214" style="zoom:50%;" />

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250318185810201.png" alt="image-20250318185810201" style="zoom: 50%;" />

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/115746_nnq5_2720166.webp" alt="115746_nnq5_2720166" style="zoom:50%;" />

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/d21b2749927d9e817702742924381d4.png" alt="d21b2749927d9e817702742924381d4" style="zoom:50%;" />

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250320200932493.png" alt="image-20250320200932493" style="zoom:50%;" />

### 2. MCP智能体开发入门项目

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/2bc296344f628da9922f47d501cb248.png" alt="2bc296344f628da9922f47d501cb248" style="zoom:33%;" />

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250320195529610.png" alt="image-20250320195529610" style="zoom:50%;" />

## 二、GraphRAG基于知识图谱的检索增强技术

>  【6小时最强合集】GraphRAG从原理到实战技术精讲：https://www.bilibili.com/video/BV1uCifYLEQd/
>
>  <img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250320173643435.png" alt="image-20250320173643435" style="zoom: 25%;" />
>
>  GraphRAG 项目地址：https://github.com/microsoft/graphrag/
>
>  <img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20241128154854230.png" alt="image-20241128154854230" style="zoom:33%;" />

### 1.GraphRAG入门介绍

&emsp;&emsp;**检索增强生成（RAG）** 是一种通过结合真实世界的信息来提升大型语言模型（LLM）输出质量的技术。RAG 技术是大多数基于 LLM 的工具中的一个重要组成部分。大多数 RAG 方法使用 **向量相似性** 作为检索技术，我们将其称为 **基线 RAG（Baseline RAG）**。

&emsp;&emsp;RAG 技术在帮助 LLM 推理私有数据集方面显示了很大的潜力——例如，LLM 没有在训练时接触过的、企业的专有研究、业务文档或通信数据。基线 RAG 技术最初是为了解决这个问题而提出的，但我们观察到，在某些情况下，基线 RAG 的表现并不理想。以下是几个典型的场景：

1. **基线 RAG 很难将信息串联起来**：当一个问题的答案需要通过多个不同的信息片段，并通过它们共享的属性来连接，进而提供新的综合见解时，基线 RAG 表现得很差。

   例如，在回答类似“如何通过现有的数据推断出新结论”这种问题时，基线 RAG 无法很好地处理这些散布在不同文档中的相关信息，它可能会遗漏一些关键联系点。

2. **基线 RAG 无法有效理解大型数据集或单一大文档的整体语义概念**：当被要求在大量数据或复杂文档中进行总结、提炼和理解时，基线 RAG 往往表现不佳。

   例如，如果问题要求对整个文档或多篇文档的主题进行总结和理解，基线 RAG 的简单向量检索方法可能无法处理文档间的复杂关系，导致对全局语义的理解不完整。

&emsp;&emsp;为了应对这些挑战，技术社区正在努力开发扩展和增强 RAG 的方法。**微软研究院**（Microsoft Research）提出的 **GraphRAG** 方法，使用 **LLM** 基于输入语料库构建 **知识图谱**。这个图谱与社区总结和图谱机器学习输出结合，能够在查询时增强提示（prompt）。GraphRAG 在回答以上两类问题时，展示了 **显著的改进**，尤其是在 **复杂信息的推理能力** 和 **智能性** 上，超越了基线 RAG 之前应用于私有数据集的其他方法。

<img src="https://snowball101.oss-cn-beijing.aliyuncs.com/img/202404101838975.png" alt="image-20250202191312085" style="zoom:50%;" />

### 2.GraphRAG基本原理回顾

​	**GraphRAG** 是微软研究院开发的一种先进的增强检索生成（RAG）框架，旨在提升语言模型（LLM）在处理复杂数据时的性能。与传统的 RAG 方法依赖向量相似性检索不同，**GraphRAG** 利用 **知识图谱** 来显著增强语言模型的问答能力，特别是在处理私有数据集或大型、复杂数据集时表现尤为出色。

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/2bc296344f628da9922f47d501cb248.png" alt="2bc296344f628da9922f47d501cb248" style="zoom:33%;" />

&emsp;&emsp;传统的 **Baseline RAG** 方法在某些情况下表现不佳，尤其是当查询需要在不同信息片段之间建立联系时，或是当需要对大规模数据集进行整体理解时。GraphRAG 通过以下方式克服了这些问题：

- **更好的连接信息点**：GraphRAG 能够处理那些需要从多个数据点合成新见解的任务。
- **更全面的理解能力**：GraphRAG 更擅长对大型数据集进行全面理解，能够更好地处理复杂的抽象问题。

&emsp;&emsp;而借助微软开源的GeaphRAG项目，我们可以快速做到以下事项：

- **基于图的检索**：传统的 RAG 方法使用向量相似性进行检索，而 GraphRAG 引入了知识图谱来捕捉实体、关系及其他重要元数据，从而更有效地进行推理。
- **层次聚类**：GraphRAG 使用 **Leiden** 技术进行层次聚类，将实体及其关系进行组织，提供更丰富的上下文信息来处理复杂的查询。
- **多模式查询**：支持多种查询模式：
  - **全局搜索**：通过利用社区总结来进行全局性推理。
  - **局部搜索**：通过扩展相关实体的邻居和关联概念来进行具体实体的推理。
  - **DRIFT 搜索**：结合局部搜索和社区信息，提供更准确和相关的答案。
- **图机器学习**：集成了图机器学习技术，提升查询响应质量，并提供来自结构化和非结构化数据的深度洞察。
- **Prompt 调优**：提供调优工具，帮助根据特定数据和需求调整查询提示，从而提高结果质量。

### 3. GraphRAG运行流程

#### 3.1 **索引（Indexing）过程**

1. **文本单元切分**：将输入文本分割成 **TextUnits**，每个 TextUnit 是一个可分析的单元，用于提取关键信息。
2. **实体和关系提取**：使用 LLM 从 TextUnits 中提取实体、关系和关键声明。
3. **图构建**：构建知识图谱，使用 Leiden 算法进行实体的层次聚类。每个实体用节点表示，节点的大小和颜色分别代表实体的度数和所属社区。
4. **社区总结**：从下到上生成每个社区及其成员的总结，帮助全局理解数据集。

#### 3.2 **查询（Query）过程**      

 索引完成后，用户可以通过不同的搜索模式进行查询：

- **全局搜索**：当我们想了解整个语料库或数据集的整体概况时，GraphRAG 可以利用 社区总结 来快速推理和获取信息。这种方式适用于大范围问题，如某个主题的总体理解。
- **局部搜索**：如果问题关注于某个特定的实体，GraphRAG 会向该实体的 邻居（即相关实体）扩展搜索，以获得更详细和精准的答案。
- **DRIFT 搜索**：这是对局部搜索的增强，除了获取邻居和相关概念，还引入了 社区信息 的上下文，从而提供更深入的推理和连接。

#### 3.3 **Prompt 调优**        

为了获得最佳性能，GraphRAG 强烈建议进行 **Prompt 调优**，确保模型可以根据你的特定数据和查询需求进行优化，从而提供更准确和相关的答案。

#### 3.4 GraphRAG计算流程极简示例

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/GraphRAG%E5%AF%BC%E5%9B%BE.png" alt="GraphRAG导图" style="zoom:33%;" />

### 4.GraphRAG安装与Indexing&Query流程实现

注意，以下内容在Jupyter中通过代码完成，扫码即可领取课件代码。

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250320174353383.png" alt="image-20250320174353383" style="zoom:37%;" />

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/202503201126698.png" alt="539f63f72884f3656e6b3ca0f744950" style="zoom: 25%;" />

### 5.GraphRAG API使用方法

![1742464833834](https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/1742464833834.jpg)

## 三、MCP+GraphRAG搭建检索增强智能体

​	接下来即可根据GraphRAG API的调用方法，来创建一个基于GraphRAG的MCP智能体服务器，并尝试在本地client对其进行调用。

### 1.MCP+GraphRAG项目环境搭建

#### 1.1 创建 MCP 客户端项目

```bash
# 创建项目目录
uv init mcp-graphrag
cd mcp-graphrag
```

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250320180427660.png" alt="image-20250320180427660" style="zoom:50%;" />

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250320180441881.png" alt="image-20250320180441881" style="zoom: 50%;" />

#### 1.2 创建MCP客户端虚拟环境

```bash
# 创建虚拟环境
uv venv

# 激活虚拟环境
source .venv/bin/activate
```

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/202503171509604.png" alt="image-20250317150947534" style="zoom:50%;" />

这里需要注意的是，相比pip，uv会自动识别当前项目主目录并创建虚拟环境。

然后即可通过add方法在虚拟环境中安装相关的库。

```bash
# 安装 MCP SDK
uv add mcp graphrag pathlib pandas
```

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250319203936669.png" alt="image-20250319203936669" style="zoom:50%;" />

#### 1.3 创建GraphRAG并构建索引（Index）

- 创建项目目录并进行初始化

```bash
mkdir -p ./graphrag/input
graphrag init --root ./graphrag
```

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250319222103544.png" alt="image-20250319222103544" style="zoom:33%;" />

- 修改配置文件

打开.env文件，填写DeepSeek API-KEY或OpenAI API-Key

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250319205455014.png" alt="image-20250319205455014" style="zoom:30%;" />

打开setting.yaml文件，填写模型名称和代理地址：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250320175421785.png" alt="image-20250320175421785" style="zoom:33%;" />

- 上传文本数据

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250320182131832.png" alt="image-20250320182131832" style="zoom:33%;" />

- index过程

```bash
graphrag index --root ./graphrag
```

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250319222646991.png" alt="image-20250319222646991" style="zoom:50%;" />

### 2.创建GraphRAG服务器Server

​	这里需要注意，当前创建的GraphRAG Server只负责进行对某一个完成Index的知识库进行Query，更加复杂的如文件管理、实时增加检索、多文件库检索等，详见2025大模型Agent智能体开发实战》（春季班）https://whakv.xetslk.com/s/pxKHG内容介绍。

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/d0c81dfe43a1becced8c07db33c3a787_.jpg" alt="d0c81dfe43a1becced8c07db33c3a787_" style="zoom:12%;" />

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250320180856530.png" alt="image-20250320180856530" style="zoom: 50%;" />

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/a6edbd7d658518f05cf04d82b1e3b1a.jpg" alt="a6edbd7d658518f05cf04d82b1e3b1a" style="zoom:50%;" />

这里我们在当前项目中创建一个名为rag_server.py的server，

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250320181000546.png" alt="image-20250320181000546" style="zoom: 50%;" />

并写入如下代码：

```python
from pathlib import Path
from pprint import pprint

import pandas as pd

import graphrag.api as api
from graphrag.config.load_config import load_config
from graphrag.index.typing.pipeline_run_result import PipelineRunResult

from typing import Any
from mcp.server.fastmcp import FastMCP

# 初始化 MCP 服务器
mcp = FastMCP("rag_ML")
USER_AGENT = "rag_ML-app/1.0"

@mcp.tool()
async def rag_ML(query: str) -> str:
    """
    用于查询机器学习决策树相关信息。
    :param query: 用户提出的具体问题
    :return: 最终获得的答案
    """
    PROJECT_DIRECTORY = "/root/autodl-tmp/MCP/mcp-graphrag/graphrag"
    graphrag_config = load_config(Path(PROJECT_DIRECTORY))
    
    # 加载实体
    entities = pd.read_parquet(f"{PROJECT_DIRECTORY}/output/entities.parquet")
    # 加载社区
    communities = pd.read_parquet(f"{PROJECT_DIRECTORY}/output/communities.parquet")
    # 加载社区报告
    community_reports = pd.read_parquet(
        f"{PROJECT_DIRECTORY}/output/community_reports.parquet"
    )
    # 进行全局搜索
    response, context = await api.global_search(
        config=graphrag_config,
        entities=entities,
        communities=communities,
        community_reports=community_reports,
        community_level=2,
        dynamic_community_selection=False,
        response_type="Multiple Paragraphs",
        query=query,
    )
    
    return response

if __name__ == "__main__":
    # 以标准 I/O 方式运行 MCP 服务器
    mcp.run(transport='stdio')
```

**代码解释如下：**

1. **导入必要的模块和库：**

   - `Path` 和 `pprint`：用于路径操作和美化打印输出。
   - `pandas`：用于数据处理，特别是读取 Parquet 格式的数据文件。
   - `graphrag.api` 和相关配置模块：用于加载配置和调用 GraphRAG 的 API。
   - `FastMCP`：MCP 协议的快速实现，用于创建 MCP 服务器。

2. **初始化 MCP 服务器：**

   - `mcp = FastMCP("rag_ML")`：创建一个名为 `rag_ML` 的 MCP 服务器实例。
   - `USER_AGENT = "rag_ML-app/1.0"`：定义用户代理字符串，可能用于标识客户端应用程序的版本信息。

3. **定义工具函数 `rag_ML`：**

   - 使用装饰器 `@mcp.tool()` 将函数注册为 MCP 工具，使其可被客户端调用。

   - 函数为异步函数，接受一个字符串类型的 `query` 参数，表示用户的查询。

   - 函数内部执行以下操作：

     - 加载 GraphRAG 配置：

       - `PROJECT_DIRECTORY`：定义项目目录路径。
       - `graphrag_config = load_config(Path(PROJECT_DIRECTORY))`：加载 GraphRAG 的配置文件。

     - 加载数据文件：

       - 使用 `pandas` 的 `read_parquet` 方法分别加载实体、社区和社区报告的 Parquet 文件。

     - 调用 

       ```
       api.global_search
       ```

        方法进行全局搜索：

       - 传入配置、实体、社区和社区报告等参数。
       - 设置 `community_level=2` 和 `dynamic_community_selection=False`，用于控制社区层级和是否动态选择社区。
       - 设置 `response_type="Multiple Paragraphs"`，指定响应类型为多段落文本。

     - 返回搜索结果 `response`。

4. **运行 MCP 服务器：**

   - 在主程序中，调用 `mcp.run(transport='stdio')` 以标准输入输出（`stdio`）的方式运行 MCP 服务器，使其能够接收和响应客户端的请求。

> MCP入门实战教程详见：
>
> <img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/202503201126698.png" alt="539f63f72884f3656e6b3ca0f744950" style="zoom: 25%;" />

### 3.创建GraphRAG服务器client

接下来继续创建客户端，在项目主目录下创建一个名为`client.py`的客户端，

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250320181523870.png" alt="image-20250320181523870" style="zoom: 50%;" />

并写入如下代码：

```python
import asyncio
import os
import json
from typing import Optional
from contextlib import AsyncExitStack

from openai import OpenAI  
from dotenv import load_dotenv

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

# 加载 .env 文件，确保 API Key 受到保护
load_dotenv()

class MCPClient:
    def __init__(self):
        """初始化 MCP 客户端"""
        self.exit_stack = AsyncExitStack()
        self.openai_api_key = os.getenv("OPENAI_API_KEY")  # 读取 OpenAI API Key
        self.base_url = os.getenv("BASE_URL")  # 读取 BASE YRL
        self.model = os.getenv("MODEL")  # 读取 model
        if not self.openai_api_key:
            raise ValueError("❌ 未找到 OpenAI API Key，请在 .env 文件中设置 OPENAI_API_KEY")
        self.client = OpenAI(api_key=self.openai_api_key, base_url=self.base_url) # 创建OpenAI client
        self.session: Optional[ClientSession] = None   

    async def transform_json(self, json2_data):
        """
        将Claude Function calling参数格式转换为OpenAI Function calling参数格式，多余字段会被直接删除。
        
        :param json2_data: 一个可被解释为列表的 Python 对象（或已解析的 JSON 数据）
        :return: 转换后的新列表
        """
        result = []
        
        for item in json2_data:
            # 确保有 "type" 和 "function" 两个关键字段
            if not isinstance(item, dict) or "type" not in item or "function" not in item:
                continue
        
            old_func = item["function"]
        
            # 确保 function 下有我们需要的关键子字段
            if not isinstance(old_func, dict) or "name" not in old_func or "description" not in old_func:
                continue
        
            # 处理新 function 字段
            new_func = {
                "name": old_func["name"],
                "description": old_func["description"],
                "parameters": {}
            }
        
            # 读取 input_schema 并转成 parameters
            if "input_schema" in old_func and isinstance(old_func["input_schema"], dict):
                old_schema = old_func["input_schema"]
                
                # 新的 parameters 保留 type, properties, required 这三个字段
                new_func["parameters"]["type"] = old_schema.get("type", "object")
                new_func["parameters"]["properties"] = old_schema.get("properties", {})
                new_func["parameters"]["required"] = old_schema.get("required", [])
            
            new_item = {
                "type": item["type"],
                "function": new_func
            }
        
            result.append(new_item)
    
        return result

    async def connect_to_server(self, server_script_path: str):
        """连接到 MCP 服务器并列出可用工具"""
        is_python = server_script_path.endswith('.py')
        is_js = server_script_path.endswith('.js')
        if not (is_python or is_js):
            raise ValueError("服务器脚本必须是 .py 或 .js 文件")

        command = "python" if is_python else "node"
        server_params = StdioServerParameters(
            command=command,
            args=[server_script_path],
            env=None
        )

        # 启动 MCP 服务器并建立通信
        stdio_transport = await self.exit_stack.enter_async_context(stdio_client(server_params))
        self.stdio, self.write = stdio_transport
        self.session = await self.exit_stack.enter_async_context(ClientSession(self.stdio, self.write))

        await self.session.initialize()

        # 列出 MCP 服务器上的工具
        response = await self.session.list_tools()
        tools = response.tools
        print("\n已连接到服务器，支持以下工具:", [tool.name for tool in tools])     
        
    async def process_query(self, query: str) -> str:
        """
        使用大模型处理查询并调用可用的 MCP 工具 (Function Calling)
        """
        messages = [{"role": "user", "content": query}]
        
        response = await self.session.list_tools()
        
        available_tools = [{
            "type": "function",
            "function": {
                "name": tool.name,
                "description": tool.description,
                "input_schema": tool.inputSchema
            }
        } for tool in response.tools]
        # print(available_tools)

        # 进行参数格式转化
        available_tools = await self.transform_json(available_tools)
        
        response = self.client.chat.completions.create(
            model=self.model,            
            messages=messages,
            tools=available_tools     
        )
        
        # 处理返回的内容
        content = response.choices[0]
        if content.finish_reason == "tool_calls":
            # 如何是需要使用工具，就解析工具
            tool_call = content.message.tool_calls[0]
            tool_name = tool_call.function.name
            tool_args = json.loads(tool_call.function.arguments)
            
            # 执行工具
            result = await self.session.call_tool(tool_name, tool_args)
            print(f"\n\n[Calling tool {tool_name} with args {tool_args}]\n\n")
            
            # 将模型返回的调用哪个工具数据和工具执行完成后的数据都存入messages中
            messages.append(content.message.model_dump())
            messages.append({
                "role": "tool",
                "content": result.content[0].text,
                "tool_call_id": tool_call.id,
            })
            
            # 将上面的结果再返回给大模型用于生产最终的结果
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
            )
            return response.choices[0].message.content
            
        return content.message.content
    
    async def chat_loop(self):
        """运行交互式聊天循环"""
        print("\n🤖 MCP 客户端已启动！输入 'quit' 退出")

        while True:
            try:
                query = input("\n你: ").strip()
                if query.lower() == 'quit':
                    break
                
                response = await self.process_query(query)  # 发送用户输入到 OpenAI API
                print(f"\n🤖 OpenAI: {response}")

            except Exception as e:
                print(f"\n⚠️ 发生错误: {str(e)}")

    async def cleanup(self):
        """清理资源"""
        await self.exit_stack.aclose()

async def main():
    if len(sys.argv) < 2:
        print("Usage: python client.py <path_to_server_script>")
        sys.exit(1)

    client = MCPClient()
    try:
        await client.connect_to_server(sys.argv[1])
        await client.chat_loop()
    finally:
        await client.cleanup()

if __name__ == "__main__":
    import sys
    asyncio.run(main())
```

这段代码实现了一个 **MCP 客户端**，用于连接 MCP 服务器，并利用 OpenAI 的 API 进行 Function Calling（函数调用）。该客户端能够与 MCP 服务器交互，列出可用工具，并根据用户输入选择适当的工具调用。

1. **初始化**

- `AsyncExitStack()` 处理多个异步上下文（如 MCP 连接）。
- 读取 .env配置：
  - `OPENAI_API_KEY`
  - `BASE_URL`（可选，用于自定义 API 代理）
  - `MODEL`（指定 OpenAI 使用的模型）
- `self.client = OpenAI(...)` 创建 OpenAI API 客户端。

2. **转换 API 格式 (`transform_json`)**

- OpenAI 和 Claude API 的 Function Calling 格式不同。
- 该函数将 Claude 的 `input_schema` 转换为 OpenAI 兼容格式。

3. **连接 MCP 服务器**

- 连接 MCP 服务器，支持 Python 或 JavaScript 服务器脚本。
- `stdio_client(server_params)` 通过 `stdio` 进行通信。
- `await self.session.list_tools()` 列出 MCP 服务器上可用的工具。

4. **处理用户查询 (`process_query`)**

- 获取 MCP 服务器上可用的工具 (`list_tools`)。
- 让 OpenAI 选择是否需要调用 MCP 服务器上的工具 (`tool_calls`)。
- 若需要工具调用：
  - 解析 `tool_calls`
  - `call_tool(tool_name, tool_args)` 调用 MCP 服务器上的工具
  - 再次向 OpenAI 提交新信息，获取最终答案

5. **交互式聊天 (`chat_loop`)**

- 允许用户输入查询，自动选择 MCP 工具或直接回答。
- 输入 `quit` 退出聊天。

然后创建配置文件.env：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250320182426174.png" alt="image-20250320182426174" style="zoom: 50%;" />

并手动输入

```bash
BASE_URL=
MODEL=
OPENAI_API_KEY=
```

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250320182514475.png" alt="image-20250320182514475" style="zoom:50%;" />

此处可以设置OpenAI、DeepSeek或者任何ollama、vLLM调度的本地模型。具体配置方法参考《MCP入门实战教程》。

> MCP入门实战教程详见：
>
> <img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/202503201126698.png" alt="539f63f72884f3656e6b3ca0f744950" style="zoom: 25%;" />

### 4.MCP+GraphRAG问答测试

#### 4.1 命令行问答

最后即可开始进行问答测试，在命令行中输入如下命令即可启动问答：

```python
uv run client.py rag_server.py
```

问答效果如图所示：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250320183021314.png" alt="image-20250320183021314" style="zoom:50%;" />

#### 4.2 Claude Desktop问答



详见2025大模型Agent智能体开发实战》（春季班）https://whakv.xetslk.com/s/pxKHG内容介绍。

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/d0c81dfe43a1becced8c07db33c3a787_.jpg" alt="d0c81dfe43a1becced8c07db33c3a787_" style="zoom:12%;" />

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250320180856530.png" alt="image-20250320180856530" style="zoom: 50%;" />

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250320183236028.png" alt="image-20250320183236028" style="zoom: 50%;" />

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250320183157454.png" alt="image-20250320183157454" style="zoom:50%;" />

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/a6edbd7d658518f05cf04d82b1e3b1a.jpg" style="zoom:50%;" />

---

## 四、MCP智能体开发基础理论入门

### 1. 真实世界的复杂智能体开发项目

#### 1.1 2023年MateGen 1.0代码结构图

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/202310292019679.png" alt="Code AI Agent架构图" style="zoom:90%;" />

#### 1.2 2025大模型Agent开发实战付费课程企业问答智能体项目流程图

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250320183806729.png" alt="image-20250320183806729" style="zoom:50%;" />

#### 1.3 2025大模型Agent开发实战付费课程智能客服项目流程图

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250320183753223.png" alt="image-20250320183753223" style="zoom:50%;" />

#### 1.4 2025大模型Agent开发实战付费课程智能市场分析项目流程图

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250320183902790.png" alt="image-20250320183902790" style="zoom:50%;" />

#### 1.5 2025大模型Agent开发实战付费课程MateGen 2.0项目架构

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250320184004758.png" alt="image-20250320184004758" style="zoom:50%;" />

详见2025大模型Agent智能体开发实战》（春季班）https://whakv.xetslk.com/s/pxKHG内容介绍。

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/d0c81dfe43a1becced8c07db33c3a787_.jpg" alt="d0c81dfe43a1becced8c07db33c3a787_" style="zoom:12%;" />

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/a6edbd7d658518f05cf04d82b1e3b1a.jpg" alt="a6edbd7d658518f05cf04d82b1e3b1a" style="zoom:50%;" />

### 2. 智能体开发框架选型

12项Agent智能体开发框架入门与选型！https://www.bilibili.com/video/BV16NBJYRE3s/

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250320184124671.png" alt="image-20250320184124671" style="zoom:50%;" />

### 3. 从零快速了解智能体开发

​	在使用 LLM 构建应用时，我们建议**尽可能选择最简单的解决方案**，只有在**确实需要**时才增加复杂性。这意味着，在某些情况下，可能根本**不需要构建代理系统**。

​	**代理系统（Agentic Systems）\**通常会\**牺牲响应速度（latency）和成本（cost）**，以换取更好的任务执行能力。因此，在使用代理之前，你需要考虑这种**权衡是否合理**。

当应用场景**需要更复杂的逻辑**时：

- **工作流（Workflows）** 提供了**可预测性**和**一致性**，适用于**任务流程清晰的情况**。
- **代理（Agents）** 更适用于**需要灵活性和大规模模型驱动决策**的场景。

然而，对于许多应用来说，**优化单次 LLM 调用**（例如结合**检索增强（RAG）\**和\**上下文示例（in-context examples）**）通常已经足够，无需使用复杂的代理系统。

​	分发模式：将任务分发（Fan-out）给多个子代理（sub-agents），然后汇总（Fan-in）结果。每个子任务都是一个 **AugmentedLLM**，整个 **Parallel** 工作流本身也是如此，这意味着每个子任务可以选择性地成为一个更复杂的工作流。

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250320184519636.png" alt="image-20250320184519636" style="zoom:50%;" />

​	路由模式：**对于给定的输入，系统会将其路由（分配）到最相关的 `top_k` 个类别。**
 其中，每个类别（category）可以是：

1. **Agent**（智能代理）：可能是一个 AI 代理（如 LLM 驱动的任务处理单元）。
2. **MCP 服务器**（MCP Server）：可以是基于 **Model Context Protocol (MCP)** 的服务器，用于处理特定任务或提供外部数据支持。
3. **常规函数**（Regular Function）：即普通的代码函数，可能是执行计算、数据处理等任务的函数。

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250320184527687.png" alt="image-20250320184527687" style="zoom: 50%;" />

​	编排模式：**一个更高层次的 LLM（大语言模型）负责生成任务计划（plan），然后将各个子任务分配给子代理（sub-agents），并最终整合（synthesize）这些子任务的结果。**

其中：

- **高层 LLM 生成计划**：这个 LLM 充当“指挥官”，根据输入任务制定执行步骤。
- **子代理（sub-agents）执行任务**：每个子任务被分配给不同的子代理，可能是不同的 AI 组件、MCP 服务器或特定函数。
- **整合（synthesize）结果**：在所有子任务执行完毕后，系统会将它们的结果合并，生成最终输出。

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250320184628739.png" alt="image-20250320184628739" style="zoom: 50%;" />

​	优化器模式：**一个 LLM 充当“优化器”（optimizer），不断优化回答；另一个 LLM 充当“评估者”（evaluator），对回答进行批判性评估，直到回答达到质量标准。**

**具体流程**

1. 优化器（optimizer）
   - 生成初步的回答，并在每轮迭代中不断优化它，使其更准确、更符合要求。
2. 评估者（evaluator）
   - 对优化器生成的回答进行**审查和批评**，指出其中的问题（如逻辑错误、信息缺失、语义不清等）。
   - 如果回答未达到质量标准，它会要求优化器进行修改和改进。
3. 循环优化
   - 这个过程会**反复进行**，直到评估者认可答案的质量（即超过某个质量标准）。

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250320184758415.png" alt="image-20250320184758415" style="zoom:50%;" />

接下来我们尝试借助MCP，实现分发模式和路由模式，并据此搭建一个NL2SQL+NL2Python的初级数据分析智能体。

## 五、OpenAI风格API Function calling进阶功能介绍

本部分内容需参考以下Jupyer部分代码进行学习。

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250320191058921.png" alt="image-20250320191058921" style="zoom:50%;" />

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250320191119828.png" alt="image-20250320191119828" style="zoom:50%;" />

## 六、借助MCP搭建AI数据分析智能体

​	在了解了Function calling的进阶功能外，接下来我们继续介绍如何基于上述功能，来进行MCP智能体快速发开发，来搭建一个能够进行SQL查询和Python自动编写的入门级数据分析智能体。

### 1. miniMateGen项目初始化

```bash
cd /root/autodl-tmp/MCP
# 创建项目目录
uv init miniMateGen
cd miniMateGen
```

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/202503201125366.png" alt="image-20250320112530253" style="zoom:50%;" />

```bash
# 创建虚拟环境
uv venv

# 激活虚拟环境
source .venv/bin/activate
```

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/202503201125651.png" alt="image-20250320112559581" style="zoom:50%;" />

创建项目如下：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250320191417271.png" alt="image-20250320191417271" style="zoom: 50%;" />

### 2. 创建MCP服务器一：SQL_server

#### 2.1 Linux环境下安装MySQL服务器并创建简单数据集

- 创建MySQL数据库

```bash
apt install mysql-server
```

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250214175933719.png" alt="image-20250214175933719" style="zoom:50%;" />

然后启动mysql，并设置初始密码：

```bash
mysqld &
mysql
```

进入到SQL命令行后，输入如下命令：

```sql
ALTER USER 'root'@'localhost' IDENTIFIED BY '123';
```

> 此处密码可根据实际需求设置。

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250214181533818.png" alt="image-20250214181533818" style="zoom:50%;" />

然后输入`exit;`即可退出。

然后再次进入MySQL，并根据要求输入密码：

```bash
mysql -u root -p
```

然后创建一个数据库：

```sql
CREATE DATABASE school;
USE school;
```

然后创建一个虚拟表格，里面包含了10位同学各自3门课程的分数：

```sql
CREATE TABLE students_scores (
    id INT AUTO_INCREMENT PRIMARY KEY,  
    name VARCHAR(50),                   
    course1 INT,                        
    course2 INT,                       
    course3 INT                        
);
```

```sql
INSERT INTO students_scores (name, course1, course2, course3)
VALUES
    ('学生1', 85, 92, 78),
    ('学生2', 76, 88, 91),
    ('学生3', 90, 85, 80),
    ('学生4', 65, 70, 72),
    ('学生5', 82, 89, 95),
    ('学生6', 91, 93, 87),
    ('学生7', 77, 78, 85),
    ('学生8', 88, 92, 91),
    ('学生9', 84, 76, 80),
    ('学生10', 89, 90, 92);
```

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250214182224214.png" alt="image-20250214182224214" style="zoom:50%;" />

然后即可查看数据集基本情况：

```sql
SELECT * FROM students_scores;
```

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250214182305761.png" alt="image-20250214182305761" style="zoom:50%;" />

此外，还需要刷新身份验证，使得其他库（如pymysql）可以通过密码验证登录：

```SQL
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '123';
```

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250214183946616.png" alt="image-20250214183946616" style="zoom:50%;" />

#### 2.2 编写SQL_server.py代码

- 功能示意图

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250320192252182.png" alt="image-20250320192252182" style="zoom:50%;" />

- 代码位置

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250320192327617.png" style="zoom:50%;" />

需要增加额外依赖：

```bash
uv add pymysql numpy pandas
```

代码内容如下：

```python
import json
import httpx
from typing import Any
import pymysql
import csv
from mcp.server.fastmcp import FastMCP

# 初始化 MCP 服务器
mcp = FastMCP("SQLServer")
USER_AGENT = "SQLserver-app/1.0"

@mcp.tool()
async def sql_inter(sql_query):
    """
    查询本地MySQL数据库，通过运行一段SQL代码来进行数据库查询。\
    :param sql_query: 字符串形式的SQL查询语句，用于执行对MySQL中school数据库中各张表进行查询，并获得各表中的各类相关信息
    :return：sql_query在MySQL中的运行结果。
    """
    
    connection = pymysql.connect(
            host='localhost',  # 数据库地址
            user='root',  # 数据库用户名
            passwd='123',  # 数据库密码
            db='school',  # 数据库名
            charset='utf8'  # 字符集选择utf8
        )
    
    try:
        with connection.cursor() as cursor:
            # SQL查询语句
            sql = sql_query
            cursor.execute(sql)

            # 获取查询结果
            results = cursor.fetchall()

    finally:
        connection.close()
    
    
    return json.dumps(results)

@mcp.tool()
async def export_table_to_csv(table_name, output_file):
    """
    将 MySQL 数据库中的某个表导出为 CSV 文件。
    
    :param table_name: 需要导出的表名
    :param output_file: 输出的 CSV 文件路径
    """
    # 连接 MySQL 数据库
    connection = pymysql.connect(
        host='localhost',  # 数据库地址
        user='root',  # 数据库用户名
        passwd='123',  # 数据库密码
        db='school',  # 数据库名
        charset='utf8'  # 字符集
    )

    try:
        with connection.cursor() as cursor:
            # 查询数据表的所有数据
            query = f"SELECT * FROM {table_name};"
            cursor.execute(query)

            # 获取所有列名
            column_names = [desc[0] for desc in cursor.description]

            # 获取查询结果
            rows = cursor.fetchall()

            # 将数据写入 CSV 文件
            with open(output_file, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                
                # 写入表头
                writer.writerow(column_names)
                
                # 写入数据
                writer.writerows(rows)

            print(f"数据表 {table_name} 已成功导出至 {output_file}")

    except Exception as e:
        print(f"导出失败: {e}")

    finally:
        connection.close()

if __name__ == "__main__":
    # 以标准 I/O 方式运行 MCP 服务器
    mcp.run(transport='stdio')
```

**代码详细解释**

这段代码是一个 **MCP 服务器（Model Context Protocol Server）**，它提供了两个主要功能：

1. **查询 MySQL 数据库（`sql_inter`）**：允许用户输入 SQL 查询，并获取 MySQL 数据库的查询结果。
2. **将数据库表导出为 CSV 文件（`export_table_to_csv`）**：把 MySQL 数据库中的某个表转换为 CSV 文件并保存到本地。

此外，整个 MCP 服务器是基于 `FastMCP` 运行的，允许其他系统或用户通过 MCP 协议调用这些工具。

其中两个核心函数解释如下

**(1) `sql_inter(sql_query)`：查询 MySQL 数据库**

**功能**

- 该函数**接收一条 SQL 查询语句**，并在 MySQL 数据库 `school` 中执行查询。
- 通过 `pymysql.connect()` 连接本地 MySQL 服务器（用户名 `root`，密码 `123`）。
- 使用 `cursor.execute(sql_query)` 执行 SQL 语句，并使用 `fetchall()` 获取所有查询结果。
- 结果最终**转换为 JSON 格式返回**。

**(2) `export_table_to_csv(table_name, output_file)`：导出表为 CSV**

**功能**

- 该函数**导出 MySQL 数据表为 CSV 文件**。
- 连接 MySQL 服务器并执行 `SELECT * FROM table_name;` 查询**获取表数据**。
- **提取表头（列名）**，并将其与查询结果一起**写入 CSV 文件**。
- **打印导出成功消息** 或 **错误信息**。

| **功能**                    | **作用**                                     |
| --------------------------- | -------------------------------------------- |
| **MCP 服务器** (`FastMCP`)  | 允许 MCP 客户端调用 SQL 查询和数据导出功能。 |
| **`sql_inter()`**           | 执行 SQL 语句并返回 JSON 结果。              |
| **`export_table_to_csv()`** | 导出 MySQL 数据表为 CSV 文件。               |
| **`mcp.run()`**             | 启动 MCP 服务器，监听客户端请求。            |

### 3. 创建MCP服务器二：Python_server

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250320192905560.png" alt="image-20250320192905560" style="zoom:50%;" />

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250320192930353.png" alt="image-20250320192930353" style="zoom:50%;" />

```python
import json
from typing import Any
import csv
import numpy as np
import pandas as pd
import random
from mcp.server.fastmcp import FastMCP

# 初始化 MCP 服务器
mcp = FastMCP("PythonServer")
USER_AGENT = "Pythonserver-app/1.0"

@mcp.tool()
async def python_inter(py_code):
    """
    运行用户提供的 Python 代码，并返回执行结果。
    
    :param py_code: 字符串形式的 Python 代码
    :return: 代码运行的最终结果
    """
    g = globals()
    
    try:
        # 若是表达式，直接运行并返回
        result = eval(py_code, g)
        return json.dumps(str(result), ensure_ascii=False)
    
    except Exception:
        global_vars_before = set(g.keys())
        try:
            exec(py_code, g)
        except Exception as e:
            return json.dumps(f"代码执行时报错: {e}", ensure_ascii=False)

        global_vars_after = set(g.keys())
        new_vars = global_vars_after - global_vars_before

        if new_vars:
            # 只返回可序列化的变量值
            safe_result = {}
            for var in new_vars:
                try:
                    json.dumps(g[var])  # 尝试序列化，确保可以转换为 JSON
                    safe_result[var] = g[var]
                except (TypeError, OverflowError):
                    safe_result[var] = str(g[var])  # 如果不能序列化，则转换为字符串

            return json.dumps(safe_result, ensure_ascii=False)
        
        else:
            return json.dumps("已经顺利执行代码", ensure_ascii=False)

if __name__ == "__main__":
    # 以标准 I/O 方式运行 MCP 服务器
    mcp.run(transport='stdio')
```

这段代码实现了一个 **MCP 服务器**，它允许 **远程执行 Python 代码**，并返回执行结果。

**代码执行逻辑如下**

**(a) `eval()` 处理单行 Python 表达式**

```python
try:
    result = eval(py_code, g)
    return json.dumps(str(result), ensure_ascii=False)
```

- **如果 `py_code` 是一个简单表达式**（如 `"1 + 1"` 或 `"max([3,5,7])"`），则直接用 `eval()` 计算并返回结果。

- 示例

  ```python
  python_inter("3 + 4")
  ```

  返回

  ```json
  "7"
  ```

**(b) `exec()` 处理完整的 Python 代码**

如果 `eval()` **执行失败**（意味着输入是代码块而不是单个表达式），那么：

```python
global_vars_before = set(g.keys())  # 记录执行前的全局变量
try:
    exec(py_code, g)  # 运行 Python 代码
except Exception as e:
    return json.dumps(f"代码执行时报错: {e}", ensure_ascii=False)
```

- **使用 `exec()` 执行完整的 Python 代码**（如定义变量、循环、函数）。
- **如果 `exec()` 发生错误，则返回错误信息**。

**(c) 提取新创建的变量**

```python
global_vars_after = set(g.keys())  # 记录执行后的全局变量
new_vars = global_vars_after - global_vars_before  # 找出新创建的变量

if new_vars:
    safe_result = {}
    for var in new_vars:
        try:
            json.dumps(g[var])  # 尝试序列化
            safe_result[var] = g[var]
        except (TypeError, OverflowError):
            safe_result[var] = str(g[var])  # 不能序列化的变量转换为字符串

    return json.dumps(safe_result, ensure_ascii=False)
```

- **检查 `exec()` 运行后新增的变量**，只返回**可序列化**的变量。

- 示例

  ```python
  python_inter("a = 10\nb = 20\nc = a + b")
  ```

  返回

  ```json
  {
      "a": 10,
      "b": 20,
      "c": 30
  }
  ```

- **如果代码运行后没有新变量，只返回 `已顺利执行代码`**。

代码总结：

| **功能**                   | **作用**                         |
| -------------------------- | -------------------------------- |
| **MCP 服务器** (`FastMCP`) | 允许远程执行 Python 代码         |
| **`python_inter()`**       | 运行 Python 代码，返回 JSON 结果 |
| **支持 `eval()`**          | 计算简单 Python 表达式           |
| **支持 `exec()`**          | 运行完整 Python 代码             |
| **代码安全检查**           | 仅返回可序列化变量               |

### 4.创建MCP客户端Client

接下来考虑创建客户端Client，此时客户端需要满足以下几点要求：

1. 同时连接多个服务器上的若干个工具；
2. 需要能够同时完成串联或者并联模式；
3. 需要能够支持多轮对话。

据此设计架构如下所示：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250320195529610.png" alt="image-20250320195529610" style="zoom:50%;" />

代码位置：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250320195620652.png" alt="image-20250320195620652" style="zoom:50%;" />

完整代码内容如下：

```python
import asyncio
import os
import json
from typing import Optional, Dict
from contextlib import AsyncExitStack

from openai import OpenAI
from dotenv import load_dotenv

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

load_dotenv()

class MultiServerMCPClient:
    def __init__(self):
        """管理多个 MCP 服务器的客户端"""
        self.exit_stack = AsyncExitStack()
        self.openai_api_key = os.getenv("OPENAI_API_KEY")  
        self.base_url = os.getenv("BASE_URL")  
        self.model = os.getenv("MODEL")  
        if not self.openai_api_key:
            raise ValueError("❌ 未找到 OPENAI_API_KEY，请在 .env 文件中配置")

        # 初始化 OpenAI Client
        self.client = OpenAI(api_key=self.openai_api_key, base_url=self.base_url)
        
        # 存储 (server_name -> MCP ClientSession) 映射
        self.sessions: Dict[str, ClientSession] = {}
        # 存储工具信息
        self.tools_by_session: Dict[str, list] = {}  # 每个 session 的 tools 列表
        self.all_tools = []  # 合并所有工具的列表

    async def connect_to_servers(self, servers: dict):
        """
        同时启动多个服务器并获取工具
        servers: 形如 {"weather": "weather_server.py", "rag": "rag_server.py"}
        """
        for server_name, script_path in servers.items():
            session = await self._start_one_server(script_path)
            self.sessions[server_name] = session
            
            # 列出此服务器的工具
            resp = await session.list_tools()
            self.tools_by_session[server_name] = resp.tools  # 保存到 self.tools_by_session

            for tool in resp.tools:
                # OpenAI Function Calling 格式修正
                function_name = f"{server_name}_{tool.name}"
                # print(tool.name)
                self.all_tools.append({
                    "type": "function",
                    "function": {
                        "name": function_name,
                        "description": tool.description,
                        "input_schema": tool.inputSchema
                    }
                })
         
        
        # 转化function calling格式
        self.all_tools = await self.transform_json(self.all_tools)
        # print(self.all_tools)

        print("\n✅ 已连接到下列服务器:")
        for name in servers:
            print(f"  - {name}: {servers[name]}")
        print("\n汇总的工具:")
        
        for t in self.all_tools:
            print(f"  - {t['function']['name']}")

    async def transform_json(self, json2_data):
        """
        将类似 json2 的格式转换为类似 json1 的格式，多余字段会被直接删除。
        
        :param json2_data: 一个可被解释为列表的 Python 对象（或已解析的 JSON 数据）
        :return: 转换后的新列表
        """
        result = []
        
        for item in json2_data:
            # 确保有 "type" 和 "function" 两个关键字段
            if not isinstance(item, dict) or "type" not in item or "function" not in item:
                continue
        
            old_func = item["function"]
        
            # 确保 function 下有我们需要的关键子字段
            if not isinstance(old_func, dict) or "name" not in old_func or "description" not in old_func:
                continue
        
            # 处理新 function 字段
            new_func = {
                "name": old_func["name"],
                "description": old_func["description"],
                "parameters": {}
            }
        
            # 读取 input_schema 并转成 parameters
            if "input_schema" in old_func and isinstance(old_func["input_schema"], dict):
                old_schema = old_func["input_schema"]
                
                # 新的 parameters 保留 type, properties, required 这三个字段
                new_func["parameters"]["type"] = old_schema.get("type", "object")
                new_func["parameters"]["properties"] = old_schema.get("properties", {})
                new_func["parameters"]["required"] = old_schema.get("required", [])
            
            new_item = {
                "type": item["type"],
                "function": new_func
            }
        
            result.append(new_item)
    
        return result            

    async def _start_one_server(self, script_path: str) -> ClientSession:
        """启动单个 MCP 服务器子进程，并返回 ClientSession"""
        is_python = script_path.endswith(".py")
        is_js = script_path.endswith(".js")
        if not (is_python or is_js):
            raise ValueError("服务器脚本必须是 .py 或 .js 文件")

        command = "python" if is_python else "node"
        server_params = StdioServerParameters(
            command=command,
            args=[script_path],
            env=None
        )
        stdio_transport = await self.exit_stack.enter_async_context(stdio_client(server_params))
        read_stream, write_stream = stdio_transport
        session = await self.exit_stack.enter_async_context(ClientSession(read_stream, write_stream))
        await session.initialize()
        return session


    async def chat_base(self, messages: list) -> list:
    
        # messages = [{"role": "user", "content": query}]
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            tools=self.all_tools
        )
        if response.choices[0].finish_reason == "tool_calls":
            while True:
                messages = await self.create_function_response_messages(messages, response)
                response = self.client.chat.completions.create(
                    model=self.model,
                    messages=messages,
                    tools=self.all_tools
                )
                if response.choices[0].finish_reason != "tool_calls":
                    break
                    
        # return response.choices[0].message.content
        return response
        
    async def create_function_response_messages(self, messages, response):
        function_call_messages = response.choices[0].message.tool_calls
        messages.append(response.choices[0].message.model_dump())
        
        for function_call_message in function_call_messages:
            tool_name = function_call_message.function.name
            tool_args = json.loads(function_call_message.function.arguments)
        
            # 运行外部函数
            function_response = await self._call_mcp_tool(tool_name, tool_args)

            # 拼接消息队列
            messages.append(
                {
                    "role": "tool",
                    "content": function_response,
                    "tool_call_id": function_call_message.id,
                }
            )
        return messages  

    async def process_query(self, user_query: str) -> str:
        """
        OpenAI 最新 Function Calling 逻辑:
         1. 发送用户消息 + tools 信息
         2. 若模型 `finish_reason == "tool_calls"`，则解析 toolCalls 并执行相应 MCP 工具
         3. 把调用结果返回给 OpenAI，让模型生成最终回答
        """
        messages = [{"role": "user", "content": user_query}]

        # 第一次请求
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            tools=self.all_tools
        )
        content = response.choices[0]
        print(content)
        print(self.all_tools)

        # 如果模型调用了 MCP 工具
        if content.finish_reason == "tool_calls":
            # 解析 tool_calls
            tool_call = content.message.tool_calls[0]
            tool_name = tool_call.function.name  # 形如 "weather_query_weather"
            tool_args = json.loads(tool_call.function.arguments)

            print(f"\n[ 调用工具: {tool_name}, 参数: {tool_args} ]\n")

            # 执行MCP工具
            result = await self._call_mcp_tool(tool_name, tool_args)

            # 把工具调用历史写进 messages
            messages.append(content.message.model_dump())
            messages.append({
                "role": "tool",
                "content": result,
                "tool_call_id": tool_call.id,
            })
            # 第二次请求，让模型整合工具结果，生成最终回答
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages
            )
            return response.choices[0].message.content

        # 如果模型没调用工具，直接返回回答
        return content.message.content

    async def _call_mcp_tool(self, tool_full_name: str, tool_args: dict) -> str:
        """
        根据 "serverName_toolName" 调用相应的服务器工具
        """
        parts = tool_full_name.split("_", 1)  # 拆分 "weather_query_weather" -> ["weather", "query_weather"]
        if len(parts) != 2:
            return f"无效的工具名称: {tool_full_name}"

        server_name, tool_name = parts
        session = self.sessions.get(server_name)
        if not session:
            return f"找不到服务器: {server_name}"
        
        # 执行 MCP 工具
        resp = await session.call_tool(tool_name, tool_args)
        print(resp)
        return resp.content if resp.content else "工具执行无输出"

    async def chat_loop(self):
        print("\n🤖 多服务器 MCP + 最新 Function Calling 客户端已启动！输入 'quit' 退出。")
        messages = []

        while True:
            query = input("\n你: ").strip()
            if query.lower() == "quit":
                break
            try:
                messages.append({"role": "user", "content": query})
                messages = messages[-20: ]
                # print(messages)
                response = await self.chat_base(messages)
                messages.append(response.choices[0].message.model_dump())
                result = response.choices[0].message.content
                
                print(f"\nAI: {result}")
            except Exception as e:
                print(f"\n⚠️  调用过程出错: {e}")

    async def cleanup(self):
        # 关闭所有资源
        await self.exit_stack.aclose()

async def main():
    # 服务器脚本
    servers = {
        "write": "write_server.py",
        "weather": "weather_server.py",
        "SQLServer":"SQL_server.py",
        "PythonServer":"Python_server.py"
    }

    client = MultiServerMCPClient()
    try:
        await client.connect_to_servers(servers)
        await client.chat_loop()
    finally:
        await client.cleanup()

if __name__ == "__main__":
    asyncio.run(main())
```

代码解释如下：



### 5.miniMateGen功能测试

接下来即可启动MCP客户端：

```bash
source .venv/bin/activate
uv run client.py
```

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250320200153992.png" alt="image-20250320200153992" style="zoom:50%;" />

此时项目内拷贝了weather_server.py（天气查询客户端），因此可以先测试function calling并行能否顺利运行：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/6b7a027acfad3957ec9ea25a23fbe7d.png" alt="6b7a027acfad3957ec9ea25a23fbe7d" style="zoom:50%;" />

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250320184519636.png" alt="image-20250320184519636" style="zoom:50%;" />
以及Function calling串联能否运行：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250320200249903.png" alt="image-20250320200249903" style="zoom:50%;" />

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250320184527687.png" alt="image-20250320184527687" style="zoom: 50%;" />

#### 5.1 NL2SQL功能测试

`请帮我查询数据库中总共包含几张表？`

`这张表中总共有几条数据？`

`请帮我将这张表导出到本地`

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/7da9cfc1dc299abd4dc5af53eab2ba8.png" alt="7da9cfc1dc299abd4dc5af53eab2ba8" style="zoom:50%;" />

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/5cf72a2b9cb63872b20db61ae652d6b.png" alt="5cf72a2b9cb63872b20db61ae652d6b" style="zoom:50%;" />

#### 5.2 NL2Python功能测试

`你好，请帮我编写并运行一段Python代码，来创建一个10位的随机数`

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250320200454658.png" alt="image-20250320200454658" style="zoom:50%;" />

#### 5.3 NL2SQL+NL2Python功能联动测试

`请帮我运行Python代码来读取本地students_scores.csv文件，并打印第一行数据`

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/949b23bfe0808aa89f2178ae395d697.png" alt="949b23bfe0808aa89f2178ae395d697" style="zoom:50%;" />

`好的，接下来我想要查看这张表的全部信息，请帮我打印这张表`

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/279c9c33b130c754e24eb34d528d890.png" alt="279c9c33b130c754e24eb34d528d890" style="zoom:50%;" />

`请帮我计算这张表中全部学生三门学科的平均分数`

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/4d2ec74e710091af9fb14397027851a.png" alt="4d2ec74e710091af9fb14397027851a" style="zoom: 50%;" />

# 从零到一MCP开发与部署实战

[toc]

- 公开课代码领取

  <img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/0202fa8f35ef772a657853eaf4ad58f.png" alt="0202fa8f35ef772a657853eaf4ad58f" style="zoom:50%;" />

## 一、MCP技术入门介绍

### 1.智能体开发核心技术—MCP

#### 1.1 **Function calling技术回顾**

​	如何快速开发一款智能体应用，最关键的技术难点就在于如何让大模型高效稳定的接入一些外部工具。而在MCP技术诞生之前，最主流的方法，是借助Function calling技术来打通大模型和外部工具之间的联系，换而言之，也就是借助Function calling，来让大模型灵活的调用外部工具。

​	例如一个典型的Function calling示例，我们希望让大模型能够调用一些天气API查询即时天气，此时我们就需要创建一个查询天气的外部函数，负责调用天气API来查询天气，同时将外部函数的说明传递给大模型，使其能够根据用户意图，在必要的时候向外部函数发起调用请求。

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250318202029130.png" alt="image-20250318202029130" style="zoom:33%;" />

> Function calling最早由OpenAI与2023年6月13号正式提出，该项技术的名字也由此命名：https://openai.com/index/function-calling-and-other-api-updates/
>
> <img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250422153118206.png" alt="image-20250422153118206" style="zoom:33%;" />
>
> 此外，Function calling也被称作tool use、tool call等技术。

​	毫无疑问，Function calling的诞生意义重大，这项技术目前也成为大模型调用外部工具的基本技术范式，哪怕是MCP盛行的今天，底层仍然是Function calling执行流程。

#### 1.2 **Function calling公开课介绍**

​	而对于大模型开发者来说，无论是采用何种Agent开发框架或MCP技术，掌握Function calling的实现流程和底层原理至关重要，具体Function calling实现原理可以参考公开课《智能体从何而来？深度详解大模型调用工具底层原理》：https://www.bilibili.com/video/BV1w6dBYxELA/，而关于DeepSeek模型Function calling实现流程，可以参考公开课《DeepSeek智能体开发实战，从零手搓Mini Manus！》：https://www.bilibili.com/video/BV1L3ZDYDEnE/。

#### 1.3 **Function calling能力从何而来**

​	不过为了更好的学习本期公开课，需要重点强调的是关于大模型的Function calling的能力如何而来。我们都知道，对于当前大模型来说，有些模型有Function calling能力，如DeepSeek-V3模型，而有些模型没有，如DeepSeek-R1模型：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250422154443869.png" alt="image-20250422154443869" style="zoom: 33%;" />

甚至对于DeepSeek-V3-0324模型来说，还支持工具的并联、串联调用甚至是自动debug：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250422154552824.png" alt="image-20250422154552824" style="zoom: 50%;" />

> 具体代码实现流程可参考公开课《DeepSeek智能体开发实战，从零手搓Mini Manus！》：https://www.bilibili.com/video/BV1L3ZDYDEnE/。

那模型是如何具备Function calling能力的呢？答案是通过模型训练。对于DeepSeek-V3模型来说，由于在训练阶段（指令微调阶段）就带入了大量的类似如下的工具调用对话数据进行训练，因此能够识别外部工具并发起对外部工具调用的请求。而类似的，R1模型的训练过程没有工具调用数据，因此就不具备Function calling能力。

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250422154737842.png" alt="image-20250422154737842" style="zoom: 50%;" />

> 更多关于Function calling原理，可以参考公开课《智能体从何而来？深度详解大模型调用工具底层原理》：https://www.bilibili.com/video/BV1w6dBYxELA/，

而Function calling的能力，是大模型顺利开启MCP功能的基础。

#### 1.4 MCP技术本质：Function calling的更高层实现

​	而近一段时间大火的MCP技术，其实就可以将其理解为Function calling技术的更高层封装和实现。传统的Function calling技术要求围绕不同的外部工具API单独创建一个外部函数，类似一把锁单独配一把钥匙，而一个智能体又往往涉及到多个外部工具设计，因此开发工作量很大。

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250318185821214.png" alt="image-20250318185821214" style="zoom: 33%;" />

而MCP技术，全称为Model Context Protocol，模型上下文协议，是一种开发者共同遵守的协议，在这个协议框架下，大家围绕某个API开发的外部工具就能够共用，从而大幅减少重复造轮子的时间。

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250318185810201.png" alt="image-20250318185810201" style="zoom: 33%;" />

#### 1.5 MCP技术带来的智能体开发效率革命

​	举个例子，在我们开设的《大模型原理与实战课程》：https://whakv.xetslk.com/s/3p66pN系列课程中，2023年的第一期课程里曾经讲解过一个Agent实战项目，

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250422155926009.png" alt="image-20250422155926009" style="zoom:15%;" />

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250422155951977.png" alt="image-20250422155951977" style="zoom: 57%;" />

其中涉及关于大模型对话长短期记忆存储和管理相关功能实现时，光是编写消息类（Messages）对象的各种操作方法以及围绕本地文件夹的各类操作，如创建、删除、写入文档、清空对话、统计文本长度等，就写了300多行代码：

<video src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/452c6c9140ae5c41827d619c7f830241_raw.mp4"></video>

而现在，借助MCP技术，采用别人已经开发好的Filesystem工具，仅需几行代码，导入工具配置即可实现完全相同的功能。由此Agent开发效率大幅提高，而这就是MCP技术搭建起来的协作体系的力量。

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250422160858753.png" alt="image-20250422160858753" style="zoom:50%;" />

### 2. MCP服务器接入示例

​	而在MCP技术大爆发的今天，接入一个MCP工具也是非常简单，以下是一个将高德地图导航MCP（服务器）接入Cherry Studio（客户端）的示例：

<video src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/2025-04-14%2014-29-22.mp4"></video>

> 我们可以暂时把MCP服务器视作MCP工具。

我们能看到，现在如果想要接入一个MCP工具，我们只需要在支持MCP功能的客户端中写入相关配置即可。例如我们只需要在Cherry Studio的MCP配置文档中写入如下字段：

```json
    "amap-maps": {
      "isActive": true,
      "command": "npx",
      "args": [
        "-y",
        "@amap/amap-maps-mcp-server"
      ],
      "env": {
        "AMAP_MAPS_API_KEY": "YOUR_API_KRY"
      },
      "name": "amap-maps"
    }
```

![image-20250422162450429](https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250422162450429.png)

即可让大模型自动关联高德MCP工具（服务器），而一个高德MCP服务器的API有几十种之多：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250422162541456.png" alt="image-20250422162541456" style="zoom:50%;" />

可以说是覆盖了出行生活的放方面。而当一个大模型接入高德MCP服务器后，就能瞬间化身出行规划智能体。

> 更多客户端接入服务器方法，详见公开课《零门槛接入MCP！Cursor、阿里云百炼、Open-WebUI、Cherry Studio接入10大最热门MCP工具》：https://www.bilibili.com/video/BV1dCo7YdEgK/

而要知道的是，如果没有MCP工具，我们需要单独围绕这些API将其封装为一个个外部函数，再据此创建一个出行规划智能体，其工作量可想而知。

### 3. MCP工具标准接入流程

​	在上述示例中，我们不难发现，一个MCP服务器标准接入流程是通过写入一个配置文件来完成的。而在支持MCP功能的客户端（如Cherry Studio）中写入MCP工具的配置，其本质就是先将指定的MCP工具下载到本地，然后在有需要的时候对其进行调用。例如高德MCP配置文件如下：

```json
    "amap-maps": {
      "isActive": true,
      "command": "npx",
      "args": [
        "-y",
        "@amap/amap-maps-mcp-server"
      ],
      "env": {
        "AMAP_MAPS_API_KEY": "YOUR_API_KRY"
      },
      "name": "amap-maps"
    }
```

代表的含义就是我们需要先使用如下命令：

```bash
npx -y @amap/amap-maps-mcp-server
```

对这个库`@amap/amap-maps-mcp-server`进行下载，然后在本地运行，当有必要的时候调用这个库里面的函数执行相关功能。

​	而这个`@amap/amap-maps-mcp-server`库是一个托管在https://www.npmjs.com/上的库，

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250422163303357.png" alt="image-20250422163303357" style="zoom:33%;" />

可以使用npx命令进行下载。搜索库名即可看到这个库的完整代码，https://www.npmjs.com/package/@amap/amap-maps-mcp-server：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250422163336824.png" style="zoom: 33%;" />

而这种通过配置文件来进行MCP工具下载的方式，最早由Claude（MCP技术的提出者）提出并被广泛接纳。

### 4. MCP服务器与客户端

#### 4.1 MCP服务器（server）与客户端（client）概念介绍

​	在上面的示例中，Cherry Studio是一个支持MCP功能的客户端，而接入的高德MCP是一个MCP服务器，这里的客户端和服务器又是什么意思呢？

​	这其实是MCP技术体系中对于大模型和外部工具的另一种划分方式，也就是说在MCP技术体系中，会将外部工具运行脚本称作服务器，而接入这些外部工具的大模型运行环境称作客户端。

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250318202116026.png" alt="image-20250318202116026" style="zoom:50%;" />

一个客户端可以接入多个不同类型的服务器的，但要求是都可以遵循MCP通信协议。简单理解就是MCP服务器的输出内容是一种标准格式的内容，只能被MCP客户端所识别。在客户端和服务器都遵循MCP协议的时候，客户端就能够像Function calling中大模型调用外部工具一样，调用MCP服务器里面的工具。

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250318153131024.png" alt="image-20250318153131024" style="zoom:50%;" />

#### 4.2 MCP服务器集合

​	暂时抛开底层原理不谈，在MCP技术爆发的这几个月，市面上已经诞生了成百上千的MCP服务器，甚至还出现了大量的MCP服务器集合网站：

- MCP官方服务器合集：https://github.com/modelcontextprotocol/servers

  <img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250318195013063.png" alt="image-20250318195013063" style="zoom:50%;" />

- MCP Github热门导航：https://github.com/punkpeye/awesome-mcp-servers

  <img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250318195101093.png" alt="image-20250318195101093" style="zoom:50%;" />

- Smithery：https://smithery.ai/

  <img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250410160659176.png" alt="image-20250410160659176" style="zoom:50%;" />

- MCP导航：https://mcp.so/

  <img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250318195025102.png" alt="image-20250318195025102" style="zoom:50%;" />

在实际进行智能体开发过程中，我们可以参考这些网站上的MCP工具，并有选择的对其进行调用。但需要注意的是，无论这些网站的组织形式多么花样百出，但实际上当我们本地调用MCP工具的时候，都是通过uvx或者npx将对应的库下载到本地，然后再进行运行。

### 5. MCP与Function calling技术对比介绍

​	此外，我们还需要补充一点的是关于Function calling和MCP技术的关系。通过在MCP运行过程的抓包可知，MCP底层实际上仍然是借助大模型原生的Function calling来完成外部工具调用，只不过进行了更高层的封装。

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250422164758122.png" alt="image-20250422164758122" style="zoom:50%;" />

实际上MCP客户端对MCP服务器上的工具调用流程如下：

- **Step 1. 建立和服务器的通信**；
- **Step 2. 查询服务器上总共有多少个外部工具；**
- **Step 3. 将外部工具组成列表，带入到当前对话中；**
- **Step 4. 借助Function calling进行外部工具调用。**

也就是说，如果模型本身不支持Function calling，那么是无法顺利开启MCP功能的。

​	不过这里也有例外，那就是Open-WebUI和cline作为MCP客户端时，可以使用不具备Function calling功能的DeepSeek-R1模型进行MCP工具调用，这是为何呢？

​	原因非常简单，那就是这些客户端内置了一些提示词模板，借助提示让大模型输出类似Function call message（调用外部工具的信息）的内容，然后开启Function calling，从而能够调用MCP工具。举个例子，对于cline来说会通过一段非常长的提示词，引导模型输出Function call message：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250422165507170.png" alt="image-20250422165507170" style="zoom:50%;" />

>  cline项目官网：https://github.com/cline/cline

我们可以将其精简为如下形式：

```python
system_message = (
    "You are a helpful assistant with access to these tools:\n\n"
    f"{tools_description}\n"
    "Choose the appropriate tool based on the user's question. "
    "If no tool is needed, reply directly.\n\n"
    "IMPORTANT: When you need to use a tool, you must ONLY respond with "
    "the exact JSON object format below, nothing else:\n"
    "{\n"
    '    "tool": "tool-name",\n'
    '    "arguments": {\n'
    '        "argument-name": "value"\n'
    "    }\n"
    "}\n\n"
    "After receiving a tool's response:\n"
    "1. Transform the raw data into a natural, conversational response\n"
    "2. Keep responses concise but informative\n"
    "3. Focus on the most relevant information\n"
    "4. Use appropriate context from the user's question\n"
    "5. Avoid simply repeating the raw data\n\n"
    "Please use only the tools that are explicitly defined above."
)
```

翻译如下：

````markdown
你是一个乐于助人的助手，可以使用以下工具：

```
{tools_description}
```

请根据用户的问题选择合适的工具。  
如果不需要使用工具，请直接回复。

重要提示：如果需要使用工具，**你必须仅以以下精确的 JSON 对象格式进行回复，不要添加其他内容**：

```json
{
    "tool": "工具名称",
    "arguments": {
        "参数名称": "参数值"
    }
}
```

在收到工具返回的结果后：

1. 将原始数据转化为自然、对话式的回答  
2. 保持回答简洁但富有信息量  
3. 聚焦于最相关的信息  
4. 使用用户问题中的相关上下文  
5. 避免直接照搬原始数据

请**只使用上述明确定义的工具**。
````

在这些提示词引导下，一些不具备Function calling的大模型，也能顺利使用MCP工具。不过需要注意的是，借助提示词开启的MCP功能，毕竟不如模型原生能力稳定，因此如果希望搭建企业级应用的Agent，最好还是使用具备Function calling功能的大模型。

### 6. MCP技术生态

​	最后需要介绍当前MCP完整的技术生态。MCP技术发展至今，已经不再是简单的“协议”，而是一个包含了协议、开发工具和现成的已经开发好的MCP工具所共同组成的完整技术生态。

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250416155146454.png" alt="image-20250416155146454" style="zoom:50%;" />

其中：

- **MCP协议：**指的是“虚”的规范，例如大模型和工具调度规范、服务器客户端的通信规范等，遵循这些协议的对象就是MCP服务器或客户端；
- **MCP开发工具：**包含多种语言的SDK，也就是开发工具包，开发人员能够使用这些SDK快速完成MCP的服务器和客户端开发；
- **MCP服务器生态：**开源的MCP服务器，是基于MCP协议的庞大的技术生态，智能体开发人员可以直接使用开源的MCP工具来加快开发进程。

- 公开课代码领取

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/0202fa8f35ef772a657853eaf4ad58f.png" alt="0202fa8f35ef772a657853eaf4ad58f" style="zoom:50%;" />

## 二、从零到一进行MCP项目开发

​	在基本了解MCP技术概念之后，接下来为大家详细介绍如何从零到一完成MCP项目开发。根据此前的介绍不难发现，MCP项目开发会涉及两个方面，分别是MCP客户端开发和服务器开发，本节公开课我们将重点介绍MCP服务器开发，同时为大家提供一个通用的客户端模板。

### 1. MCP服务器开发流程介绍

​	MCP服务器通用开发流程如下：

- **Step 1.创建功能函数，并在代码环境中完成测试；**
- **Step 2.创建MCP服务器项目，完成服务器项目开发；**
- **Step 3.借助MCP官方工具Inspector进行MCP服务器debug；**
- **Step 4.借助MCP客户端，进行本地通信测试**
- **Step 5.【可选】将MCP服务器发布到npm或者pypi平台，供其他开发人员使用；**
- **Step 6.【可选】将MCP服务器项目离线拷贝并在其他服务器上运行。**

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250422172644338.png" alt="image-20250422172644338" style="zoom:50%;" />

接下来我们将详细介绍这6个环节的实现方法。

### 2. MCP Server核心功能开发

#### 2.1 Mini DeepResearch项目介绍

​	在规划MCP服务器项目开发的时候，我们首先需要确定当前MCP服务器的核心功能。我们这里尝试创建一个此前公开课介绍的Mini DeepResearch项目的MCP服务器，即一个集成了Mini DeepResearch功能的MCP服务器，能够围绕用户给出的主题进行深度搜索，并给出最终结果。接下来我们将把Mini DeepResearch封装为MCP服务器，一方面详细介绍MCP Server开发流程，同时也介绍**如何将一个Multi-Agent封装为MCP server并带入到其他应用场景中。**

- 项目效果演示

​	项目效果类似于ChatGPT DeepResearch功能，具体项目演示效果如下：

<video src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/Mini%20DeepResearch%E6%BC%94%E7%A4%BA.mp4"></video>

此时输入：`你好，我想了解下MCP（Model Context Protocol）这项技术`

输出：

```markdown
# MCP（模型上下文协议）技术深入解析报告

本文旨在对 MCP（Model Protocol Context，模型上下文协议）技术进行全面而深入的解析。从其技术背景、发展历程、核心架构，到应用领域和未来发展趋势，本文将以详细的说明和实例分析，帮助读者对 MCP 技术有一个透彻的认识。

---

## 1. 引言

随着人工智能（AI）的迅速发展和大型语言模型（LLM）的普及，传统的依赖静态训练数据的模式逐渐暴露出局限性。AI 模型在面对复杂、动态的应用场景时，亟需一种能够实时链接外部数据源和工具的技术方案。MCP，即模型上下文协议，正是在这种背景下应运而生。MCP 提供了标准化的接口，使 AI 模型可以安全、便捷地与外部系统进行数据交互和功能调用。本文将详细探讨 MCP 的技术架构、核心优势、实际应用案例及未来展望。

---

## 2. MCP 技术的起源与发展

MCP 技术最初由 Anthropic 公司提出，作为一种开放标准协议，其目标在于解决 AI 模型信息获取受限以及定制接口开发成本高昂的问题。传统的大型语言模型仅仅依靠之前的训练数据进行问答或生成内容，而一旦遇到应用场景中新产生的数据或需求，就会陷入信息更新滞后的尴尬。MCP 协议通过提供一种标准化的通信方法，实现了 AI 模型与外部数据源和工具的无缝衔接。

### 2.1 背景介绍

- **AI 发展带来的新要求**：随着算法和算力的提升，AI 模型在自然语言处理、图像识别、医学影像分析等领域展现了卓越的能力。然而，这些模型的训练数据相对静态，难以实时反映现实世界中大量动态变化的信息。MCP 的设计初衷就是为了解决这类静态数据与动态应用之间的脱节问题。
- **传统接口的局限性**：在传统应用中，开发者通常需要为每个外部数据源或工具编写专门的接口，造成了开发周期长、接口碎片化的问题。MCP 的出现使得各类数据源可以通过统一入口被 AI 模型调用，大幅降低了开发者的集成成本。

### 2.2 发展历程

自提出以来，MCP 迅速引起各界关注。从最初的标准构架到目前支持 STDIO 与 HTTP+SSE 两种数据传输方式，MCP 正在不断完善自身的协议规范，支持更多样化的数据交互模式。学术界和工业界纷纷开展针对 MCP 的研究和应用，力求更好地与现有系统集成，从而推动 AI 模型的应用边界不断拓宽。

---

## 3. MCP 的技术原理与架构

MCP 协议采用客户端-服务器模型，由三大核心组件构成：MCP 主机、MCP 客户端以及 MCP 服务器。这一模型确保 AI 模型能够通过标准化接口与外部工具或数据源进行高效交互。

### 3.1 核心组件

- **MCP 主机**：通常指运行在桌面版工具、集成开发环境（IDE）或 AI 辅助应用中的主程序，负责发起与外部系统的连接请求。
- **MCP 客户端**：位于主机程序内部，和 MCP 服务器保持 1:1 的连接关系，执行协议层面的消息传递和响应处理。
- **MCP 服务器**：独立的轻量级程序，通过标准化的 MCP 接口，连接各种本地或远程的数据源与外部服务，并按照协议要求提供相应的功能。

### 3.2 协议通信机制

MCP 协议采用 JSON-RPC 2.0 格式定义消息传输，确保通信内容具有清晰的请求与响应逻辑。主要包含以下两种传输方式：

- **STDIO 传输**：利用标准输入输出流完成数据传输，具有低延迟的优点，适用于高效通信需求的场景。
- **HTTP+SSE 传输**：通过 HTTP 协议结合服务器发送事件（Server-Sent Events），实现实时数据流和长连接通信，适合于跨网络环境的数据同步和更新。

这种灵活的通信机制不仅满足了高性能应用的要求，也为开发者允许实现定制的传输方式提供了可能性，但前提是必须保留 MCP 指定的消息格式和生命周期管理要求。

### 3.3 消息交换和生命周期管理

MCP 协议采用明确的消息帧格式，对请求、响应、通知等多种消息模式进行了详细定义。整个通信生命周期包括：

1. **初始化阶段**：客户端与服务器之间建立连接，并进行身份认证和功能协商。
2. **消息交换阶段**：在连接保持期间，双方通过请求-响应模型或推送通知模式进行数据传输和指令交互。
3. **终止阶段**：当通信任务完成或出现异常时，客户端或服务器终止连接，并进行资源回收。

这种设计确保了通信的稳定性和可靠性，极大地降低了系统集成的复杂性。

---

## 4. MCP 的关键优势与应用场景

### 4.1 关键优势

- **统一标准**：MCP 提供了开放、统一的通信接口，解决了传统 API 接口碎片化的问题，使得不同系统之间的集成更加简单高效。
- **动态数据交互**：借助 MCP，AI 模型可以在运行过程中动态获取外部数据，而不再局限于预先训练数据的内容，这大大提升了模型的实用性和智能化水平。
- **安全性与用户控制**：MCP 的设计强调用户对数据交互的控制权，通过标准化和严格的认证机制，在一定程度上保障了数据安全和隐私保护。
- **扩展性强**：惠及多种传输方式和应用场景，不论是本地数据访问还是远程服务调用，都能够灵活适配。

### 4.2 应用场景

#### 4.2.1 软件开发与调试

在软件开发领域，集成了 MCP 的编码工具能够自动读取和修改代码库，利用实时数据进行静态检查和代码优化，从而提升开发效率。例如，IDE 通常会集成 MCP 客户端，实现自动化错误提示和修正建议。

#### 4.2.2 数据科学与安全审计

数据科学家可以通过 MCP 安全地查询内部数据库或者调用大数据平台接口，无需暴露底层敏感凭据。同时，MCP 协议支持安全审计机制，减少了安全审计项，从而降低系统维护成本。

#### 4.2.3 医疗与健康管理

在医疗领域，医疗系统通过 MCP 协议整合患者生理数据、影像信息及实验室检测结果，生成更为精确的诊断报告。这种跨系统的数据整合，显著提升了医疗决策的准确性和效率。

#### 4.2.4 云平台与多集群管理

部分云平台，如华为云的多云容器平台，已经开始借助 MCP 实现跨云和多集群的统一管理。通过 MCP，企业可以实现应用在多集群间的动态部署和弹性伸缩，有效解决多云环境下应用管理和资源调度的挑战。

---

## 5. 案例分析与技术比较

### 5.1 实际应用案例

以某三甲医院的医疗信息系统为例，通过引入 MCP，医院大大缩短了医疗影像系统与电子病历对接的周期。以前需要数月时间完成的数据对接，如今可在短短几天内实现，既提高了医疗服务效率，也降低了系统的集成成本。

### 5.2 与传统 API 的比较

传统 API 接口往往需要针对每个数据源进行单独开发和维护，存在定制成本高、适配性差等问题。相比之下，MCP 的标准化接口能够快速对接各种外部工具和数据源，极大地提升了 AI 模型在实际场景中的响应速度和准确性。

---

## 6. MCP 技术的发展趋势与面临的挑战

### 6.1 发展趋势

随着技术不断演进，MCP 正在向更高的集成化和智能化方向发展。未来的发展趋势主要包括：

- **标准的不断完善**：随着越来越多的开发者和企业参与，MCP 的协议规范将进一步细化，涵盖更多应用场景。
- **跨平台的广泛应用**：MCP 的统一标准不仅适用于桌面工具和云平台，还将扩展到移动设备、物联网设备等各类终端中。
- **多智能体协作**：未来的 AI 应用将越来越依赖多个模型之间的协同工作，MCP 将为这些多智能体系统提供高效的上下文传递和状态同步能力。
- **安全性与隐私保护进一步加强**：在数据安全和用户隐私方面，MCP 将引入更多先进的加密和认证技术，以满足日益严格的安全需求。

### 6.2 面临的挑战

尽管 MCP 技术具备诸多优势，但在推广和应用过程中仍面临一些挑战：

- **技术普及和标准统一**：作为新兴技术，MCP 需要更多的行业参与者和开发者支持，才能形成统一的标准生态。
- **兼容性与扩展性平衡**：在设计上，如何在保证标准化的同时，又能灵活应对不同应用的特殊需求，是 MCP 需要解决的问题。
- **安全性保障**：在跨平台、跨系统数据交互过程中，如何确保数据不被泄露并严格控制访问权限，是技术实现中的重点和难点。

---

## 7. 总结与展望

MCP（模型上下文协议）作为一种前沿的开放标准协议，通过标准化的接口，实现了 AI 模型与外部数据源和工具之间高效、安全的交互。本文从 MCP 的起源、技术架构、优势、应用案例及未来发展趋势等多个方面进行了详细阐述，展示了其在软件开发、医疗信息系统、云平台管理等领域的潜在价值。

可以预见，在 AI 应用不断深入和场景日益复杂的背景下，MCP 有望成为连接静态模型与动态数据的重要桥梁，推动人工智能迈向更加智能和高效的未来。面对未来，行业内各方需要进一步协同合作，完善标准、提升安全防护，并不断扩展协议的应用领域，共同探索 MCP 技术的最佳实践和发展路径。

---

## 参考文献与进一步阅读

1. [模型上下文协议（Wikipedia）](https://zh.wikipedia.org/wiki/%E6%A8%A1%E5%9E%8B%E4%B8%8A%E4%B8%8B%E6%96%87%E5%8D%8F%E8%AE%AE)
2. [Model Context Protocol 官方文档](https://modelcontextprotocol.info/zh-cn/docs/introduction/)
3. [有关 MCP 在 AI 集成中的应用探讨](https://blog.eimoon.com/p/mcp-introduction/?utm_source=openai)

---

*注：本文主要聚焦于 MCP 作为一项开放标准协议的技术体系，不同领域中同样缩写为 MCP 的其他技术（如多芯片封装、微通道板）则属于截然不同的技术体系，读者在查阅相关文献时需注意区分。*
```

- 课件领取

Mini DeepResearch公开课资料见本节公开课网盘：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250422175708266.png" alt="image-20250422175708266" style="zoom:50%;" />

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250422175724068.png" alt="image-20250422175724068" style="zoom:50%;" />

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/6920963aa5d94ab50c23e4e8b86144d.png" alt="6920963aa5d94ab50c23e4e8b86144d" style="zoom:50%;" />

- Mini DeepResearch技术栈

​	Mini DeepResearch以OpenAI模型及开源Agents SDK框架为主进行的开发，实际运行过程中需要输入OpenAI API-KEY。OpenAI API-KEY获取方法详见课件中的参考资料《OpenAI注册指南》部分，此外也可以直接在某宝上购买官方API-KEY。此外，项目中自带国内反向代理地址，无需额外网络门槛即可使用。

> 需要注意的是，必须要使用OpenAI官方API-KEY才能运行项目，中转API-KEY无法运行。

- Mini DeepResearch命令行快速上手使用

​	在课件中下载MiniDeepResearch.zip压缩包并解压缩，然后即可在主目录下运行该项目：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250422181458515.png" alt="image-20250422181458515" style="zoom:50%;" />

需要提前安装openai库和agents库

```bash
pip install openai openai-agents
```

并且在三个_agent.py文件中写入国内反向代理地址和OpenAI官方API-KEY，然后输入如下命令即可运行：

```bash
python -m ChatBot.main
```

#### 2.2 Mini DeepResearch项目架构介绍

​	接下来让我们快速回顾这个Multi-Agent系统核心代码结构。Mini DeepResearch主要由三个Agent构成：

| Agent           | 功能                                    |
| --------------- | --------------------------------------- |
| `planner_agent` | 生成研究关键词和搜索策略                |
| `search_agent`  | 负责执行网络搜索 + 总结内容（使用工具） |
| `writer_agent`  | 汇总所有搜索结果，编写报告              |

并且实际运行过程中，三个Agent组成一个线性的workflow进行运行：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250422183609642.png" alt="image-20250422183609642" style="zoom:50%;" />

这其实是一个相对简单的Multi-Agent系统，并且在最新GPT-4.1和o4-mini模型加持下，以及搭配开源的Agents-SDK框架和GPT模型原生的网络搜索功能，能够非常高效稳定的实现类DeepResearch功能。

​	接下来我们逐个介绍这三个Agent代码实现。以下代码均在Jupyter中完成测试，代码课件详见：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250423170244816.png" alt="image-20250423170244816" style="zoom:50%;" />

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250423202415047.png" alt="image-20250423202415047" style="zoom:50%;" />

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/6920963aa5d94ab50c23e4e8b86144d.png" alt="6920963aa5d94ab50c23e4e8b86144d" style="zoom: 50%;" />

#### 2.3 planner_agent功能实现

- 基础依赖库安装

```bash
pip install openai openai-agents
```

- 基础代码测试

​	这里首先需要设置基础Agents-SDK开发环境并进行简单测试，测试代码如下：

```python
from openai import AsyncOpenAI
from agents import OpenAIChatCompletionsModel,Agent,Runner,set_default_openai_client, set_tracing_disabled
from agents.model_settings import ModelSettings
from pydantic import BaseModel
from agents import Agent, WebSearchTool
from agents.model_settings import ModelSettings
import os
from dotenv import load_dotenv
load_dotenv(override=True)

external_client = AsyncOpenAI(
    base_url = os.getenv("BASE_URL"),
    api_key = os.getenv("API_KEY"), 
)
set_default_openai_client(external_client)
set_tracing_disabled(True)
agent = Agent(name="Assistant", instructions="你是一名助人为乐的助手。")
result = await Runner.run(agent, "请写一首关于编程中递归的俳句。") 
print(result.final_output)
```

这里需要在base_url中填写国内反向代理地址，需要在api_key中填写OpenAI的API-KEY。实际运行结果如下：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250422183323339.png" alt="image-20250422183323339" style="zoom:50%;" />

- planner_agent代码详解与功能介绍

​	接下来创建planner_agent，具体代码如下：

```python
PROMPT = (
    "You are a helpful research assistant. Given a query, come up with a set of web searches "
    "to perform to best answer the query. Output between 10 and 20 terms to query for."
)


class WebSearchItem(BaseModel):
    reason: str
    "Your reasoning for why this search is important to the query."

    query: str
    "The search term to use for the web search."


class WebSearchPlan(BaseModel):
    searches: list[WebSearchItem]
    """A list of web searches to perform to best answer the query."""


planner_agent = Agent(
    name="PlannerAgent",
    instructions=PROMPT,
    model="o4-mini",
    output_type=WebSearchPlan,
)
```

​	其中Planner Agent 的职责是接收一个研究主题，生成一份“搜索计划（WebSearchPlan）”，告诉系统应该搜索哪些子问题/关键词以及搜索这些关键词的理由。具体代码解释如下：

```python
from pydantic import BaseModel
```

导入 Pydantic，用于定义结构化数据模型。它是整个 Agents SDK 中用于**类型校验 + 数据结构定义**的核心库。

```python
from agents import Agent
```

导入 SDK 的核心类 `Agent`，我们后面会实例化一个具体的 Agent 实体 `planner_agent`。

```python
PROMPT = (
    "You are a helpful research assistant. Given a query, come up with a set of web searches "
    "to perform to best answer the query. Output between 20 and 30 terms to query for."
)
```

定义这个 Agent 的提示词（Prompt），告诉 LLM：

- 你是一个研究助手；
- 收到一个主题后，请生成 20 到 30 条搜索建议；
- 每条建议应当包括 **搜索关键词 + 搜索原因**。


接下来是两个重要的数据结构定义：

```python
class WebSearchItem(BaseModel):
    reason: str
    "Your reasoning for why this search is important to the query."

    query: str
    "The search term to use for the web search."
```

这是一个“单个搜索建议”的结构，包含两个字段：

| 字段     | 说明                                           |
| -------- | ---------------------------------------------- |
| `reason` | 你为什么要搜索这个关键词？（用于解释搜索动机） |
| `query`  | 你要搜索的关键词本身                           |


```python
class WebSearchPlan(BaseModel):
    searches: list[WebSearchItem]
    """A list of web searches to perform to best answer the query."""
```

这是“搜索计划”的整体结构，包含一个列表 `searches`，每项是上面的 `WebSearchItem`。

其中模型输出结构化的关键在这：

```python
output_type=WebSearchPlan,
```

它告诉 `planner_agent` **“你必须输出一份结构化的 WebSearchPlan 对象，里面包含多个 WebSearchItem。”**这样可以约束模型输出格式，也便于下一步自动解析内容。

​	实际运行效果如下：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250422183732911.png" alt="image-20250422183732911" style="zoom:50%;" />

输出了14个搜索关键词和对应的搜索原因。

#### 2.4 search_agent功能实现

​	接下来是负责实际执行搜索工作的search_agent，代码如下：

```python
from agents import Agent, WebSearchTool
from agents.model_settings import ModelSettings

INSTRUCTIONS = (
    "You are a research assistant. Given a search term, you search the web for that term and "
    "produce a concise summary of the results. The summary must 2-3 paragraphs and less than 300 "
    "words. Capture the main points. Write succinctly, no need to have complete sentences or good "
    "grammar. This will be consumed by someone synthesizing a report, so its vital you capture the "
    "essence and ignore any fluff. Do not include any additional commentary other than the summary "
    "itself."
)

search_agent = Agent(
    name="Search agent",
    instructions=INSTRUCTIONS,
    tools=[WebSearchTool()],
    model_settings=ModelSettings(tool_choice="required"),
)
```

`search_agent` 的作用是接收一个**搜索关键词**，调用 Web 搜索工具，然后根据搜索结果生成一份简洁的摘要（2-3 段，<300词），**不带评论，只保留信息本身**。也就是说，这是整个系统中真正“去网上查资料”的角色。具体代码解释如下：

```python
from agents import Agent, WebSearchTool
from agents.model_settings import ModelSettings
```

其中：

- `Agent`：导入 SDK 的智能体基类；
- `WebSearchTool`：一个由 Agents SDK 内置的**网页搜索工具**，调用它可以模拟 “上网搜索” 的效果；
- `ModelSettings`：可以配置一些模型使用时的行为，比如是否必须使用工具。

然后是重点提示词 `INSTRUCTIONS`

```python
INSTRUCTIONS = (
    "You are a research assistant. Given a search term, you search the web for that term and"
    "produce a concise summary of the results. The summary must 2-3 paragraphs and less than 300"
    "words. Capture the main points. Write succinctly, no need to have complete sentences or good"
    "grammar. This will be consumed by someone synthesizing a report, so its vital you capture the"
    "essence and ignore any fluff. Do not include any additional commentary other than the summary"
    "itself."
)
```

这是模型的行为提示，翻译一下这段内容的精髓：

| 指令含义                           | 说明                                    |
| ---------------------------------- | --------------------------------------- |
| 你是一个研究助手                   | 模拟一个能查资料的人                    |
| 给你关键词后上网搜索               | 关键词来自 planner_agent                |
| 写出 2-3 段简洁总结                | 每次搜索结果必须压缩成 300 字以内的摘要 |
| 用要点式语言、可以语法不完整       | 不要求像论文，重点是信息密度高          |
| 不要添加自己的评论                 | 不能主观判断，只提取信息                |
| 最终目的是为后续写报告的人准备素材 | 所以格式自由，内容集中就行              |

接下来创建创建 Agent 对象

```python
search_agent = Agent(
    name="Search agent",
    instructions=INSTRUCTIONS,
    tools=[WebSearchTool()],
    model_settings=ModelSettings(tool_choice="required"),
)
```

其中`name="Search agent"`是Agent 名称，用于日志和上下文显示。而`instructions=INSTRUCTIONS`告诉大语言模型它要怎么完成任务。`tools=[WebSearchTool()]`设置它可以使用的工具。在这个 case 中，它只能用 `WebSearchTool`，这是 SDK 内置的网页搜索工具。而`model_settings=ModelSettings(tool_choice="required")`则表示：**强制要求模型一定要调用工具（WebSearchTool）来完成任务**。不允许模型“凭空回答”或“胡编搜索内容”，这有助于提升真实性。

总结流程如下：

```
关键词（来自 planner_agent） → search_agent →
     🔍 使用 WebSearchTool 搜索
     ✂️ 根据结果生成 2-3 段摘要
     📦 返回给 writer_agent 写整合报告
```

带入planner_agent的一个搜索条目后运行效果如下：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250422184136261.png" alt="image-20250422184136261" style="zoom:50%;" />

#### 2.5 writer_agent功能实现

​	最后则是writer_agent的功能介绍，其核心代码如下：

```python
from pydantic import BaseModel
from agents import Agent

PROMPT_TEMP = (
    "You are a senior researcher tasked with writing a cohesive report for a research query. "
    "You will be provided with the original query, and some initial research done by a research "
    "assistant.\n"
    "You should first come up with an outline for the report that describes the structure and "
    "flow of the report. Then, generate the report and return that as your final output.\n"
    "The final output should be in markdown format, and it should be lengthy and detailed. Aim "
    "for 10-20 pages of content, at least 1500 words."
    "最终结果请用中文输出。"
)


class ReportData(BaseModel):
    short_summary: str
    """A short 2-3 sentence summary of the findings."""

    markdown_report: str
    """The final report"""

    follow_up_questions: list[str]
    """Suggested topics to research further"""


writer_agent = Agent(
    name="WriterAgent",
    instructions=PROMPT_TEMP,
    model="o4-mini",
    output_type=ReportData,
)
```

Writer Agent这是 **整个研究系统的“输出终结者”**，负责把之前所有搜索到的信息，**综合成一份完整、结构化、可阅读的长篇报告**。该 Agent 的任务是：

- 收到研究主题和之前的所有搜索摘要；
- **先写一个大纲（outline）**；
- 然后根据大纲写出一份 **详细的 Markdown 格式报告**；
- 同时生成一个简短总结和一些后续可以研究的问题。

具体代码解释如下：

```python
# Agent used to synthesize a final report from the individual summaries.
from pydantic import BaseModel
from agents import Agent
```

- 和前两个 Agent 一样，我们导入了：
  - `BaseModel`：用于定义结构化输出；
  - `Agent`：Agent SDK 中的核心类。

然后是提示词定义（Prompt）

```python
PROMPT = (
    "You are a senior researcher tasked with writing a cohesive report for a research query. "
    "You will be provided with the original query, and some initial research done by a research "
    "assistant.\n"
    "You should first come up with an outline for the report that describes the structure and "
    "flow of the report. Then, generate the report and return that as your final output.\n"
    "The final output should be in markdown format, and it should be lengthy and detailed. Aim "
    "for 15-20 pages of content, at least 3000 words."
    "最终结果请用中文输出。"
)
```

提示词要点：

| 行为     | 说明                                          |
| -------- | --------------------------------------------- |
| 角色设定 | 你是一个资深研究员（senior researcher）       |
| 输入     | 会拿到：研究主题 + 搜索摘要                   |
| 第一步   | 写出报告结构（outline）                       |
| 第二步   | 写出 Markdown 报告正文                        |
| 要求     | 长、详细、有逻辑（10-20页，1500+词）          |
| 输出格式 | Markdown 格式（如 `# 一级标题`, `- 列表` 等） |
| 语言风格 | 精炼、学术、结构清晰                          |

这个 prompt 是整个系统中最“生成型”的一个 prompt。紧接着是输出数据结构定义，定义一个 `ReportData` 类，用来约束模型的输出结构：

```python
class ReportData(BaseModel):
    short_summary: str
    """A short 2-3 sentence summary of the findings."""

    markdown_report: str
    """The final report"""

    follow_up_questions: list[str]
    """Suggested topics to research further"""
```

具体含义如下：

| 字段名                | 类型        | 说明                              |
| --------------------- | ----------- | --------------------------------- |
| `short_summary`       | `str`       | 对研究结果的简要总结（2~3 句话）  |
| `markdown_report`     | `str`       | 报告正文，Markdown 格式，内容详实 |
| `follow_up_questions` | `list[str]` | 建议后续可以进一步研究的问题列表  |

注意：这个结构就是通过 `output_type=ReportData` 来告诉 SDK 要求模型输出这个结构，否则 SDK 会报错或解析失败。

紧接着创建 Agent 实例

```python
writer_agent = Agent(
    name="WriterAgent",
    instructions=PROMPT,
    model="gpt-4.1",
    output_type=ReportData,
)
```

| 参数           | 含义                                                     |
| -------------- | -------------------------------------------------------- |
| `name`         | Agent 名                                                 |
| `instructions` | 提示词指令                                               |
| `model`        | 使用的模型（这里是 `"gpt-4.1"`，可以替换为 `gpt-4o` 等） |
| `output_type`  | 指定输出为 `ReportData` 类型，支持结构化结果             |


整体流程总结如下：

```text
1. 用户输入研究主题 → planner_agent → 搜索关键词列表
2. 每个关键词 → search_agent → 搜索摘要
3. 所有摘要集合 + 原始主题 → writer_agent →
     📌 输出：
     - short_summary
     - markdown_report（正文）
     - follow_up_questions（可继续研究的问题）
```

最终返回的是一个完整结构化的 `ReportData` 对象。

​	带入其中第一个条目搜索结果后可以编写文本如下：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250422184456790.png" alt="image-20250422184456790" style="zoom:50%;" />

需要注意的是，实际执行过程中，需要带入全部搜索条目的短文本后再编写最终的长文本。

#### 2.6 MCP服务器主函数编写

​	在实现了这一系列Agents的基础功能之后，我们来编写当前MCP服务器的主函数。其实MCP服务器的主函数和Function calling运行过程中的外部函数类似，基本要求如下：

1. 能实现稳定的输入和输出。对于当前Mini DeepResearch服务器来说，输入就是用户的问题，而输出就是最终的调研报告；
2. 需要编写明确的函数说明，包括函数功能、函数参数和函数输出等。这些内容都是MCP客户端去识别外部工具的关键。
3. 推荐可以使用MCP SDK进行服务器开发。

​	这里我们创建一个deepresearch函数组，这个函数组用于调用上面的Agents来执行完整的规划、搜索和文档编写工作，该函数组完整代码如下：

```python
import asyncio
import os
import time
from typing import List

async def _plan_searches(query: str) -> WebSearchPlan:
    """
    用于进行某个搜索主题的搜索规划
    """
    result = await Runner.run(
        planner_agent,
        f"Query: {query}",
    )
    return result.final_output_as(WebSearchPlan)

async def _perform_searches(search_plan: WebSearchPlan) -> List[str]:
    """
    用于实际执行搜索，并组成搜索条目列表
    """
    tasks = [asyncio.create_task(_search(item)) for item in search_plan.searches]
    results = []
    for task in asyncio.as_completed(tasks):
        result = await task
        if result is not None:
            results.append(result)
    return results

async def _search(item: WebSearchItem) -> str | None:
    """
    实际负责进行搜索，并完成每个搜索条目的短文本编写
    """
    try:
        result = await Runner.run(
            search_agent,
            input=f"Search term: {item.query}\nReason for searching: {item.reason}"
        )
        return str(result.final_output)
    except Exception:
        return None
    
async def _write_report(query: str, search_results: List[str]) -> ReportData:
    """
    根据搜索的段文档，编写长文本
    """
    result = await Runner.run(
        writer_agent,
        input=f"Original query: {query}\nSummarized search results: {search_results}",
    )
    return result.final_output_as(ReportData)


async def deepresearch(query: str) -> ReportData:
    """
    主函数，输入一个研究主题，自动完成搜索规划、搜索、写报告。
    返回最终的 ReportData 对象，就是一个markdown格式的完整的研究报告文档
    """
    search_plan = await _plan_searches(query)
    search_results = await _perform_searches(search_plan)
    report = await _write_report(query, search_results)
    return report
```

编写完成后可以输入如下代码进行测试：

```python
import nest_asyncio
nest_asyncio.apply()

report = await deepresearch("人工智能在教育领域的应用")

from rich.markdown import Markdown
display(Markdown(report.markdown_report))
```

具体运行结果如下所示：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250422193358384.png" alt="image-20250422193358384" style="zoom:33%;" />

- 课件领取

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250423202445365.png" alt="image-20250423202445365" style="zoom:50%;" />

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/6920963aa5d94ab50c23e4e8b86144d.png" alt="6920963aa5d94ab50c23e4e8b86144d" style="zoom:50%;" />

### 3. MCP Server项目开发

​	在完成了代码功能测试后，接下来我们需要创建一个完整的MCP Server项目来实现该功能。对于一个完整的MCP项目来说，要有完整的项目代码结构、以及符合MCP服务器基本调用规范。具体项目创建流程如下：

#### Step 1. 借助uv创建Python项目

​	MCP开发要求借助uv进行虚拟环境创建和依赖管理。`uv` 是一个**Python 依赖管理工具**，类似于 `pip` 和 `conda`，但它更快、更高效，并且可以更好地管理 Python 虚拟环境和依赖项。它的核心目标是**替代 `pip`、`venv` 和 `pip-tools`**，提供更好的性能和更低的管理开销。

**`uv` 的特点**：

1. **速度更快**：相比 `pip`，`uv` 采用 Rust 编写，性能更优。
2. **支持 PEP 582**：无需 `virtualenv`，可以直接使用 `__pypackages__` 进行管理。
3. **兼容 `pip`**：支持 `requirements.txt` 和 `pyproject.toml` 依赖管理。
4. **替代 `venv`**：提供 `uv venv` 进行虚拟环境管理，比 `venv` 更轻量。
5. **跨平台**：支持 Windows、macOS 和 Linux。

​	以Ubuntu系统为例，首先使用pip安装uv：

```bash
pip install uv
```

> 此外，也可以直接使用curl安装uv
>
> ```bash
> curl -LsSf https://astral.sh/uv/install.sh | sh
> ```

然后按照如下流程创建项目主目录：

```bash
# cd /root/autodl-tmp/MCP

# 创建项目目录
uv init mcp-server-deepresearch
cd mcp-server-deepresearch
```

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250422205522445.png" alt="image-20250422205522445" style="zoom:50%;" />

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250422205551113.png" alt="image-20250422205551113" style="zoom:50%;" />

然后输入如下命令创建虚拟环境：

```bash
# 创建虚拟环境
uv venv

# 激活虚拟环境
source .venv/bin/activate
```

此时就构建了一个基础项目结构：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250422205823374.png" alt="image-20250422205823374" style="zoom:50%;" />

各文件解释如下：

| 文件/文件夹       | 作用             |
| ----------------- | ---------------- |
| `.git/`           | Git 版本控制目录 |
| `.venv/`          | 虚拟环境         |
| `.gitignore`      | Git 忽略规则     |
| `.python-version` | Python版本声明   |
| `main.py`         | 主程序入口       |
| `pyproject.toml`  | 项目配置文件     |
| `README.md`       | 项目说明文档     |

#### Step 2. 添加项目依赖

​	接下来继续使用uv工具，为我们的项目添加基础依赖。根据此前的代码解释不难看出，当前项目主要需要用到`openai`和`openai-agents`这两个库，我们可以使用如下命令安装相关依赖，并同时安装mcp sdk：

```bash
# 安装 MCP SDK
uv add mcp openai openai-agents asyncio typing pydantic
```

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250422210130954.png" alt="image-20250422210130954" style="zoom:50%;" />

注意，对于uv管理库来说，相关依赖会安装到.venv文件中，并不会和系统库产生冲突。

#### Step 3.编写项目源码

​	接下来在主目录下创建`/src/mcp_server_deepresearch`作为代码主目录

```bash
mkdir -p ./src/mcp_server_deepresearch
cd ./src/mcp_server_deepresearch
```

然后创建server.py脚本，作为整个DeepResearch MCP服务器的核心脚本，

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250423170612007.png" alt="image-20250423170612007" style="zoom:50%;" />

并写入代码如下：

```python
import asyncio
import argparse
from typing import List
from mcp.server.fastmcp import FastMCP
from openai import AsyncOpenAI
from pydantic import BaseModel
from agents import OpenAIChatCompletionsModel,Agent,Runner,set_default_openai_client, set_tracing_disabled,WebSearchTool
from agents.model_settings import ModelSettings

# 初始化 MCP 服务器
mcp = FastMCP("DeepResearch")
USER_AGENT = "deepresearch-app/1.0"
API_KEY = None

# 创建planner_agent
PROMPT = (
    "You are a helpful research assistant. Given a query, come up with a set of web searches "
    "to perform to best answer the query. Output between 10 and 20 terms to query for."
)


class WebSearchItem(BaseModel):
    reason: str
    "Your reasoning for why this search is important to the query."

    query: str
    "The search term to use for the web search."


class WebSearchPlan(BaseModel):
    searches: list[WebSearchItem]
    """A list of web searches to perform to best answer the query."""


planner_agent = Agent(
    name="PlannerAgent",
    instructions=PROMPT,
    model="o3-mini",
    output_type=WebSearchPlan,
)

# 创建search_agent
INSTRUCTIONS = (
    "You are a research assistant. Given a search term, you search the web for that term and "
    "produce a concise summary of the results. The summary must 2-3 paragraphs and less than 300 "
    "words. Capture the main points. Write succinctly, no need to have complete sentences or good "
    "grammar. This will be consumed by someone synthesizing a report, so its vital you capture the "
    "essence and ignore any fluff. Do not include any additional commentary other than the summary "
    "itself."
)

search_agent = Agent(
    name="Search agent",
    instructions=INSTRUCTIONS,
    tools=[WebSearchTool()],
    model_settings=ModelSettings(tool_choice="required"),
)

# 创建writer_agent
PROMPT_TEMP = (
    "You are a senior researcher tasked with writing a cohesive report for a research query. "
    "You will be provided with the original query, and some initial research done by a research "
    "assistant.\n"
    "You should first come up with an outline for the report that describes the structure and "
    "flow of the report. Then, generate the report and return that as your final output.\n"
    "The final output should be in markdown format, and it should be lengthy and detailed. Aim "
    "for 10-20 pages of content, at least 1500 words."
    "最终结果请用中文输出。"
)


class ReportData(BaseModel):
    short_summary: str
    """A short 2-3 sentence summary of the findings."""

    markdown_report: str
    """The final report"""

    follow_up_questions: list[str]
    """Suggested topics to research further"""


writer_agent = Agent(
    name="WriterAgent",
    instructions=PROMPT_TEMP,
    model="o3-mini",
    output_type=ReportData,
)

# 辅助函数组
async def _plan_searches(query: str) -> WebSearchPlan:
    """
    用于进行某个搜索主题的搜索规划
    """
    result = await Runner.run(
        planner_agent,
        f"Query: {query}",
    )
    return result.final_output_as(WebSearchPlan)

async def _perform_searches(search_plan: WebSearchPlan) -> List[str]:
    """
    用于实际执行搜索，并组成搜索条目列表
    """
    tasks = [asyncio.create_task(_search(item)) for item in search_plan.searches]
    results = []
    for task in asyncio.as_completed(tasks):
        result = await task
        if result is not None:
            results.append(result)
    return results

async def _search(item: WebSearchItem) -> str | None:
    """
    实际负责进行搜索，并完成每个搜索条目的短文本编写
    """
    try:
        result = await Runner.run(
            search_agent,
            input=f"Search term: {item.query}\nReason for searching: {item.reason}"
        )
        return str(result.final_output)
    except Exception:
        return None
    
async def _write_report(query: str, search_results: List[str]) -> ReportData:
    """
    根据搜索的段文档，编写长文本
    """
    result = await Runner.run(
        writer_agent,
        input=f"Original query: {query}\nSummarized search results: {search_results}",
    )
    return result.final_output_as(ReportData)

# MCP服务器主函数
@mcp.tool()
async def deepresearch(query: str) -> ReportData:
    """
    当用户明确表示需要围绕某个主题进行深入研究时，请调本函数。
    本函数能够围绕用户输入的问题进行联网搜索和深入研究，并创建一篇内容完整的markdown格式的研究报告。
    输入参数query:用户提出的研究主题，以字符串形式表示；
    函数返回结果为一个markdown格式的完整的研究报告文档。
    """
    search_plan = await _plan_searches(query)
    search_results = await _perform_searches(search_plan)
    report = await _write_report(query, search_results)
    return report

def main():
    parser = argparse.ArgumentParser(description="DeepResearch Server")
    parser.add_argument("--openai_api_key", type=str, required=True, help="你的 OpenAI API Key")
    args = parser.parse_args()

    # 初始化 external_client 和设置
    external_client = AsyncOpenAI(
        base_url = "https://ai.devtool.tech/proxy/v1",
        api_key = args.openai_api_key,
    )
    set_default_openai_client(external_client)
    set_tracing_disabled(True)
    
    mcp.run(transport='stdio')

if __name__ == "__main__":
    main()
```

其中主要内容均为此前介绍的三个Agent和调度函数组的内容，而整个MCP服务器开发核心采用了fastmcp库进行高效开发：

```python
from mcp.server.fastmcp import FastMCP
```

借助fastmcp，我们仅需在脚本初始化一个MCP服务器对象，

```python
mcp = FastMCP("DeepResearch")
```

然后使用装饰器为其添加一些函数

```python
# MCP服务器主函数
@mcp.tool()
async def deepresearch(query: str) -> ReportData:
```

然后即可创建一个自定义功能的MCP服务器。我们也可以简单的将MCP服务器理解为嵌套在功能函数外层的一个对象。而在实际运行的时候，我们仅需在主函数的尾部加上：

```python
mcp.run(transport='stdio')
```

即可完成MCP服务器进程的开启。

​	不难看出借助MCP高级SDK开发MCP服务器的流程实际上非常简单，整个代码编写过程主要还是需要写清楚功能函数的执行逻辑。

> 更多MCP SDK详见官网介绍：https://github.com/modelcontextprotocol/python-sdk
>
> <img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250423172103323.png" alt="image-20250423172103323" style="zoom:50%;" />

​	而parser相关代码则是规定在调用该脚本时需要通过参数输入来设置OpenAI的API-KEY。具体解释如下：

```python
def main():
```

- 定义一个名为 `main` 的函数，作为程序的主入口函数。

```python
    parser = argparse.ArgumentParser(description="DeepResearch Server")
```

- 使用 `argparse` 模块来创建一个命令行参数解析器 `parser`。
- `description="DeepResearch Server"` 是该程序的描述，用于命令行中帮助信息的展示。

```python
    parser.add_argument("--openai_api_key", type=str, required=True, help="你的 OpenAI API Key")
```

- 定义了一个命令行参数 `--openai_api_key`，类型为字符串，**必须提供（`required=True`）**。
- `help="你的 OpenAI API Key"` 表示当用户运行 `python script.py --help` 时，会看到这段提示。

✅ 示例调用：

```bash
python script.py --openai_api_key sk-xxxxx
```

```python
    args = parser.parse_args()
```

- 从命令行读取并解析用户输入的参数，将其保存到 `args` 变量中。
- 现在可以通过 `args.openai_api_key` 访问用户输入的 API key。

```python
    external_client = AsyncOpenAI(
        base_url = "https://ai.devtool.tech/proxy/v1",
        api_key = args.openai_api_key,
    )
```

- 创建一个 OpenAI 的异步客户端实例 `external_client`，这个客户端使用了一个**代理接口** `https://ai.devtool.tech/proxy/v1`。
- 使用了用户提供的 `openai_api_key` 作为身份验证。

```python
    set_default_openai_client(external_client)
```

- 将刚刚创建的 `external_client` 设置为**全局默认的 OpenAI 客户端**，后续代码调用模型接口时将自动使用这个客户端。
- 通常用于封装库内部（比如 Agent 框架）统一使用这个客户端。

```python
    set_tracing_disabled(True)
```

- 禁用“追踪（Tracing）”功能，可能用于避免记录日志或追踪操作。具体是否影响功能取决于你使用的 SDK 或 Agent 框架。

```python
    mcp.run(transport='stdio')
```

- 启动 MCP（Model Context Protocol）服务器，采用 `stdio` 作为**传输方式**。
- `stdio` 传输方式通常用于与终端交互或被其他进程通过标准输入/输出调用（类似 CLI 工具或嵌套调用）。

这段 `main` 函数的逻辑是：

1. 从命令行中获取用户输入的 `OpenAI API Key`。
2. 构造一个通过代理地址访问 OpenAI 的异步客户端。
3. 设置这个客户端为默认客户端，禁用 tracing。
4. 以 `stdio` 模式启动 MCP Server

整个项目的脚本文件可以在网盘中领取：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250423171626094.png" alt="image-20250423171626094" style="zoom:50%;" />

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/6920963aa5d94ab50c23e4e8b86144d.png" alt="6920963aa5d94ab50c23e4e8b86144d" style="zoom: 50%;" />

### 4. 借助MCP Inspector进行功能测试

​	在完成了项目的源码开发后，接下来就可以使用MCP官方提供的Inspector工具进行功能测试了。

- Inspector项目地址：https://github.com/modelcontextprotocol/inspector

  <img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250423171508394.png" alt="image-20250423171508394" style="zoom:50%;" />

这里需要注意的是，由于当前MCP服务器脚本是使用MCP SDK进行的开发，并且MCP服务器的核心功能是为MCP客户端提供服务，因此如果不采用官方提供的Inspector进行debug，就需要自己手写一个MCP client并尝试与MCP server进行通信，才能进行debug。

​	换而言之就是官方提供的Inspector实际上是一个通用的MCP Client，能够测试MCP server实际运行效果。具体debug流程如下：

- Step 1.运行MCP服务器脚本

```bash
# 回到项目主目录
# cd /root/autodl-tmp/MCP/mcp-server-deepresearch

# 运行Inspector
npx -y @modelcontextprotocol/inspector uv run ./src/mcp_server_deepresearch/server.py --openai_api_key YOUR_KEY
```

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250422214216222.png" alt="image-20250422214216222" style="zoom:50%;" />

> 注意此处要输入OpenAI-API-KEY

启动完成后能够看到，此时服务器端口号为6277，而Inspector端口号为6274，如果是在本地运行，则可以直接在浏览器中输入`localhost:6274`进入Inspector页面，而如果是在AutoDL上运行，则需要使用SSH隧道工具，将两个端口号都映射到本地：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250422214308401.png" alt="image-20250422214308401" style="zoom: 25%;" />

然后再在`localhost:6274`进入Inspector页面。

- Step 2.设置Inspector相应时间

​	首次进入Inspector页面时需要设置响应时间，由于当前外部工具运行时间较长，Inspector默认只给出10秒响应窗口，超时未响应则会报错，因此这里需要在Configuration中进行响应时间设置：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250422221143809.png" alt="image-20250422221143809" style="zoom:50%;" />

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250422221229614.png" alt="image-20250422221229614" style="zoom:50%;" />

然后点击Connect即可连接MCP Server。

> 超时响应报错示例：
>
> <img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250422220550413.png" alt="image-20250422220550413" style="zoom:50%;" />

- Step 4.在线运行

​	当连接上MCP Server之后，接下来点击Tools、再点击List Tools，选择deepresearch工具，并在右侧输入问题，例如`你好，我想深入了解下到底什么是MCP（Model Context Protocol）技术`，接下来MCP服务器会开始进行运行：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/1745330605185.jpg" alt="1745330605185" style="zoom:50%;" />

运行后即可得到完整调研报告结果：

<video src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/inspector%E6%BC%94%E7%A4%BA.mp4"></video>

由此即完成了完整的MCP Server脚本debug。接下来即可考虑将项目进行部署上线了。

## 三、MCP服务器部署流程

​	对于MCP服务器来说，一般有两种部署方式，分别是在线发布和离线拷贝运行。

- **MCP服务器在线发布**

  ​	所谓在线发布，指的是我们可以将开发好的MCP服务器打包上传到pypi平台或者npm平台进行云平台托管，一旦上传成功，后续用户即可使用uvx或者npx进行下载和使用。我们在`3. MCP工具标准接入流程`一节中所介绍的各主流MCP客户端接入MCP工具的标准流程，实际上就是实时下载MCP工具，然后在本地进行运行。而各大MCP工具平台，如Smithery，本质上也是在pipy平台或者npm平台上托管的库基础上进行的进一步维护。

  > pipy：https://pypi.org/
  >
  > <img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250423173555112.png" alt="image-20250423173555112" style="zoom:50%;" />
  >
  > npm：https://www.npmjs.com/
  >
  > <img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250423173538149.png" alt="image-20250423173538149" style="zoom:50%;" />

- **MCP服务器离线拷贝运行**

  ​        而所谓的离线部署运行，就好理解的多，指的是将打包好的库直接拷贝到服务器上或者给他人进行使用，没有在云平台托管的这个环节，适合非公开MCP服务器进行部署。

接下来围绕我们创建的DeepResearch MCP服务器，详细介绍这两种部署方法。

### 1. DeepResearch项目完善

​	尽管此前我们已经完成了DeepResearch项目的核心脚本debug，但其仍然不算是一个结构完整的项目。核心脚本的调用关系并不明确，同时项目说明也不够完善。因此这里我们首先需要先完善项目的主体内容，再考虑进行部署或上线发布。

#### 1.1 src layout项目结构

​	其实在此之前，我们将代码都放在src内的某个文件夹里，这种项目结构也被称作src layout项目结构，这是一种非常通用、同时也便于代码维护的项目结构，基本示意图如下：

```pgsql
your-project/
├── src/               ← ✅ 所有业务代码都集中在这里
│   └── your_package/  ← Python 包的实际内容（含 __init__.py）
├── dist/              ← 构建后的分发包（如 wheel）
├── .venv/             ← 虚拟环境（本地依赖隔离）
├── .git/              ← Git 管理
├── pyproject.toml     ← 项目配置
├── README.md          ← 说明文件
├── .python-version    ← Python版本声明
├── .gitignore         ← Git 忽略规则
└── uv.lock            ← uv 的依赖锁文件
```

接下来我们还需要在`src/mcp_server_deepresearch`中创建两个py脚本，其一是`__init__.py`，使当前文件夹可以作为Python的一个库进行导入，需要在`__init__.py`写入如下代码：

```python
from .server import main
```

同时再创建一个`__main__.py`，用于实际执行主函数调用流程：

```python
from mcp_server_deepresearch import main

main()
```

最终`src/mcp_server_deepresearch`中代码文件如下所示：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250423170753513.png" alt="image-20250423170753513" style="zoom:50%;" />

整个项目的脚本文件可以在网盘中领取：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250423171236096.png" alt="image-20250423171236096" style="zoom:50%;" />

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/6920963aa5d94ab50c23e4e8b86144d.png" alt="6920963aa5d94ab50c23e4e8b86144d" style="zoom: 50%;" />

#### 1.2 修改pyproject.toml

​	创建完基本项目结构后，让我们回到当前项目主目录下，删除`main.py`（如果有的话），然后修改项目配置文件`pyproject.toml`:

```toml
[build-system]
requires = ["setuptools>=61.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "mcp-server-deepresearch"
version = "0.1.2"
description = "实现类deepresearch功能的MCP工具"
readme = "README.md"
requires-python = ">=3.10"
dependencies = [
    "asyncio>=3.4.3",
    "mcp>=1.6.0",
    "openai>=1.75.0",
    "openai-agents>=0.0.12",
    "pydantic>=2.11.3",
    "typing>=3.10.0.0",
]

[project.scripts]
mcp-server-deepresearch = "mcp_server_deepresearch:main"

[tool.setuptools]
package-dir = {"" = "src"}

[tool.setuptools.packages.find]
where = ["src"]
```

具体配置解释如下：

 `[build-system]` 段

```toml
[build-system]
requires = ["setuptools>=61.0", "wheel"]
build-backend = "setuptools.build_meta"
```

告诉 Python 构建工具（如 `pip`, `uv`, `build`）：

- 要使用 `setuptools` 来构建项目
- 同时依赖 `wheel`，因为你要构建 `.whl` 包

`[project]` 段

```toml
[project]
name = "mcp-server-deepresearch"
version = "0.1.2"
description = "实现类deepresearch功能的MCP工具"
readme = "README.md"
requires-python = ">=3.10"
dependencies = [
    "asyncio>=3.4.3",
    "mcp>=1.6.0",
    "openai>=1.75.0",
    "openai-agents>=0.0.12",
    "pydantic>=2.11.3",
    "typing>=3.10.0.0",
]
```

定义项目的**元数据**，包括：

- 项目名称、版本、描述
- Python 最低版本要求
- 自动安装的依赖项（相当于 `requirements.txt`）

 `[project.scripts]`：命令行入口

```toml
[project.scripts]
mcp-server-deepresearch = "mcp_server_deepresearch:main"
```

定义一个**可执行命令行脚本**，等价于在终端中直接运行：

```bash
mcp-server-deepresearch --openai_api_key=...
```

它会自动调用你包内的：

```python
mcp_server_deepresearch/main.py 里的 main() 函数
```

也支持：

```python
mcp_server_deepresearch/__init__.py 中的 main() 函数
```

只要是 `main()` 函数即可。

```toml
[tool.setuptools]
package-dir = {"" = "src"}

[tool.setuptools.packages.find]
where = ["src"]
```

明确告诉 setuptools：

- 你的项目源代码都在 `src/` 目录下
- 请去 `src/` 中查找 Python 包（即包含 `__init__.py` 的目录）

| 区块                | 作用                     | 评价                                          |
| ------------------- | ------------------------ | --------------------------------------------- |
| `[build-system]`    | 告诉构建工具如何构建项目 | ✅ 非常规范                                    |
| `[project]`         | 定义项目基本信息和依赖   | ✅ 可以删掉 asyncio 和 typing                  |
| `[project.scripts]` | 定义命令行工具           | ✅ 可直接用 `mcp-server-deepresearch` 命令运行 |
| `[tool.setuptools]` | 指定源码位置             | ✅ 与 src layout 完美配合                      |

然后对整个项目进行打包。首先需要安装打包（和上传）工具：

```bash
uv pip install build twine
```

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250422221754431.png" alt="image-20250422221754431" style="zoom:50%;" />

然后使用如下命令进行打包：

```bash
# 回到项目主目录
# cd /root/autodl-tmp/MCP/mcp-server-deepresearch

# 打包
python -m build
```

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250422221921794.png" alt="image-20250422221921794" style="zoom:50%;" />

打包完成后会在主目录下新增一个dist文件夹：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250422221936383.png" alt="image-20250422221936383" style="zoom:50%;" />

以及在src目录下会创建一个.egg-info文件夹，

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250422221956413.png" alt="image-20250422221956413" style="zoom:50%;" />

这两个文件夹内容解释如下：

-  `dist/` 文件夹：**打包产物目录**，会在 包含如下文件：

| 文件类型       | 说明                                    |
| -------------- | --------------------------------------- |
| `.whl` 文件    | Python wheel 格式的二进制分发包，最常用 |
| `.tar.gz` 文件 | 源代码包（source distribution）         |

而在离线部署时候，别人安装时只要 `pip install xxx.whl` 就可以了（无需源码），同时上传到 PyPI、内网 PyPI、AI 模型平台等地方部署。

- `<project-name>.egg-info/` 文件夹：**元数据文件夹**，这个是 `setuptools` 在构建或打包时生成的一个“项目元信息目录”。比如会看到这样的结构：

```
mcp_server_deepresearch.egg-info/
├── PKG-INFO
├── SOURCES.txt
├── top_level.txt
├── dependency_links.txt
├── requires.txt
```

`PKG-INFO`：你项目的基本信息（名称、版本、作者、依赖等），`requires.txt`：列出依赖项，`SOURCES.txt`：列出所有打包进 `.whl` 的文件，`top_level.txt`：顶层包名（比如 `mcp_server_deepresearch`）。

### 2. 项目离线拷贝

​	接下来继续介绍离线拷贝流程。假设我们现在需要从服务器A上把项目拷贝到服务器B上，最简单的方法首先是在服务器A上进行项目压缩：

```bash
# 回到主目录 
# cd /root/autodl-tmp/MCP/mcp-server-deepresearch
tar --exclude='.venv' -czvf mcp-server-deepresearch.tar.gz *
```

压缩后会创建一个名为mcp-server-deepresearch.tar.gz的文件：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250423175728650.png" alt="image-20250423175728650" style="zoom:50%;" />

将其下载后即可上传到服务器B上，例如将其上传到B服务器的`/root/autodl-tmp/MCP/MCP-Test`路径下：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250423175917550.png" alt="image-20250423175917550" style="zoom:50%;" />

然后即可使用如下命令进行解压缩：

```bash
tar -xzvf mcp-server-deepresearch.tar.gz
```

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250423180010291.png" alt="image-20250423180010291" style="zoom:50%;" />

然后即可激活虚拟环境并相关依赖：

```bash
# 创建虚拟环境
uv venv

# 激活虚拟环境
source .venv/bin/activate

# 使用uv（推荐）或pip安装
uv pip install .
```

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250423180133888.png" alt="image-20250423180133888" style="zoom:33%;" />

然后即可运行Inspector进行测试：

```bash
# 运行Inspector
npx -y @modelcontextprotocol/inspector uv run ./src/mcp_server_deepresearch/server.py --openai_api_key YOUR_KEY
```

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250423180254878.png" alt="image-20250423180254878" style="zoom:33%;" />

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250423180319492.png" alt="image-20250423180319492" style="zoom:50%;" />

完整项目压缩包在网盘中领取：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250423181309531.png" alt="image-20250423181309531" style="zoom:50%;" />

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/6920963aa5d94ab50c23e4e8b86144d.png" alt="6920963aa5d94ab50c23e4e8b86144d" style="zoom: 50%;" />

### 3. 项目发布到pipy平台

​	除了离线拷贝之外，我们也可以把自己开发完成的MCP Server发布到一些托管平台上方便其他人下载使用，如果是js开发的MCP Server可以发布在npm平台上，而如果是Python项目，则可以发布在pypi上。我们这里以pypi发布流程为例进行演示。首先需要先在pypi：https://pypi.org/上进行账号注册，然后获取API-KEY作为身份验证，

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250423181125735.png" alt="image-20250423181125735" style="zoom:50%;" />

然后需要再次确认打包完成，并开启上传

```bash
# 回到项目主目录
# cd /root/autodl-tmp/MCP/mcp-server-deepresearch

# 若此前打包完成，则无需再次打包
# python -m build

# 上传到pypi平台
python -m twine upload dist/*
```

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250422222050363.png" alt="image-20250422222050363" style="zoom:50%;" />

上传完成后即可在pypi中搜索到包的信息：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250422222218490.png" alt="image-20250422222218490" style="zoom:50%;" />

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250422222228719.png" alt="image-20250422222228719" style="zoom:50%;" />

然后即可在本地测试调用。

​	这里以Cherry studio为例，尝试调用我们刚刚发布的DeepResearch包。点击添加服务器：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250422222450471.png" alt="image-20250422222450471" style="zoom:50%;" />

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250422222503228.png" alt="image-20250422222503228" style="zoom:50%;" />

然后输入MCP服务器名称（随意填写），然后使用uvx进行下载，同时是stdio通信标准，并在参数中输入以下三行：

```bash
mcp-server-deepresearch
--openai_api_key
YOUR_API_KEY
```

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250422222838073.png" alt="image-20250422222838073" style="zoom:50%;" />

然后点击右上方保存，即可开启验证并自动开启这项MCP工具。紧接着在对话过程中选择deepresearch工具，只要对话中明确表达了希望围绕某个问题进行深入研究，模型就会自动调用该MCP工具进行深度调研：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250423095959573.png" alt="image-20250423095959573" style="zoom:50%;" />

实际演示效果如下：

<video src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/deepresearch%E6%95%88%E6%9E%9C%E5%B1%95%E7%A4%BA3.mp4"></video>

> 注，如果是离线拷贝的项目希望使用cherry studio进行调用，仅需在配置中写入：
>
> ```bash
> /path/to/your/mcp-server-deepresearch
> --openai_api_key
> YOUR_API_KEY
> ```
>
> 也就是第一行改为离线项目的本地存储地址即可。

> 此外，若是在Cursor中调用，则可以写入如下配置：
>
> ```json
> {
> "mcpServers": {
>  "deepresearch": {
>    "command": "uvx",
>    "args": [
>      "mcp-server-deepresearch",
>      "--openai_api_key",
>      "OPENAI_API_KEY"
>    ]
>  }
> }
> ```

## 四、基于SSE传输方式的MCP服务器创建流程

​	以上MCP服务器都是stdio传输方式，而除此之外，目前MCP服务器还支持SSE传输和基于HTTP的流式传输。这两种传输方式也有非常广泛的实际用途，接下来详细介绍如何构建基于SSE和HTTP流式传输的MCP服务器。

### 1. stdio、SSE与基于HTTP的流式传输形式对比

#### 1.1 MCP通信协议介绍

​	MCP（Model Context Protocol）是一种为了统一大规模模型和工具间通信而设计的协议，它定义了消息格式和通信方式。MCP 协议支持多种传输机制，其中包括 **`stdio`、Server-Sent Events（SSE）** 和 **Streamable HTTP**。每种通信方法在不同的应用场景中具有不同的优劣势，适用于不同的需求。

#### 1.2 **Stdio 传输（Standard Input/Output）**

​	`stdio` 传输方式是最简单的通信方式，通常在本地工具之间进行消息传递时使用。它利用标准输入输出（stdin/stdout）作为数据传输通道，适用于本地进程间的交互。

- **工作方式**：客户端和服务器通过标准输入输出流（stdin/stdout）进行通信。客户端向服务器发送命令和数据，服务器执行并通过标准输出返回结果。
- **应用场景**：适用于本地开发、命令行工具、调试环境，或者模型和工具服务在同一进程内运行的情况。

#### 1.3 **Server-Sent Events（SSE）**

​	SSE 是基于 HTTP 协议的流式传输机制，它允许服务器通过 HTTP 单向推送事件到客户端。SSE 适用于客户端需要接收服务器推送的场景，通常用于实时数据更新。

- **工作方式**：客户端通过 HTTP GET 请求建立与服务器的连接，服务器以流式方式持续向客户端发送数据，客户端通过解析流数据来获取实时信息。

- **应用场景**：适用于需要服务器主动推送数据的场景，如实时聊天、天气预报、新闻更新等。

#### 1.4 **Streamable HTTP**

- MCP更新公告：https://modelcontextprotocol.io/development/updates

  <img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250416155823463.png" alt="image-20250416155823463" style="zoom:50%;" />

- Streamable HTTP协议内容：https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/docs/specification/2025-03-26/basic/transports.mdx#streamable-http

  <img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250416155855631.png" alt="image-20250416155855631" style="zoom:50%;" />

​	Streamable HTTP 是 MCP 协议中新引入的一种传输方式，它基于 HTTP 协议支持双向流式传输。与传统的 HTTP 请求响应模型不同，Streamable HTTP 允许服务器在一个长连接中实时向客户端推送数据，并且可以支持多个请求和响应的流式传输。

​	不过需要注意的是，MCP只提供了Streamable HTTP协议层的支持，也就是规范了MCP客户端在使用Streamable HTTP通信时的通信规则，而并没有提供相关的SDK客户端。开发者在开发Streamable HTTP机制下的客户端和服务器时，可以使用比如Python httpx库进行开发。

- **工作方式**：客户端通过 HTTP POST 向服务器发送请求，并可以接收流式响应（如 JSON-RPC 响应或 SSE 流）。当请求数据较多或需要多次交互时，服务器可以通过长连接和分批推送的方式进行数据传输。

- **应用场景**：适用于需要支持高并发、低延迟通信的分布式系统，尤其是跨服务或跨网络的应用。适合高并发的场景，如实时流媒体、在线游戏、金融交易系统等。

#### 1.1.4 **MCP 传输方式优劣势对比**

| 特性               | **Stdio**                | **SSE**                          | **Streamable HTTP**                |
| ------------------ | ------------------------ | -------------------------------- | ---------------------------------- |
| **通信方向**       | 双向（但仅限本地）       | 单向（服务器到客户端）           | 双向（适用于复杂交互）             |
| **使用场景**       | 本地进程间通信           | 实时数据推送，浏览器支持         | 跨服务、分布式系统、大规模并发支持 |
| **支持并发连接数** | 低                       | 中等                             | 高（适合大规模并发）               |
| **适应性**         | 局限于本地环境           | 支持浏览器，但单向通信           | 高灵活性，支持流式数据与请求批处理 |
| **实现难度**       | 简单，适合本地调试       | 简单，但浏览器兼容性和长连接限制 | 复杂，需处理长连接和流管理         |
| **适合的业务类型** | 本地命令行工具，调试环境 | 实时推送，新闻、股票等实时更新   | 高并发、分布式系统，实时交互系统   |

三种传输方式总结如下：

- **`Stdio` 传输**：适合本地进程之间的简单通信，适合命令行工具或调试阶段，但不支持分布式。
- **`SSE` 传输**：适合实时推送和客户端/浏览器的单向通知，但无法满足双向复杂交互需求。
- **`Streamable HTTP` 传输**：最灵活、最强大的选项，适用于大规模并发、高度交互的分布式应用系统，虽然实现较复杂，但能够处理更复杂的场景。

### 2. 基于SSE传输的MCP服务器创建流程

​	需要注意的是，目前MCP SDK只提供了stdio和SSE两种传输方式的开发库，而暂时还没有提供基于流式HTTP传输的开发工具。因此在进行MCP开发过程中，实现stdio和SSE传输方式较为简单，但要实现流式传输的HTTP流程则会非常复杂。

​	这里我们先介绍相对简单的SSE传输方式的实现方法。当我们使用MCP Python SDK开发MCP服务器时，只需要在此处进行设置：

```python
mcp.run(transport='sse')
```

即可让MCP服务器开启SSE模式，非常简单。这里我们以创建一个查询天气MCP服务器为例进行演示。

- 创建项目主目录

```bash
cd /root/autodl-tmp/MCP
mkdir ./MCP-sse-test
cd ./MCP-sse-test
```

- 创建基础项目结构

```bash
uv init mcp-get-weather
cd mcp-get-weather

# 创建虚拟环境
uv venv

# 激活虚拟环境
source .venv/bin/activate

uv add mcp httpx
```

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250423110303182.png" alt="image-20250423110303182" style="zoom:50%;" />

然后删除主目录下的main.py文件，并创建代码文件夹：

```bash
mkdir -p ./src/mcp_get_weather
cd ./src/mcp_get_weather
```

- 创建服务器核心代码

​	在src/mcp_get_weather中创建三个代码文件：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250423110703450.png" alt="image-20250423110703450" style="zoom:50%;" />

其中server.py主要负责进行天气查询，代码如下：

```python
import json
import httpx
import argparse  
from typing import Any
from mcp.server.fastmcp import FastMCP

# 初始化 MCP 服务器
mcp = FastMCP("WeatherServer")

# OpenWeather API 配置
OPENWEATHER_API_BASE = "https://api.openweathermap.org/data/2.5/weather"
API_KEY = None  
USER_AGENT = "weather-app/1.0"

async def fetch_weather(city: str) -> dict[str, Any] | None:
    """
    从 OpenWeather API 获取天气信息。
    """
    if API_KEY is None:
        return {"error": "API_KEY 未设置，请提供有效的 OpenWeather API Key。"}

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric",
        "lang": "zh_cn"
    }
    headers = {"User-Agent": USER_AGENT}

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(OPENWEATHER_API_BASE, params=params, headers=headers, timeout=30.0)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            return {"error": f"HTTP 错误: {e.response.status_code}"}
        except Exception as e:
            return {"error": f"请求失败: {str(e)}"}

def format_weather(data: dict[str, Any] | str) -> str:
    """
    将天气数据格式化为易读文本。
    """
    if isinstance(data, str):
        try:
            data = json.loads(data)
        except Exception as e:
            return f"无法解析天气数据: {e}"

    if "error" in data:
        return f"⚠️ {data['error']}"

    city = data.get("name", "未知")
    country = data.get("sys", {}).get("country", "未知")
    temp = data.get("main", {}).get("temp", "N/A")
    humidity = data.get("main", {}).get("humidity", "N/A")
    wind_speed = data.get("wind", {}).get("speed", "N/A")
    weather_list = data.get("weather", [{}])
    description = weather_list[0].get("description", "未知")

    return (
        f"🌍 {city}, {country}\n"
        f"🌡 温度: {temp}°C\n"
        f"💧 湿度: {humidity}%\n"
        f"🌬 风速: {wind_speed} m/s\n"
        f"🌤 天气: {description}\n"
    )

@mcp.tool()
async def query_weather(city: str) -> str:
    """
    输入指定城市的英文名称，返回今日天气查询结果。
    """
    data = await fetch_weather(city)
    return format_weather(data)

def main():
    parser = argparse.ArgumentParser(description="Weather Server")
    parser.add_argument("--api_key", type=str, required=True, help="你的 OpenWeather API Key")
    args = parser.parse_args()
    global API_KEY
    API_KEY = args.api_key
    mcp.run(transport='sse')

if __name__ == "__main__":
    main()
```

其仍然是采用了fastmcp进行创建，而在mcp.run中设置了使用sse方式进行传输。

```python
mcp.run(transport='sse')
```

此外需要在`__init__.py`中写入

```python
from .server import main
```

而在`__main__.py`中写入：

```python
from mcp_get_weather import main

main()
```

同时回到主目录，修改项目配置文件`pyproject.toml`：

```toml
[build-system]
requires = ["setuptools>=61.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "mcp-get-weather"
version = "0.1.5"
description = "输入OpenWeather-API-KEY，获取天气信息。"
readme = "README.md"
requires-python = ">=3.9"
dependencies = [
    "httpx>=0.28.1",
    "mcp>=1.6.0",
    "openai>=1.75.0",
    "python-dotenv>=1.1.0",
]

[project.scripts]
mcp-get-weather = "mcp_get_weather:main"

[tool.setuptools]
package-dir = {"" = "src"}

[tool.setuptools.packages.find]
where = ["src"]
```

至此即完成了整个项目的代码编写工作。完整项目代码可在网盘中领取：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250423185709445.png" alt="image-20250423185709445" style="zoom:50%;" />

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/6920963aa5d94ab50c23e4e8b86144d.png" alt="6920963aa5d94ab50c23e4e8b86144d" style="zoom: 50%;" />

### 3. 基于SSE的MCP服务器测试与发布流程

#### 3.1 SSE MCP服务器测试流程

​	同样，接下来可以使用Inspector进行服务器性能测试，但有所不同的是，我们需要先开启MCP服务器，然后再开启Inspector：

> 在stdio模式下是开启Inspector时同步开启MCP Server

- 开启SSE MCP服务器：

  ```bash
  # 回到项目主目录
  # cd /root/autodl-tmp/MCP/MCP-sse-test/mcp-get-weather
  
  uv run ./src/mcp_get_weather/server.py --api_key YOUR_KEY
  ```

  <img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250423111412552.png" alt="image-20250423111412552" style="zoom:50%;" />

- 开启Inspector

  ```bash
  # 回到项目主目录
  # cd /root/autodl-tmp/MCP/MCP-sse-test/mcp-get-weather
  
  npx -y @modelcontextprotocol/inspector uv run ./src/mcp_get_weather/server.py --api_key YOUR_KEY
  ```

  <img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250423110918301.png" alt="image-20250423110918301" style="zoom:50%;" />

- 进行测试

  同样，如果是使用AutoDL，则先需要使用隧道工具将端口映射到本地进行运行：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250423111426277.png" alt="image-20250423111426277" style="zoom: 25%;" />

然后打开Inspector，并选择SSE模式，选择默认运行地址：`http://localhost:8000/sse`，然后点击connect：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250423111502594.png" alt="image-20250423111502594" style="zoom:50%;" />

然后输入地名进行测试：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250423111530795.png" alt="image-20250423111530795" style="zoom:50%;" />

完整测试流程如下：

<video src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/Inspector%E6%BC%94%E7%A4%BA1.mp4"></video>

#### 3.2 SSE MCP服务器发布与调用流程

​	测试完成后，即可上线发布。这里仍然考虑发布到pypi平台，并使用cherry studio进行本地调用测试。

- 打包上传：

```bash
# 回到项目主目录
# cd /root/autodl-tmp/MCP/MCP-sse-test/mcp-get-weather

uv pip install build twine
python -m build
python -m twine upload dist/*
```

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250423112413209.png" alt="image-20250423112413209" style="zoom:50%;" />

- 查看发布的库：https://pypi.org/search/?q=mcp-get-weather

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250423112456668.png" alt="image-20250423112456668" style="zoom:50%;" />

- 本地安装：

```bash
pip install mcp-get-weather
```

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250423112752130.png" alt="image-20250423112752130" style="zoom:50%;" />

- 开启服务：uv run mcp-get-weather

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250423112859366.png" alt="image-20250423112859366" style="zoom:33%;" />

然后即可打开浏览器输入`http://localhost:8000/sse`测试连接情况

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250423120618768.png" alt="image-20250423120618768" style="zoom:50%;" />

> 注意，这里在服务器上开启服务然后本地连接也可以，和stdio不同，SSE模式下的MCP服务器并不需要本地运行。

- 使用Cherry studio进行连接

​	然后即可使用Cherry studio连接SSE模式下的MCP服务器，这里只需要输入服务器地址即可：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250423120352181.png" alt="image-20250423120352181" style="zoom:50%;" />

具体演示效果如下

<video src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/sse%E6%95%88%E6%9E%9C%E6%BC%94%E7%A4%BA.mp4"></video>

至此我们就完成了两个服务器、同时也是两种类型的服务器的开发与部署流程。

## 五、基于HTTP流式传输的MCP服务器创建流程

​	最后一部分，让我们来介绍基于HTTP流式传输的MCP服务器创建流程。需要注意的是，尽管HTTP流式传输是理论上性能最好的传输方式，但开发和应用的门槛都很大，不仅目前MCP SDK没有HTTP流式传输开发工具，而且目前主流的MCP客户端，如Cherry Studio和Cursor等，对于HTTP流式传输的MCP服务器调用支持都很差，因此目前对于MCP来说，HTTP流式传输功能还处于初级阶段。

### 1. HTTP流式传输协议

​	上面谈到，目前MCP的各官方SDK并没有提供HTTP流式传输的MCP开发工具，因此HTTP流式传输的MCP服务器尚且停留在“协议阶段”，也就是说MCP提供了HTTP的传输协议，但没有提供对应能完成相关功能开发的SDK，开发者如果需要创建HTTP流式传输的MCP服务器，则需要先研究MCP HTTP流式传输协议，然后手动创建满足该协议的MCP Server。整体来看研发难度较大。

​	为此，我们首先需要深入研究MCP提出的HTTP流式传输基本协议。整个协议内容较多，这里需要重点关注以下几分材料：

#### 1.1 Streamable HTTP协议简介

- 文档连接：https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/docs/specification/2025-03-26/basic/transports.mdx#streamable-http

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250423191120857.png" alt="image-20250423191120857" style="zoom:50%;" />

其中详细说明了HTTP流式传输的基本协议，也可以通过如下流程进行说明：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/1745407238854.jpg" alt="1745407238854" style="zoom:25%;" />

#### 1.2 HTTP进程生命周期

- 文档地址：https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/docs/specification/2025-03-26/basic/lifecycle.mdx

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250423193650765.png" alt="image-20250423193650765" style="zoom:33%;" />

其中详细介绍了从开始会话到结束的完整服务器生命周期进程，也可以用下图进行展示：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250423193716887.png" alt="image-20250423193716887" style="zoom:50%;" />

#### 1.3 HTTP服务器外部工具调用识别与调用流程

- 文档地址：https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/docs/specification/2025-03-26/server/tools.mdx

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250423193753618.png" alt="image-20250423193753618" style="zoom:50%;" />

其中详细说明了HTTP流式传输服务器与客户端之间的通信流程，以及外部工具信息同步格式与流程等，也可以用下图进行说明：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250423193843946.png" alt="image-20250423193843946" style="zoom:50%;" />

#### 1.4 HTTP流式传输MCP服务器与客户端通信流程

​	下面按 **客户端首次启动 ➜ 成功连到服务器 ➜ 等待用户提问** 这一完整过程，把 **MCP Streamable HTTP 的请求–响应顺序**用时间线列出来，帮助你完全掌握每一步在干什么。

- **启动时： 3 步握手（无用户输入）**

| 时刻  | HTTP          | JSON-RPC `method`           | 作用                                                         | 服务器典型响应                                               |
| ----- | ------------- | --------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **①** | **POST /mcp** | `initialize`                | 协商协议版本 & 能力                                          | `result.protocolVersion` = `2024-11-05``result.capabilities.tools.listChanged` = `true` |
| **②** | **POST /mcp** | `notifications/initialized` | 告诉服务器“我已就绪”（通知 ⇒ 服务器只回 **204 No Content**） | HTTP `204` 无包体                                            |
| **③** | **POST /mcp** | `tools/list`                | 向服务器要工具清单                                           | `result.tools` 数组 + `nextCursor`                           |

- **当用户第一次提问时（模型判断要用工具）**

| 时刻  | HTTP          | JSON-RPC `method`   | 内容要点                                                     |
| ----- | ------------- | ------------------- | ------------------------------------------------------------ |
| **④** | **POST /mcp** | `tools/call`        | `params.name` = `get_weather``params.arguments.city` 或 `location` |
| **⑤** | **流式响应**  | `stream` / `result` | 服务器逐行推送：• 进度 `stream`• 成功 `result.content[]`     |

客户端在收到 **⑤** 的最终 `result` 后，把文本回填到 LLM，LLM 再输出给终端——你就看到天气结果啦。

- **详细顺序（带状态码）**

1. **POST /mcp → 200** `initialize`
2. **POST /mcp → 204** `notifications/initialized`
3. **POST /mcp → 200** `tools/list`
4. ——等待用户——
5. **POST /mcp → 200/stream** `tools/call` （服务器保持连接，逐行推流）
   - JSON 一行 `{"stream": "正在查询…"}…`
   - JSON 一行 `{"result": { "content":[…] }}` → 服务器随后关闭流

> 如果有多次工具调用，步骤 ④ – ⑤ 会重复，每次 `id` 自增。

完整流程总结如下：

| 场景                 | 服务器应当…                                                  |
| -------------------- | ------------------------------------------------------------ |
| **客户端重新连接**   | 再走 ①②③，每轮 `initialize` 会话独立                         |
| **需要分页工具**     | 在 ③ 返回 `nextCursor` ≠ `null`，客户端会继续 `tools/list`   |
| **通知工具列表变更** | 主动 `notifications/tools/list_changed`，客户端再发 `tools/list` 拉新列表 |

> **JSON-RPC** 是一种用 JSON 编写的、结构化的远程调用协议。其基本格式结构如下：
>
> | 类型 | 字段      | 说明                                  |
> | ---- | --------- | ------------------------------------- |
> | 请求 | `jsonrpc` | 固定为 `"2.0"`                        |
> |      | `id`      | 请求编号，用于对应请求与响应          |
> |      | `method`  | 要调用的方法名（比如 `"tools/call"`） |
> |      | `params`  | 方法参数（可以是对象或数组）          |
> | 响应 | `jsonrpc` | 也要写 `"2.0"`                        |
> |      | `id`      | 与请求的 ID 一致                      |
> |      | `result`  | 成功返回值（只需 result）             |
> |      | `error`   | 如果出错则返回 error 对象             |

### 2. HTTP流式传输MCP服务器开发流程

- 创建项目文件：

```bash
cd /root/autodl-tmp/MCP/MCP-sse-test
uv init mcp-weather-http
cd mcp-weather-http

# 创建虚拟环境
uv venv

# 激活虚拟环境
source .venv/bin/activate

uv add mcp httpx fastapi
```

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250423122344329.png" alt="image-20250423122344329" style="zoom:50%;" />

```bash
mkdir -p ./src/mcp_weather_http
cd ./src/mcp_weather_http
```

然后创建`server.py`

![image-20250423194305977](https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250423194305977.png)

并写入如下代码：

```python
"""weather_http_server_v8.py – MCP Streamable HTTP (Cherry‑Studio verified)
==========================================================================
• initialize  → protocolVersion + capabilities(streaming + tools.listChanged)
                + friendly instructions
• notifications/initialized → ignored (204)
• tools/list  → single-page tool registry (get_weather)
• tools/call  → execute get_weather, stream JSON (content[])
• GET → 405 (no SSE stream implemented)
"""

from __future__ import annotations

import argparse
import asyncio
import json
from typing import Any, AsyncIterator

import httpx
from fastapi import FastAPI, Request, Response, status
from fastapi.responses import StreamingResponse

# ---------------------------------------------------------------------------
# Server constants
# ---------------------------------------------------------------------------
SERVER_NAME = "WeatherServer"
SERVER_VERSION = "1.0.0"
PROTOCOL_VERSION = "2024-11-05"  # Cherry Studio current

# ---------------------------------------------------------------------------
# Weather helpers
# ---------------------------------------------------------------------------
OPENWEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"
API_KEY: str | None = None
USER_AGENT = "weather-app/1.0"


async def fetch_weather(city: str) -> dict[str, Any]:
    if not API_KEY:
        return {"error": "API_KEY 未设置，请提供有效的 OpenWeather API Key。"}
    params = {"q": city, "appid": API_KEY, "units": "metric", "lang": "zh_cn"}
    headers = {"User-Agent": USER_AGENT}
    async with httpx.AsyncClient(timeout=30.0) as client:
        try:
            r = await client.get(OPENWEATHER_URL, params=params, headers=headers)
            r.raise_for_status()
            return r.json()
        except httpx.HTTPStatusError as exc:
            return {"error": f"HTTP 错误: {exc.response.status_code}"}
        except Exception as exc:  # noqa: BLE001
            return {"error": f"请求失败: {exc}"}


def format_weather(data: dict[str, Any]) -> str:
    if "error" in data:
        return data["error"]
    city = data.get("name", "未知")
    country = data.get("sys", {}).get("country", "未知")
    temp = data.get("main", {}).get("temp", "N/A")
    humidity = data.get("main", {}).get("humidity", "N/A")
    wind = data.get("wind", {}).get("speed", "N/A")
    desc = data.get("weather", [{}])[0].get("description", "未知")
    return (
        f"🌍 {city}, {country}\n"
        f"🌡 温度: {temp}°C\n"
        f"💧 湿度: {humidity}%\n"
        f"🌬 风速: {wind} m/s\n"
        f"🌤 天气: {desc}"
    )


async def stream_weather(city: str, req_id: int | str) -> AsyncIterator[bytes]:
    # progress chunk
    yield json.dumps({"jsonrpc": "2.0", "id": req_id, "stream": f"查询 {city} 天气中…"}).encode() + b"\n"

    await asyncio.sleep(0.3)
    data = await fetch_weather(city)

    if "error" in data:
        yield json.dumps({"jsonrpc": "2.0", "id": req_id, "error": {"code": -32000, "message": data["error"]}}).encode() + b"\n"
        return

    yield json.dumps({
        "jsonrpc": "2.0", "id": req_id,
        "result": {
            "content": [
                {"type": "text", "text": format_weather(data)}
            ],
            "isError": False
        }
    }).encode() + b"\n"

# ---------------------------------------------------------------------------
# FastAPI app
# ---------------------------------------------------------------------------
app = FastAPI(title="WeatherServer HTTP-Stream v8")

TOOLS_REGISTRY = {
    "tools": [
        {
            "name": "get_weather",
            "description": "用于进行天气信息查询的函数，输入城市英文名称，即可获得当前城市天气信息。",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "city": {
                        "type": "string",
                        "description": "City name, e.g. 'Hangzhou'"
                    }
                },
                "required": ["city"]
            }
        }
    ],
    "nextCursor": None
}


@app.get("/mcp")
async def mcp_initialize_via_get():
    #  GET 请求也执行了 initialize 方法
    return {
        "jsonrpc": "2.0",
        "id": 0,
        "result": {
            "protocolVersion": PROTOCOL_VERSION,
            "capabilities": {
                "streaming": True,
                "tools": {"listChanged": True}
            },
            "serverInfo": {
                "name": SERVER_NAME,
                "version": SERVER_VERSION
            },
            "instructions": "Use the get_weather tool to fetch weather by city name."
        }
    }

@app.post("/mcp")
async def mcp_endpoint(request: Request):
    try:
        body = await request.json()
        # ✅ 打印客户端请求内容
        print("💡 收到请求:", json.dumps(body, ensure_ascii=False, indent=2))
    except Exception:
        return {"jsonrpc": "2.0", "id": None, "error": {"code": -32700, "message": "Parse error"}}

    req_id = body.get("id", 1)
    method = body.get("method")
    
    # ✅ 打印当前方法类型
    print(f"🔧 方法: {method}")
    
    # 0) Ignore initialized notification (no response required)
    if method == "notifications/initialized":
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    # 1) Activation probe (no method)
    if method is None:
        return {"jsonrpc": "2.0", "id": req_id, "result": {"status": "MCP server online."}}

    # 2) initialize
    if method == "initialize":
        return {
            "jsonrpc": "2.0", "id": req_id,
            "result": {
                "protocolVersion": PROTOCOL_VERSION,
                "capabilities": {
                    "streaming": True,
                    "tools": {"listChanged": True}
                },
                "serverInfo": {"name": SERVER_NAME, "version": SERVER_VERSION},
                "instructions": "Use the get_weather tool to fetch weather by city name."
            }
        }

    # 3) tools/list
    if method == "tools/list":
        print(json.dumps(TOOLS_REGISTRY, indent=2, ensure_ascii=False))
        return {"jsonrpc": "2.0", "id": req_id, "result": TOOLS_REGISTRY}

    # 4) tools/call
    if method == "tools/call":
        params = body.get("params", {})
        tool_name = params.get("name")
        args = params.get("arguments", {})

        if tool_name != "get_weather":
            return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32602, "message": "Unknown tool"}}

        city = args.get("city")
        if not city:
            return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32602, "message": "Missing city"}}

        return StreamingResponse(stream_weather(city, req_id), media_type="application/json")

    # 5) unknown method
    return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not found"}}

# ---------------------------------------------------------------------------
# Runner
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(description="Weather MCP HTTP-Stream v8")
    parser.add_argument("--api_key", required=True)
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8000)
    args = parser.parse_args()

    global API_KEY
    API_KEY = args.api_key

    import uvicorn
    uvicorn.run(app, host=args.host, port=args.port, log_level="info")


if __name__ == "__main__":
    main()
```

代码解释如下：总体结构说明

```text
📦 weather_http_server_v8.py
├── 常量定义（协议版本 + OpenWeather 配置）
├── 工具方法（fetch_weather、format_weather、stream_weather）
├── FastAPI 路由
│   ├── GET /mcp  → 可选支持
│   └── POST /mcp → 支持所有 JSON-RPC 调用
└── main()        → 启动 uvicorn 服务器
```

1️⃣ 头部信息（元数据 + 模块引入）

```python
"""weather_http_server_v8.py – MCP Streamable HTTP (Cherry‑Studio verified)
• initialize → 声明 streaming + tools.listChanged 能力
• tools/list → 提供 get_weather 工具
• tools/call → 调用后 stream JSON 数据
• GET → 405 或简单返回信息（支持 Cherry 探测）
"""
```

✔ 简洁明了地说明这个服务符合 Cherry Studio 所支持的 MCP HTTP 协议子集。

2️⃣ 常量定义

```python
SERVER_NAME = "WeatherServer"
SERVER_VERSION = "1.0.0"
PROTOCOL_VERSION = "2024-11-05"  # MCP 规定版本号

OPENWEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"
API_KEY: str | None = None  # 启动时注入
USER_AGENT = "weather-app/1.0"
```

✔ 提前定义版本号、天气接口、全局变量等。

3️⃣ 天气处理逻辑

```python
async def fetch_weather(city: str) -> dict[str, Any]:
```

- 向 OpenWeather API 请求天气数据
- 自动处理错误（比如 key 不对、超时）

```python
def format_weather(data: dict[str, Any]) -> str:
```

- 把原始 JSON 格式化成可读文本 🌤️

```python
async def stream_weather(city: str, req_id: int | str) -> AsyncIterator[bytes]:
```

- 生成器流式返回天气内容（符合 MCP 协议的逐行 JSON）

示例输出：

```json
{"jsonrpc": "2.0", "id": 1, "stream": "查询 Hangzhou 天气中…"}
{"jsonrpc": "2.0", "id": 1, "result": { "content": [{"type":"text","text":"🌡 温度: 22°C"}] }}
```

4️⃣ MCP 工具注册表

```python
TOOLS_REGISTRY = {
  "tools": [
    {
      "name": "get_weather",
      "description": "...",
      "inputSchema": {
        "type": "object",
        "properties": {
          "city": {
            "type": "string",
            "description": "City name, e.g. 'Hangzhou'"
          }
        },
        "required": ["city"]
      }
    }
  ],
  "nextCursor": None
}
```

✔ 符合 MCP 2025-03-26 文档对 `tools/list` 的格式要求。

5️⃣ 核心路由逻辑（FastAPI）

✔ `/mcp [GET]`

```python
@app.get("/mcp")
```

- Cherry Studio 在探测时会发 GET 请求
- 我们这里返回一个 `initialize` 风格的响应

✔ `/mcp [POST]`

```python
@app.post("/mcp")
async def mcp_endpoint(request: Request):
```

整个 MCP 协议的核心路由！

| JSON-RPC 方法               | 说明                   |
| --------------------------- | ---------------------- |
| `initialize`                | 返回协议版本、能力列表 |
| `notifications/initialized` | 无需响应（204）        |
| `tools/list`                | 返回工具清单           |
| `tools/call`                | 开始天气查询（流式）   |
| 未知 method                 | 返回 `-32601` 错误     |

6️⃣main() 启动逻辑

```python
def main():
    parser.add_argument("--api_key", required=True)
    uvicorn.run(app, host=..., port=...)
```

✔ 从命令行传入 OpenWeather 的 API Key 并启动服务。

```bash
uv run ./server.py --api_key 你的key
```

### 3. HTTP流式传输MCP服务器开启与测试

​	在创建完`server.py`后，我们可以开启服务并进行测试。需要注意的是，Inspector并不支持流式传输的MCP服务器测试，我们只能基于对HTTP流式传输的协议理解，创建一个测试流程。

- 开启HTTP流式传输服务器

  ```bash
  # 回到项目主目录
  # cd /root/autodl-tmp/MCP/MCP-sse-test/mcp-weather-http
  uv run ./src/mcp_weather_http/server.py --api_key YOUR_API_KEY
  ```

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250423194917232.png" alt="image-20250423194917232" style="zoom:50%;" />

接下来我们通过 **4 个 `curl` 命令**来模拟 MCP 客户端与服务器的标准通信流程。

- ① `initialize` 请求（能力协商）

```bash
curl -X POST http://localhost:8000/mcp \
  -H "Content-Type: application/json" \
  -d '{
        "jsonrpc": "2.0",
        "id": 1,
        "method": "initialize",
        "params": {
          "protocolVersion": "2024-11-05"
        }
      }'
```

期望响应：返回服务器支持的协议版本、功能：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250423195102648.png" alt="image-20250423195102648" style="zoom:50%;" />

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250423195018016.png" alt="image-20250423195018016" style="zoom:50%;" />

- ② `notifications/initialized` 通知（确认上线）

```bash
curl -X POST http://localhost:8000/mcp \
  -H "Content-Type: application/json" \
  -d '{
        "jsonrpc": "2.0",
        "method": "notifications/initialized"
      }'
```

📥 期望响应：`204 No Content`（因为是通知类型）：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250423195113826.png" alt="image-20250423195113826" style="zoom:50%;" />

- ③ `tools/list` 请求（获取工具注册表）

```bash
curl -X POST http://localhost:8000/mcp \
  -H "Content-Type: application/json" \
  -d '{
        "jsonrpc": "2.0",
        "id": 2,
        "method": "tools/list",
        "params": {}
      }'
```

📥 期望响应：返回工具清单， `get_weather` 工具的结构体和 schema：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250423195204959.png" alt="image-20250423195204959" style="zoom:50%;" />

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250423195147212.png" alt="image-20250423195147212" style="zoom:50%;" />

- ④ `tools/call` 请求（调用实际工具，流式返回）

```bash
curl -N -X POST http://localhost:8000/mcp \
  -H "Content-Type: application/json" \
  -d '{
        "jsonrpc": "2.0",
        "id": 3,
        "method": "tools/call",
        "params": {
          "name": "get_weather",
          "arguments": {
            "city": "Hangzhou"
          }
        }
      }'
```

📥 期望响应（逐行输出）：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250423195245966.png" alt="image-20250423195245966" style="zoom:50%;" />

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250423195238084.png" alt="image-20250423195238084" style="zoom:50%;" />

脚本完整代码：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250423195417206.png" alt="image-20250423195417206" style="zoom:50%;" />

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/6920963aa5d94ab50c23e4e8b86144d.png" alt="6920963aa5d94ab50c23e4e8b86144d" style="zoom: 50%;" />

### 4. HTTP流式传输MCP服务器Cherry Studio调用测试

​	在基本测试完HTTP流式传输MCP服务器基本功能后，接下来即可接入MCP进行测试。需要注意的是，目前Cherry Studio版本更新迭代较快，部分情况下尚无法稳定支持HTTP流式传输MCP服务器的调用，因此以下流程不一定能顺利完成。若以下流程无法顺利完成，可以看下一节自定义MCP HTTP流式传输客户端进行调用测试。

- 工具名称：weather-http
- URL：http://localhost:8000/mcp
- 请求头：Content-Type=application/json

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250423195846461.png" alt="image-20250423195846461" style="zoom:50%;" />

具体演示效果如下：

<video src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/http%E6%B5%81%E5%BC%8F%E4%BC%A0%E8%BE%93%E6%BC%94%E7%A4%BA.mp4"></video>

### 5. 自定义MCP客户端Client接入HTTP流式传输MCP服务器

​	截止目前，主流的MCP客户端都无法很好的完成HTTP流式MCP服务器的接入，因此这里为大家介绍如何从零编写MCP客户端，并按照标准流程接入HTTP流式MCP服务器。

#### 5.1 编写client.py脚本

```bash
# 回到代码文件夹
cd /root/autodl-tmp/MCP/MCP-sse-test/mcp-weather-http/src/mcp_weather_http
```

创建`client.py`：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250423200139631.png" alt="image-20250423200139631" style="zoom:33%;" />

然后写入如下代码：

```python
"""mcp_http_client.py – Async MCP client (Streamable HTTP)
===========================================================
• 完全移除 stdio 传输，改用 Streamable HTTP (POST + optional SSE)
• 支持 initialize → notifications/initialized → tools/list → tools/call
• 自动处理 line‑delimited JSON stream (application/json 或 text/event-stream)
• 保留交互式 chat_loop，兼容 OpenAI Function Calling
"""

from __future__ import annotations

import asyncio
import json
import logging
import os
from contextlib import AsyncExitStack
from typing import Any, Dict, List, Optional

import httpx
from dotenv import load_dotenv
from openai import OpenAI

################################################################################
# 通用配置加载
################################################################################

class Configuration:
    def __init__(self) -> None:
        load_dotenv()
        self.api_key = os.getenv("LLM_API_KEY")
        self.base_url = os.getenv("BASE_URL")
        self.model = os.getenv("MODEL", "gpt-4o")
        if not self.api_key:
            raise ValueError("❌ 未找到 LLM_API_KEY，请在 .env 文件中配置")

    @staticmethod
    def load_config(path: str) -> Dict[str, Any]:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

################################################################################
# HTTP‑based MCP Server wrapper
################################################################################

class HTTPMCPServer:
    """与单个 MCP Streamable HTTP 服务器通信"""

    def __init__(self, name: str, endpoint: str) -> None:
        self.name = name
        self.endpoint = endpoint.rstrip("/")  # e.g. http://localhost:8000/mcp
        self.session: Optional[httpx.AsyncClient] = None
        self.protocol_version: str = "2024-11-05"

    async def initialize(self) -> None:
        self.session = httpx.AsyncClient(timeout=httpx.Timeout(30.0))
        # 1) initialize
        init_req = {
            "jsonrpc": "2.0",
            "id": 0,
            "method": "initialize",
            "params": {
                "protocolVersion": self.protocol_version,
                "capabilities": {},
                "clientInfo": {"name": "HTTP-MCP-Demo", "version": "0.1"},
            },
        }
        r = await self._post_json(init_req)
        if "error" in r:
            raise RuntimeError(f"Initialize error: {r['error']}")
        # 2) send initialized notification (no response expected)
        await self._post_json({"jsonrpc": "2.0", "method": "notifications/initialized"})

    async def list_tools(self) -> List[Dict[str, Any]]:
        req = {"jsonrpc": "2.0", "id": 1, "method": "tools/list", "params": {}}
        res = await self._post_json(req)
        return res["result"]["tools"]

    async def call_tool_stream(self, tool_name: str, arguments: Dict[str, Any]) -> str:
        """调用工具并将流式结果拼接为完整文本"""
        req = {
            "jsonrpc": "2.0",
            "id": 3,
            "method": "tools/call",
            "params": {"name": tool_name, "arguments": arguments},
        }
        assert self.session is not None
        async with self.session.stream(
            "POST", self.endpoint, json=req, headers={"Accept": "application/json"}
        ) as resp:
            if resp.status_code != 200:
                raise RuntimeError(f"HTTP {resp.status_code}")
            collected_text: List[str] = []
            async for line in resp.aiter_lines():
                if not line:
                    continue
                chunk = json.loads(line)
                if "stream" in chunk:
                    continue  # 中间进度
                if "error" in chunk:
                    raise RuntimeError(chunk["error"]["message"])
                if "result" in chunk:
                    # 根据协议，文本在 result.content[0].text
                    for item in chunk["result"]["content"]:
                        if item["type"] == "text":
                            collected_text.append(item["text"])
            return "\n".join(collected_text)

    async def _post_json(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        assert self.session is not None
        r = await self.session.post(self.endpoint, json=payload, headers={"Accept": "application/json"})
        if r.status_code == 204 or not r.content:
            return {}          # ← 通知无响应体
        r.raise_for_status()
        return r.json()

    async def close(self) -> None:
        if self.session:
            await self.session.aclose()
            self.session = None

################################################################################
# LLM 封装（OpenAI Function‑Calling）
################################################################################

class LLMClient:
    def __init__(self, api_key: str, base_url: Optional[str], model: str) -> None:
        self.client = OpenAI(api_key=api_key, base_url=base_url)
        self.model = model

    def chat(self, messages: List[Dict[str, Any]], tools: Optional[List[Dict[str, Any]]]):
        return self.client.chat.completions.create(model=self.model, messages=messages, tools=tools)

################################################################################
# 多服务器 MCP + LLM Function Calling
################################################################################

class MultiHTTPMCPClient:
    def __init__(self, servers_conf: Dict[str, Any], api_key: str, base_url: Optional[str], model: str) -> None:
        self.servers: Dict[str, HTTPMCPServer] = {
            name: HTTPMCPServer(name, cfg["endpoint"]) for name, cfg in servers_conf.items()
        }
        self.llm = LLMClient(api_key, base_url, model)
        self.all_tools: List[Dict[str, Any]] = []  # 转为 OAI FC 的 tools 数组

    async def start(self):
        for srv in self.servers.values():
            await srv.initialize()
            tools = await srv.list_tools()
            for t in tools:
                # 重命名以区分不同服务器
                full_name = f"{srv.name}_{t['name']}"
                self.all_tools.append({
                    "type": "function",
                    "function": {
                        "name": full_name,
                        "description": t["description"],
                        "parameters": t["inputSchema"],
                    },
                })
        logging.info("已连接服务器并汇总工具：%s", [t["function"]["name"] for t in self.all_tools])

    async def call_local_tool(self, full_name: str, args: Dict[str, Any]) -> str:
        srv_name, tool_name = full_name.split("_", 1)
        srv = self.servers[srv_name]
        # 兼容 city/location
        city = args.get("city") or args.get("location")
        if not city:
            raise ValueError("Missing city/location")
        return await srv.call_tool_stream(tool_name, {"city": city})

    async def chat_loop(self):
        print("🤖 HTTP MCP + Function Calling 客户端已启动，输入 quit 退出")
        messages: List[Dict[str, Any]] = []
        while True:
            user = input("你: ").strip()
            if user.lower() == "quit":
                break
            messages.append({"role": "user", "content": user})
            # 1st LLM call
            resp = self.llm.chat(messages, self.all_tools)
            choice = resp.choices[0]
            if choice.finish_reason == "tool_calls":
                tc = choice.message.tool_calls[0]
                tool_name = tc.function.name
                tool_args = json.loads(tc.function.arguments)
                print(f"[调用工具] {tool_name} → {tool_args}")
                tool_resp = await self.call_local_tool(tool_name, tool_args)
                messages.append(choice.message.model_dump())
                messages.append({"role": "tool", "content": tool_resp, "tool_call_id": tc.id})
                resp2 = self.llm.chat(messages, self.all_tools)
                print("AI:", resp2.choices[0].message.content)
                messages.append(resp2.choices[0].message.model_dump())
            else:
                print("AI:", choice.message.content)
                messages.append(choice.message.model_dump())

    async def close(self):
        for s in self.servers.values():
            await s.close()

################################################################################
# main entry
################################################################################

async def main():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
    conf = Configuration()
    servers_conf = conf.load_config("./src/mcp_weather_http/servers_config.json").get("mcpServers", {})
    client = MultiHTTPMCPClient(servers_conf, conf.api_key, conf.base_url, conf.model)
    try:
        await client.start()
        await client.chat_loop()
    finally:
        await client.close()

if __name__ == "__main__":
    asyncio.run(main())
```

具体代码解释如下：模块结构概览

```text
mcp_http_client.py
├── Configuration         # 读取 API Key 和服务器配置
├── HTTPMCPServer         # 单个 HTTP-MCP 服务器的连接逻辑
├── LLMClient             # OpenAI Function Calling 包装器
├── MultiHTTPMCPClient    # 多服务器协调 + 聊天交互循环
└── main()                # 启动入口
```

1️⃣ `Configuration`：环境变量和 JSON 配置加载器

```python
class Configuration:
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv("LLM_API_KEY")
        self.base_url = os.getenv("BASE_URL")
        self.model = os.getenv("MODEL", "gpt-4o")
```

✔ 支持从 `.env` 中加载 API key，并读取 `servers_config.json` 来配置 MCP 服务器：

```json
{
  "mcpServers": {
    "weather": {
      "endpoint": "http://localhost:8000/mcp"
    }
  }
}
```

2️⃣ `HTTPMCPServer`：与单个 MCP 服务器交互

这是每个 MCP 工具服务器的**小助手**，支持四个核心操作：

✔ 初始化 handshake（初始化 → 初始化通知）

```python
await self._post_json({
  "method": "initialize",
  "params": {"protocolVersion": "2024-11-05", ...}
})
await self._post_json({
  "method": "notifications/initialized"
})
```

服务器返回支持的功能后，客户端表示“准备好了”。

✔ 获取工具列表

```python
await self._post_json({
  "method": "tools/list",
  "params": {}
})
```

返回所有支持的工具定义，包括 name、description、inputSchema。

✔ 工具调用（流式读取）

```python
async def call_tool_stream(...)
```

使用 `httpx.stream(...)` 开始调用，逐行 `aiter_lines()` 读取服务器响应。

- 跳过 `"stream"` 字段
- 捕获 `"result"` → 拼接成文本
- 抛出 `"error"` → 报错提示

例如天气服务会逐行返回：

```json
{"stream": "正在查询"}
{"result": {"content": [{"type":"text", "text":"🌤 杭州"}]}}
```

✔ `_post_json` 方法

自动处理：

- `204 No Content` → 返回空 `{}`，用于通知类方法
- 非 `200` → 报错提示
- 返回 JSON 内容体

3️⃣ `LLMClient`：OpenAI 对话接口（支持 tools 参数）

```python
def chat(self, messages, tools):
    return self.client.chat.completions.create(...)
```

传入历史消息 + tools，自动处理工具调用的交互。

4️⃣ `MultiHTTPMCPClient`：协调多个服务器 + 交互流程

✔ `start()` 初始化阶段

```python
await server.initialize()
tools = await server.list_tools()
```

- 汇总所有 MCP 工具，转为 OpenAI 的 Function Calling 格式
- 工具名改成 `weather_get_weather` 这样的组合

✔ `chat_loop()`：交互主循环

```text
你: 请告诉我杭州的天气
🤖 AI → 推理 → 返回 tool_call
🔁 调用 MCP 工具 → 获取流式响应
📩 把结果送回 LLM → 输出最终结果
```

- 支持多轮对话
- 自动识别是否需要调用工具
- 自动处理工具参数解析和调用逻辑

client亮点总结：

| 特性                        | 说明                                        |
| --------------------------- | ------------------------------------------- |
| ✅ 完全异步                  | 使用 `asyncio + httpx.AsyncClient` 保证性能 |
| ✅ 支持流式工具调用          | 与流式 HTTP 工具无缝配合                    |
| ✅ 支持多服务器              | 可以一次连多个 MCP 服务，拼接统一工具列表   |
| ✅ 支持 LLM Function Calling | 与 `gpt-4-turbo`、`gpt-4o` 等模型深度集成   |
| ✅ 支持容错和错误处理        | 连接失败、调用错误都有明确提示              |

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250423201452398.png" alt="image-20250423201452398" style="zoom:50%;" />

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/6920963aa5d94ab50c23e4e8b86144d.png" alt="6920963aa5d94ab50c23e4e8b86144d" style="zoom: 50%;" />

#### 5.2 创建.env和servers_config.json文件

​	然后在src文件夹内创建.env文件，并写入如下内容：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250423200754323.png" alt="image-20250423200754323" style="zoom:50%;" />

- BASE_URL=“大模型请求地址”
- MODEL=“模型名称”
- LLM_API_KEY=“API-KEY”

然后创建`servers_config.json`，用于记录HTTP流式传输服务器地址，例如：

```json
{
  "mcpServers": {
    "weather": {
      "endpoint": "http://127.0.0.1:8000/mcp"
    }
  }
}
```

#### 5.3 借助自定义client接入流式HTTP MCP服务器

- 开启流式HTTP MCP服务器

  ```bash
  uv run ./src/mcp_weather_http/server.py --api_key YOUR_API_KRI
  ```

  <img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250423200426456.png" alt="image-20250423200426456" style="zoom:50%;" />

- 运行client.py脚本

  ```bash
  # 回到项目主目录
  # cd /root/autodl-tmp/MCP/MCP-sse-test/mcp-weather-http
  
  uv run ./src/mcp_weather_http/client.py
  ```

- 尝试进行问答

  `你好，好久不见`

  `请问北京今天天气如何？`

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250423192945686.png" alt="image-20250423192945686" style="zoom:50%;" />

- 观察HTTP流式传输服务器端运行效果

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250423193118931.png" alt="image-20250423193118931" style="zoom:50%;" />

# 流式HTTP MCP服务器开发指南

​	长期以来，MCP工具的异地通信主要是以SSE传输方式为主，这种通信方法既没有多通道并发同时也不够稳定，很难真正的适用于企业级应用场景。因此，在2月初，在MCP官方GitHub项目主页上，就有开发者提出了采用更先进的流式HTTP传输方法代替SSE传输的技术方案，相比SSE传输，HTTP流式传输并发更高、通信更加稳定，同时也更容易集成和部署，这也是当代服务器与客户端异地通信的最佳解决方案。

![image-20250509202014713](https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250509202014713.png)

但流式HTTP MCP服务器功能复杂，相关SDK的研发难度也很高，因此在今年的3月，MCP官方首先发布了MCP的流式HTTP通信协议，其中详细说明了HTTP流式传输的基本协议。

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250423191120857.png" alt="image-20250423191120857" style="zoom:50%;" />

> https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/docs/specification/2025-03-26/basic/transports.mdx#streamable-http

​	然后在5月9号的1.8.0版本更新中，正式在SDK中加入了HTTP流式MCP服务器的相关功能支持。自此开发者就可以通过MCP SDK，高效快速开发流式HTTP MCP服务器，并顺利进行多通道并发的企业级MCP工具部署。毫无疑问，这将是MCP技术迈向企业级应用的至关重要的一步。

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250509202619324.png" alt="image-20250509202619324" style="zoom:50%;" />

> https://github.com/modelcontextprotocol/python-sdk/releases/tag/v1.8.0

本期公开课，就为大家从零介绍流式HTTP MCP服务器开发、测试、部署上线的全流程，并提供完整MCP服务器功能测试客户端脚本。公开课完整课件扫码即可领取。

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/fc27255105929007628d2838ed07629.png" alt="fc27255105929007628d2838ed07629" style="zoom:50%;" />

## 一、基于HTTP流式传输的MCP服务器开发流程

- 创建项目文件：

```bash
# cd /root/autodl-tmp/MCP
uv init mcp-weather-http
cd mcp-weather-http

# 创建虚拟环境
uv venv

# 激活虚拟环境
source .venv/bin/activate

uv add mcp httpx
```

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250509203414111.png" alt="image-20250509203414111" style="zoom:50%;" />

这里我们采用src_layer的风格进行项目文件编排，因此需要删除main.py，并创建mcp_weather_http目录。

```bash
mkdir -p ./src/mcp_weather_http
cd ./src/mcp_weather_http
```

然后创建在src/mcp_weather_http中创建三个代码文件：

![image-20250509203755085](https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250509203755085.png)

并在`__init__.py`中写入

```python
from .server import main
```

而在`__main__.py`中写入：

```python
from mcp_weather_http import main

main()
```

然后在`server.py`中写入如下代码：

```python
import contextlib
import logging
import os
from collections.abc import AsyncIterator

import anyio
import click
import httpx
import mcp.types as types
from mcp.server.lowlevel import Server
from mcp.server.streamable_http_manager import StreamableHTTPSessionManager
from starlette.applications import Starlette
from starlette.routing import Mount
from starlette.types import Receive, Scope, Send

# ---------------------------------------------------------------------------
# Weather helpers
# ---------------------------------------------------------------------------
OPENWEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"
DEFAULT_UNITS = "metric"  # use Celsius by default
DEFAULT_LANG = "zh_cn"  # Chinese descriptions


async def fetch_weather(city: str, api_key: str) -> dict[str, str]:
    """Call OpenWeather API and return a simplified weather dict.

    Raises:
        httpx.HTTPStatusError: if the response has a non-2xx status.
    """
    params = {
        "q": city,
        "appid": api_key,
        "units": DEFAULT_UNITS,
        "lang": DEFAULT_LANG,
    }
    async with httpx.AsyncClient(timeout=10) as client:
        r = await client.get(OPENWEATHER_URL, params=params)
        r.raise_for_status()
        data = r.json()
    # Extract a concise summary
    weather_main = data["weather"][0]["main"]
    description = data["weather"][0]["description"]
    temp = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    humidity = data["main"]["humidity"]
    return {
        "city": city,
        "weather": weather_main,
        "description": description,
        "temp": f"{temp}°C",
        "feels_like": f"{feels_like}°C",
        "humidity": f"{humidity}%",
    }


@click.command()
@click.option("--port", default=3000, help="Port to listen on for HTTP")
@click.option(
    "--api-key",
    envvar="OPENWEATHER_API_KEY",
    required=True,
    help="OpenWeather API key (or set OPENWEATHER_API_KEY env var)",
)
@click.option(
    "--log-level",
    default="INFO",
    help="Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)",
)
@click.option(
    "--json-response",
    is_flag=True,
    default=False,
    help="Enable JSON responses instead of SSE streams",
)
def main(port: int, api_key: str, log_level: str, json_response: bool) -> int:
    """Run an MCP weather server using Streamable HTTP transport."""

    # ---------------------- Configure logging ----------------------
    logging.basicConfig(
        level=getattr(logging, log_level.upper()),
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )
    logger = logging.getLogger("weather-server")

    # ---------------------- Create MCP Server ----------------------
    app = Server("mcp-streamable-http-weather")

    # ---------------------- Tool implementation -------------------
    @app.call_tool()
    async def call_tool(name: str, arguments: dict) -> list[types.TextContent]:
        """Handle the 'get-weather' tool call."""
        ctx = app.request_context
        city = arguments.get("location")
        if not city:
            raise ValueError("'location' is required in arguments")

        # Send an initial log message so the client sees streaming early.
        await ctx.session.send_log_message(
            level="info",
            data=f"Fetching weather for {city}…",
            logger="weather",
            related_request_id=ctx.request_id,
        )

        try:
            weather = await fetch_weather(city, api_key)
        except Exception as err:
            # Stream the error to the client and re-raise so MCP returns error.
            await ctx.session.send_log_message(
                level="error",
                data=str(err),
                logger="weather",
                related_request_id=ctx.request_id,
            )
            raise

        # Stream a success notification (optional)
        await ctx.session.send_log_message(
            level="info",
            data="Weather data fetched successfully!",
            logger="weather",
            related_request_id=ctx.request_id,
        )

        # Compose human-readable summary for the final return value.
        summary = (
            f"{weather['city']}：{weather['description']}，温度 {weather['temp']}，"
            f"体感 {weather['feels_like']}，湿度 {weather['humidity']}。"
        )

        return [
            types.TextContent(type="text", text=summary),
        ]

    # ---------------------- Tool registry -------------------------
    @app.list_tools()
    async def list_tools() -> list[types.Tool]:
        """Expose available tools to the LLM."""
        return [
            types.Tool(
                name="get-weather",
                description="查询指定城市的实时天气（OpenWeather 数据）",
                inputSchema={
                    "type": "object",
                    "required": ["location"],
                    "properties": {
                        "location": {
                            "type": "string",
                            "description": "城市的英文名称，如 'Beijing'",
                        }
                    },
                },
            )
        ]

    # ---------------------- Session manager -----------------------
    session_manager = StreamableHTTPSessionManager(
        app=app,
        event_store=None,  # 无状态；不保存历史事件
        json_response=json_response,
        stateless=True,
    )

    async def handle_streamable_http(scope: Scope, receive: Receive, send: Send) -> None:  # noqa: D401,E501
        await session_manager.handle_request(scope, receive, send)

    # ---------------------- Lifespan Management --------------------
    @contextlib.asynccontextmanager
    async def lifespan(app: Starlette) -> AsyncIterator[None]:
        async with session_manager.run():
            logger.info("Weather MCP server started! 🚀")
            try:
                yield
            finally:
                logger.info("Weather MCP server shutting down…")

    # ---------------------- ASGI app + Uvicorn ---------------------
    starlette_app = Starlette(
        debug=False,
        routes=[Mount("/mcp", app=handle_streamable_http)],
        lifespan=lifespan,
    )

    import uvicorn

    uvicorn.run(starlette_app, host="0.0.0.0", port=port)

    return 0


if __name__ == "__main__":
    main()
```

代码解释如下：

1. **引入各种功能模块**

```python
import contextlib
import logging
import os
from collections.abc import AsyncIterator

import anyio
import click
import httpx
import mcp.types as types
from mcp.server.lowlevel import Server
from mcp.server.streamable_http_manager import StreamableHTTPSessionManager
from starlette.applications import Starlette
from starlette.routing import Mount
from starlette.types import Receive, Scope, Send
```

💡**解释**：

- 这些都是“工具箱”，你可以理解为在写一个天气小程序之前，先导入一些现成的功能组件：
  - `httpx`: 用来联网查天气。
  - `mcp`: 提供了让大模型调用工具的能力。
  - `starlette`: 帮你搭建 HTTP 网络服务。
  - `click`: 帮你写命令行参数，比如 `--api-key=xxx`。
  - 其它模块则帮助你处理异步任务、打印日志、读取环境变量等。

2. **查询天气的函数**

```python
async def fetch_weather(city: str, api_key: str) -> dict[str, str]:
```

💡**解释**：

- 这个函数是你天气服务器的**核心功能**——根据城市名去 [OpenWeather](https://openweathermap.org/) 网站查询天气。
- 它用 `httpx.AsyncClient` 这个工具联网发请求，返回的结果包括：天气情况、气温、湿度等等。

3. **启动服务器的主函数 `main()`**

```python
@click.command()
@click.option("--port", default=3000, ...)
@click.option("--api-key", envvar="OPENWEATHER_API_KEY", ...)
def main(port, api_key, ...):
```

💡**解释**：

- 这是你运行服务器的“入口”，你以后运行时只需要：

  ```bash
  python weather_mcp_streamable_http_server.py --port 3000 --api-key xxxx
  ```

- `click` 是个很好用的命令行工具，帮你接收参数；

- `api_key` 可以通过环境变量设置，方便又安全。

4. MCP工具注册：让大模型能调用 `get-weather`

```python
@app.call_tool()
async def call_tool(name: str, arguments: dict):
```

💡**解释**：

- 这就是你注册给大语言模型用的“工具”，名字叫 `get-weather`。
- 当模型说“我需要查北京的天气”，MCP就会触发这个函数。
- 你在里面解析出 `"location"` 字段，然后调用上面那个 `fetch_weather()` 函数拿数据。

它还有一个 **亮点功能**：会实时往客户端推送消息：

```python
await ctx.session.send_log_message(...)
```

这些就是所谓的 **“流式日志通知”**（比如“正在查询…”、“成功了！”）。

5. **MCP告诉模型有哪些工具（工具列表）**

```python
@app.list_tools()
async def list_tools() -> list[types.Tool]:
```

💡**解释**：

- MCP 会定期问你：“你这里都有哪些工具可以用？”

- 你就返回一个叫 `get-weather` 的工具描述，告诉模型：

  > 输入需要一个 location，是城市名。

6. **流式会话管理器配置**

```python
session_manager = StreamableHTTPSessionManager(
    app=app,
    event_store=None,
    json_response=json_response,
    stateless=True,
)
```

💡**解释**：

- 这一句创建了 MCP 的“HTTP 会话处理中心”，负责处理所有 `/mcp` 路由的请求；
- `stateless=True` 表示**不保存历史对话**，每次都是新请求；
- `json_response=False` 表示用流式 SSE（你也可以改成一次性 JSON 响应）。

7. **构建 Starlette Web 应用**

```python
starlette_app = Starlette(
    routes=[Mount("/mcp", app=handle_streamable_http)],
    lifespan=lifespan,
)
```

💡**解释**：

- 这是将 MCP 服务挂载到你的网站 `/mcp` 路径上；
- 用户访问这个路径时，就会进入刚才创建的 MCP 会话管理器。

  8. **启动服务器**

```python
import uvicorn
uvicorn.run(starlette_app, host="0.0.0.0", port=port)
```

💡**解释**：

- 这行代码启动你的 MCP HTTP 服务器，监听指定端口；

- 如果你传的是 `--port 3000`，访问路径就是：

  ```
  http://localhost:3000/mcp
  ```

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250509204604818.png" alt="image-20250509204604818" style="zoom:50%;" />

同时需要回到主目录，修改项目配置文件`pyproject.toml`：

```toml
[build-system]
requires = ["setuptools>=61.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "mcp-weather-http"
version = "1.1.0"
description = "输入OpenWeather-API-KEY，获取天气信息。"
readme = "README.md"
requires-python = ">=3.10"
dependencies = [
    "httpx>=0.28.1",
    "mcp>=1.8.0",
]

[project.scripts]
mcp-weather-http = "mcp_weather_http:main"

[tool.setuptools]
package-dir = {"" = "src"}

[tool.setuptools.packages.find]
where = ["src"]
```

至此即完成了整个项目的代码编写工作。完整项目代码可在网盘中领取：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250509221528958.png" alt="image-20250509221528958" style="zoom:50%;" />

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/f0d53f9690c8c46b5e075fe8a0284af.jpg" alt="f0d53f9690c8c46b5e075fe8a0284af" style="zoom:50%;" />

## 二、HTTP流式传输MCP服务器开启与测试

​	在创建完`server.py`后，我们可以开启服务并进行测试。需要注意的是，我们需要先开启流式HTTP MCP服务器，然后再开启Inspector：

> 在stdio模式下是开启Inspector时同步开启MCP Server

- 开启流式HTTP MCP服务器：

  ```bash
  # 回到项目主目录
  # cd /root/autodl-tmp/MCP/mcp-weather-http
  
  uv run ./src/mcp_weather_http/server.py --api-key YOUR_KEY
  ```

  <img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250509204635032.png" alt="image-20250509204635032" style="zoom:50%;" />

- 开启Inspector

  ```bash
  # 回到项目主目录
  # cd /root/autodl-tmp/MCP/mcp-weather-http
  # source .venv/bin/activate
  
  npx -y @modelcontextprotocol/inspector uv run main.py --api-key YOUR_KEY
  ```

  <img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250509204755475.png" alt="image-20250509204755475" style="zoom: 50%;" />

- 进行测试

  同样，如果是使用AutoDL，则先需要使用隧道工具将端口映射到本地进行运行：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250423111426277.png" alt="image-20250423111426277" style="zoom: 25%;" />

然后打开Inspector，并选择HTTP流式模式，选择默认运行地址：`http://localhost:3000/mcp`，然后点击connect：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250509204853707.png" alt="image-20250509204853707" style="zoom:50%;" />

然后点击List Tools：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250509205307659.png" alt="image-20250509205307659" style="zoom:50%;" />

然后点击get-weather：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250509205333193.png" alt="image-20250509205333193" style="zoom:50%;" />

然后输入地名进行测试：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250509205346024.png" alt="image-20250509205346024" style="zoom:50%;" />

若能正常返回结果，则说明服务器运行正常。

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250509205402454.png" alt="image-20250509205402454" style="zoom:50%;" />

完整测试流程如下所示：

<video src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/2025-05-09%2018-37-43.mp4"></video>

## 三、流式HTTP MCP服务器异地调用

​	接下来即可在异地环境（也可以是本地）通过HTTP方式调用MCP服务了。这里以本地安装的Cherry Studio为例，进行调用演示。此处需要保持远程流式HTTP MCP服务器处于开启状态，然后按照如下流程进行调用。

​	首先点击添加服务器：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250509205717846.png" alt="image-20250509205717846" style="zoom:50%;" />

然后输入服务器名称`mcp-weather-http`，并选择流式传输类型，并选择服务器地址：http://localhost:3000/mcp ，然后点击保存：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250509205754045.png" alt="image-20250509205754045" style="zoom:50%;" />

若显示服务器更新成功，则表示已经连接上MCP服务器：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250509205843735.png" alt="image-20250509205843735" style="zoom:50%;" />

此时后台显示如下：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250509205923387.png" alt="image-20250509205923387" style="zoom:50%;" />

然后即可进行对话测试，这里回到对话页面，选择MCP服务器，

![image-20250509205950856](https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250509205950856.png)

然后进行天气查询测试：`请问北京和杭州今天天气如何？`，然后即可查看回答结果：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250509210108652.png" alt="image-20250509210108652" style="zoom:50%;" />

完整设置与调用流程演示如下：

<video src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/2025-05-09%2021-02-20.mp4"></video>

## 四、流式HTTP MCP服务器发布流程

​	测试完成后，即可上线发布。这里仍然考虑发布到pypi平台，并使用cherry studio进行本地调用测试。完整项目代码可在网盘中领取：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250509221653791.png" alt="image-20250509221653791" style="zoom:50%;" />

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/f0d53f9690c8c46b5e075fe8a0284af.jpg" alt="f0d53f9690c8c46b5e075fe8a0284af" style="zoom:50%;" />

- 打包上传：

```bash
# 回到项目主目录
# cd /root/autodl-tmp/MCP/mcp-weather-http

uv pip install build twine
python -m build
python -m twine upload dist/*
```

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250509210942317.png" alt="image-20250509210942317" style="zoom:50%;" />

- 查看发布的库：https://pypi.org/search/?q=mcp-weather-http&o=

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250509211040176.png" alt="image-20250509211040176" style="zoom:50%;" />

- 本地安装：

```bash
pip install mcp-weather-http
```

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250423112752130.png" alt="image-20250423112752130" style="zoom:50%;" />

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250509211212704.png" alt="image-20250509211212704" style="zoom:50%;" />

- 开启服务：uv run mcp-weather-http --api-key YOUR_API_KEY

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250509211617179.png" alt="image-20250509211617179" style="zoom:50%;" />

然后即可打开浏览器输入`http://localhost:3000/mcp`测试连接情况

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250509211712299.png" alt="image-20250509211712299" style="zoom:50%;" />

> 注意，这里在服务器上开启服务然后本地连接也可以，和stdio不同，HTTP模式下的MCP服务器并不需要本地运行。

- 使用Cherry studio进行连接

​	然后即可使用Cherry studio连接流式HTTP模式下的MCP服务器，还是和此前一样的连接流程，输入服务器名称`mcp-weather-http`，并选择流式传输类型，并选择服务器地址：http://localhost:3000/mcp ，然后点击保存：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250509205754045.png" alt="image-20250509205754045" style="zoom:50%;" />

若显示服务器更新成功，则表示已经连接上MCP服务器：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250509205843735.png" alt="image-20250509205843735" style="zoom:50%;" />

此时本地环境后台显示内容如下：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250509211902685.png" alt="image-20250509211902685" style="zoom:50%;" />

接下来即可进行对话测试：

<img src="https://ml2022.oss-cn-hangzhou.aliyuncs.com/img/image-20250509211942498.png" alt="image-20250509211942498" style="zoom:50%;" />

至此，我们就完成了流式HTTP MCP工具的发布、下载与调用测试流程。

