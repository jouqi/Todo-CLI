# Todo-CLI 工程化学习与实施路线（aim.md）

> 仓库：https://github.com/jouqi/Todo-CLI  
> 制定日期：2026-10-27  
> 代码基线：main，提交 06bbbec337e816bceba5a882659da7a6f1354517  
> 本文件是待实施计划。除“当前基础”外，文中的新命令、目录、数据字段和验收指标都是目标，不代表仓库已经实现。  
> README 完善工作已在 PR #1：https://github.com/jouqi/Todo-CLI/pull/1 。制定本计划时尚未合并；本文件不重复修改 README。

## 1. 最终要做出什么

把现有数字菜单 Todo 程序，逐步做成一个**单用户、本地优先、可安装和发布的 Python 命令行任务管理工具**。用它管理自己的学习任务，持续记录缺陷、实现、测试和改进。

核心完成线是 v1.0：能安装、能稳定存储、能迁移旧数据、有清晰接口、有自动测试和 CI、有发布产物、换一台电脑能照文档运行。它是一个完整的小型工程项目；它能证明的能力范围是 Python 应用开发、命令行设计、持久化、测试和交付，不应把它包装成有真实高并发或大规模用户的系统。

你的基础按现有信息处理：已完成 Git 实践，写出了任务操作与 JSON 保存，已有 9 个任务逻辑测试；MySQL 已接触多表查询、索引、事务。因此不重学 Git 入门，不先背一遍 SQL，而是练习把这些知识接到 Python 项目里。仓库中的测试存在，不等于你已经能独立设计测试，后续会专门训练。

### 完成后的能力证据

| 能力 | 仓库里应当找到的证据 |
| --- | --- |
| 分析需求 | 可执行的功能规则、边界条件、验收案例 |
| Python 开发 | 清晰模块、类型标注、异常处理、标准库应用 |
| 数据可靠性 | 损坏文件保护、事务、迁移测试、失败不破坏原数据 |
| 测试 | 业务单元测试、存储集成测试、CLI 子进程测试 |
| 工程协作 | 小步提交、可审阅 PR、真实缺陷修复记录 |
| 交付 | pyproject.toml、wheel、CI、安装验证、版本说明 |
| 独立理解 | 设计取舍文档、复盘、现场修改一个小需求 |

### 暂不进入主线的内容

不为了增加名词加入 Redis、消息队列、微服务、Kubernetes、复杂权限系统、AI 自动排期或前端框架。先把数据一致性、错误处理、测试、安装发布做扎实。后端 API 是 v1.0 之后的选修阶段；本地 CLI 的完成不依赖买服务器。

## 2. 当前基础与优先修复问题

现有模块职责：

| 文件 | 当前行为 | 要保留/改进的地方 |
| --- | --- | --- |
| app.py | 顶层读取数据并进入数字菜单循环 | 保留可运行入口，移入 main()，导入时不得启动交互 |
| todo.py | 添加、查看、完成、删除；直接 print | 保留已有业务，逐步让业务返回数据、由界面输出 |
| storage.py | 相对路径 JSON；临时文件替换；退出时保存 | 保留替换保存思想，补验证、错误传播和可注入路径 |
| tests/test_todo.py | 9 项添加、完成、删除测试 | 先跑通，再补缺陷和边界测试 |
| README.md | main 中运行示例有重复与格式问题 | 复用 PR #1，后续按每阶段真实实现更新 |

优先级从上到下：

1. 损坏 JSON 被当作空列表，退出时可能覆盖原始数据。
2. 完成/删除在空列表下会陷入无法正常取消的重试循环。
3. 保存异常只打印，调用方不知道失败；退出流程照常结束。
4. 添加/删除/完成仅修改内存，中断时可能丢失尚未保存的操作。
5. 数据位置依赖当前工作目录，容易出现“任务去哪了”。
6. 任务号是列表位置，删除或过滤后会变化，不能当长期 ID。
7. 没有数据结构校验，合法 JSON 也可能造成字段访问失败。
8. 没有打包、命令行子命令、存储测试、CI 和安装验证。

**不要一次性重写全部代码。** 每解决一个问题，保留一个可运行版本和相应测试。

## 3. 学习方式与时间安排

建议主线投入约 **90～130 小时**，按每周 8～12 小时估算约 9～16 周；这是规划预算，按验收进度调整。API 扩展另计。课程或考试忙时可以减速，不跳过数据迁移和测试来赶时间。

| 阶段 | 内容 | 参考投入 | 输出版本/成果 |
| --- | --- | --- | --- |
| P0 | 基线、环境与读懂现有项目 | 4～6 小时 | 可复现基线、调用流程笔记 |
| P1 | 数据安全与菜单可靠性 | 10～14 小时 | v0.2：可靠的现有功能 |
| P2 | 业务模型、稳定 ID 与 JSON 升级 | 14～18 小时 | v0.3：可扩展任务模型 |
| P3 | 标准子命令与可安装包 | 12～18 小时 | v0.4：可脚本调用 CLI |
| P4 | 编辑、查询、日期、导入导出 | 12～18 小时 | v0.5：可日常使用 |
| P5 | SQLite 与旧数据迁移 | 16～24 小时 | v0.6：事务化持久化 |
| P6 | CI、类型、日志与可重复环境 | 10～14 小时 | 自动质量检查 |
| P7 | 发布、演示、复盘与能力验收 | 8～12 小时 | v1.0：可展示作品 |
| P8 | FastAPI 后端扩展（选修） | 25～40 小时 | v1.1：本地 API 演示 |

每次学习 60～120 分钟，按这个顺序做：

1. 写一句用户需求，例如“损坏数据时不能覆盖原文件”。
2. 列出输入、输出、失败条件，画出这次会经过的模块。
3. 用最小失败案例复现；缺陷修复先留下能失败的测试。
4. 只读本次需要的文档章节，最多先做一个小实验。
5. 实现一条完整路径，再加异常路径。
6. 跑相关测试和全量测试，手动体验一次。
7. 提交代码，记录“为什么这样改、验证了什么、还有什么限制”。

AI 可以解释报错、给测试思路、审阅你的 diff。若让 AI 给过完整函数，至少做到：逐行解释、自己改一个边界条件、关闭答案后重写核心部分。不要把未理解且未验证的代码直接作为自己的能力证明。

## 4. 标准库和第三方包：何时学、学到什么程度

### 4.1 主线必须掌握的标准库（不需要 pip 安装）

| 模块 | 引入阶段 | 本项目用途 | 掌握标准 |
| --- | --- | --- | --- |
| sys | P0/P3 | 解释器、参数、标准输出/错误、退出码 | 看懂 sys.executable、sys.argv、stderr；用 main 返回码接 sys.exit |
| pathlib | P1 | 数据目录与文件路径 | 会 Path、mkdir、exists、read_text/open；不靠字符串硬拼路径 |
| json | P1/P2 | 持久化、旧数据迁移、导入导出 | 区分语法正确和业务结构正确；处理 JSONDecodeError |
| os | P1 | 环境变量和文件替换 | 会 environ/getenv、replace；理解同目录临时文件的原因 |
| tempfile | P1 | 独立临时文件 | 安全创建、不用固定 temp.json；失败后清理 |
| dataclasses | P2 | Task 数据模型 | 会字段、默认值与 default_factory；知道类型注解不自动校验输入 |
| enum | P2 | 固定优先级集合 | 显式约束 high/medium/low，能转换和处理错误 |
| datetime | P2/P4 | 创建/更新时间和截止日期 | 会 date、时区明确的 datetime、ISO 格式与非法日期处理 |
| typing | P2/P5 | 类型和存储接口 | 会 list、可空值、Protocol；能解释“接口”如何让存储可替换 |
| argparse | P3 | 子命令、参数、帮助 | 会 add_subparsers、choices、默认值、类型转换与错误处理 |
| subprocess | P3 | CLI 黑盒测试 | 会 run、输入/输出捕获、returncode、timeout |
| sqlite3 | P5 | SQLite 数据访问 | 参数化 SQL、事务、回滚、连接关闭、约束和锁冲突 |
| logging | P6 | 调试和错误定位 | 会级别、格式、异常栈；不把日志和命令结果混在一起 |
| unittest.mock | P1/P6 | 模拟写入失败等难造条件 | 只替换外部边界；知道 patch 的查找位置，避免把整个实现都 mock 掉 |
| tomllib | 选修 | 以后需要 TOML 配置时再读 | pyproject.toml 由工具读取，不需要为了打包自行写解析器 |
| csv | 选修 | 用户确有表格交换需求再加 CSV | 会 DictReader/DictWriter、换行和编码；v1.0 先做好 JSON |

Python 语法同步补齐：函数、参数、返回值、可变对象、作用域、列表/字典、推导式、异常、with、模块/包、类、类型注解、生成器基础。每一项都用项目里的代码解释，不要求先刷完一本书。

### 4.2 主线第三方依赖

| 安装名称 | 导入或运行方式 | 阶段 | 角色 | 学习深度 |
| --- | --- | --- | --- | --- |
| pytest | import pytest / python -m pytest | P0 起 | 开发依赖 | 必须熟练：assert、fixture、参数化、tmp_path、monkeypatch、capsys、raises |
| platformdirs | from platformdirs import user_data_path | P3 | 运行依赖 | 会获取跨系统用户数据目录；路径允许测试注入 |
| setuptools | 构建后端，由打包工具调用 | P3 | 构建依赖 | 会声明包发现和 console script，理解后端职责即可 |
| build | python -m build | P3/P7 | 开发依赖 | 会生成 wheel/sdist；理解构建与安装的区别 |
| pytest-cov | pytest 的 --cov 参数 | P6 | 开发依赖 | 会查看遗漏行和分支；覆盖率不是正确性的保证 |
| ruff | python -m ruff | P6 | 开发依赖 | 会检查、格式化和少量规则配置；能解释修复内容 |
| mypy | python -m mypy | P6 | 开发依赖 | 会查参数/返回值错误、逐步收紧，不能靠堆 Any 消除报错 |

学习优先顺序：**pytest → platformdirs 与打包 → pytest-cov / Ruff → mypy**。标准库 sqlite3 不等于需要安装名为 sqlite3 的 PyPI 包。一般官方 Python 发行版已带 sqlite3，若缺失，按发行版说明修复安装。

可选 Rich（安装 rich，导入 rich.table.Table）仅用于 P7 后改善表格显示；先做普通文本和机器可读 JSON。暂不再引入 Typer/Click，以 argparse 作为主线，避免同时学习几套同类 API。

### 4.3 后端扩展才需要的包

| 安装名称 | 常见导入 | 用途 | 必须理解 |
| --- | --- | --- | --- |
| fastapi | from fastapi import FastAPI | HTTP 路由与依赖注入 | 请求、响应、状态码、Depends；不用框架代替业务规则 |
| uvicorn | python -m uvicorn | 运行 ASGI 服务 | host、port、开发 reload 与实际运行的区别 |
| pydantic | from pydantic import BaseModel, Field | 请求/响应边界校验 | 字段约束、部分更新、序列化；不替代领域校验 |
| httpx | import httpx；或 TestClient 间接使用 | API 客户端与测试依赖 | JSON 请求、超时、错误状态、测试客户端 |

安装名称可以带连字符，导入名不一定相同；开发工具可能没有必要在业务代码中 import。不要为了“用过很多包”把测试和构建依赖混入运行依赖。

## 5. P0：建立可复现的起点

### 要做的步骤

- [ ] 拉取最新 main，确认 README PR #1 的真实状态；合并文档不是开始写功能的前置条件。
- [ ] 创建 .venv；记录 Python 版本，主线选择 Python 3.12，并在 CI 再验证 3.13。
- [ ] 安装 pytest，执行现有测试，记录实际结果；当前基线预期是 9 项。
- [ ] 手动操作添加、查看、完成、删除、退出、重启。
- [ ] 在临时目录复制测试数据复现损坏 JSON，绝不用自己的唯一数据副本。
- [ ] 画出 app → todo / storage 的调用关系。
- [ ] 写 docs/baseline.md：已实现能力、已知缺陷、复现步骤、实际运行环境。

起步命令（这些适用于现有代码）：

```bash
git clone https://github.com/jouqi/Todo-CLI.git
cd Todo-CLI
python -m venv .venv
```

Windows PowerShell：

```powershell
.\.venv\Scripts\Activate.ps1
```

macOS / Linux：

```bash
source .venv/bin/activate
```

然后执行：

```bash
python -m pip install pytest
python -m pytest -q
python app.py
```

Windows 也可用 py -3.12 创建环境；没有 python 命令的系统使用 python3。先检查 python -c "import sys; print(sys.executable)"，确认 pip 和测试确实在同一环境。

### 能力验收

不用看答案说明：数据何时加载、何时保存、任务列表由谁修改、为什么函数会改变调用方的列表、测试如何找到 todo.py。独立新写一项“负数序号不能删除任务”的测试，指出它能发现哪种错误。

## 6. P1：先让现有功能可靠

此阶段不急于搬目录或更换数据库，先在现有模块上修复问题。

### 实施顺序

- [ ] 将 app.py 的流程包进 main()，使用 if __name__ == "__main__" 入口保护。
- [ ] 空列表时完成/删除直接提示并返回菜单；输入 q 可取消操作。
- [ ] 业务入口也执行 strip 和校验，不能只依赖 app.py 提前处理。
- [ ] 给 load_tasks(path) 和 save_tasks(tasks, path) 增加显式路径参数，测试传 tmp_path。
- [ ] 定义可识别的 StorageError / DataValidationError，存储失败交给界面处理。
- [ ] 文件不存在可返回空列表；语法损坏、结构错误、权限错误要区分，禁止把损坏静默当空。
- [ ] 校验旧任务结构：顶层列表、每项对象、title 非空字符串、done 为 bool、priority 合法。
- [ ] 保留“写临时文件后 replace”的思路；临时文件在目标目录创建，名字唯一，句柄关闭后替换，尤其注意 Windows。
- [ ] 业务修改采用“副本上改动 → 保存成功 → 更新内存并提示成功”。保存失败不显示成功，保留原数据供重试。
- [ ] 每次成功修改立即保存；退出不再是唯一保存点。
- [ ] 捕获 Ctrl+C / EOF，清楚退出；不宣称能够处理强杀或断电的所有情形。

先不支持 JSON 多进程写入：原子替换只防止部分写入，不能防止两个进程覆盖彼此的更新。文档说明此限制，P5 再用事务处理。若讨论断电耐久性，区分原子替换与 fsync，不能把前者等同于绝对不丢数据。

### 必须补的测试

- [ ] import app 不触发 input，也不读写真实文件。
- [ ] 文件不存在、正常读取、中文往返、非法 JSON、缺字段、错误类型。
- [ ] 模拟临时文件写入失败和 replace 失败：原文件字节保持不变，不遗留本次临时文件。
- [ ] 空列表完成/删除可返回；非法输入可重试；q 能取消。
- [ ] 保存失败没有“操作成功”的误导；重试成功后内存与文件一致。
- [ ] 增删改后重启能看到结果；Ctrl+C 不会丢失此前已确认保存的操作。

### 交付与解释

交付 v0.2、tests/test_storage.py、缺陷复现与修复记录。能回答：JSON 语法正确为何不代表数据可用？为什么不捕获所有异常然后返回空列表？为什么业务层不直接 print？为什么原子写入不解决并发覆盖？

## 7. P2：任务模型、稳定 ID、业务分层

### 目标数据模型

| 字段 | 类型/规则 |
| --- | --- |
| id | 正整数，创建后不变，删除不重排，不复用历史 ID |
| title | 去掉两端空白后 1～200 字符 |
| description | 字符串，默认空，最多 5000 字符 |
| done | bool，默认 false |
| priority | high / medium / low，默认 medium |
| created_at | 带 UTC 时区的 ISO 时间，创建后不变 |
| updated_at | 每次实际修改时更新，使用 UTC |
| due_date | 可空，YYYY-MM-DD；只表达日历日期，不伪装成精确时刻 |

限制长度是本项目的设计选择，需要在代码、测试、帮助中一致。截止日期允许过去的日期，便于导入历史任务。逾期定义：due_date 早于本机今天且任务未完成；到期当天尚不算逾期。核心函数接收 today 参数，测试不依赖墙上时钟。

### 实施顺序

- [ ] 用 dataclass 表示 Task，用 Enum 或清晰常量约束优先级。
- [ ] 显式写入站校验与序列化函数；dataclass 不会自动验证 JSON 类型。
- [ ] 新 JSON 格式引入 schema_version、next_id、tasks；next_id 单独保存，不能每次按当前最大值重新计算。
- [ ] 新增旧格式迁移：按原顺序分配 ID，保留 title/done/priority。
- [ ] 旧格式没有时间时，以同一次迁移的时间填充，并在迁移记录说明“不是原始创建时间”。
- [ ] 迁移前备份原文件到不覆盖既有备份的新路径，全部校验通过后才替换。
- [ ] 未知更高版本拒绝读取为可写状态，不能自动降级覆盖。
- [ ] 业务层负责 add/update/done/reopen/delete/list，不负责 input/print/文件打开。
- [ ] 界面层只解析输入、调用业务、展示结果；存储层只做持久化。
- [ ] 返回明确结果或抛出明确业务异常；CLI 负责转换成错误提示。
- [ ] 原有函数逐步适配或迁移测试，不同时维护两套不一致的业务规则。

目标文件格式示意（有效数据示例，不是当前文件格式）：

```json
{
  "schema_version": 2,
  "next_id": 2,
  "tasks": [
    {
      "id": 1,
      "title": "学习存储测试",
      "description": "",
      "done": false,
      "priority": "high",
      "created_at": "2026-10-27T08:00:00+00:00",
      "updated_at": "2026-10-27T08:00:00+00:00",
      "due_date": null
    }
  ]
}
```

### 验收

- [ ] 创建 1、2、3，删除 2 后，3 仍然是 3；再添加得到 4。
- [ ] 删除最高 ID 后再添加也不能复用它；重启后规则不变。
- [ ] 旧 JSON 迁移后内容和完成状态不丢，备份可恢复。
- [ ] 迁移失败原文件不变，重复打开不会反复迁移或重复生成任务。
- [ ] 业务函数不触发终端输出，不依赖实际磁盘。
- [ ] 测试覆盖空白标题、超长标题、非法类型、重复 ID、错误 next_id、未知版本。

交付 v0.3 和 docs/decisions/001-task-model.md。能解释“展示序号”和“持久 ID”的区别，能从零写一个小 dataclass 和一个领域异常。

## 8. P3：子命令、包结构、安装入口

### 用户应当能这样使用（本阶段完成后）

```bash
todo --help
todo --version
todo add "学习 pytest" --priority high
todo list
todo done 1
todo reopen 1
todo delete 1
```

使用 argparse。先学 sys.argv 的含义，再交给 argparse 解析，不自己用下标堆叠参数判断。

### 实施顺序

- [ ] 创建 src/todo_cli/ 包和 __init__.py，逐模块迁移，每次迁移后跑测试。
- [ ] 建立 cli.main(argv=None) -> int；允许测试直接注入参数。
- [ ] __main__.py 支持 python -m todo_cli；console script 支持 todo。
- [ ] 添加各子命令及 --help，错误参数显示用法而非 Python 栈。
- [ ] 统一返回码：0 成功；2 参数/输入错误；1 找不到任务、存储等运行错误。
- [ ] 正常结果写 stdout；错误和日志写 stderr。
- [ ] 引入 platformdirs，默认使用用户数据目录，移除对工作目录的依赖。
- [ ] 支持全局 --data-dir 和 TODO_DATA_DIR：命令行 > 环境变量 > 默认目录。
- [ ] 明确全局参数写在子命令之前，例如 todo --data-dir ./demo-data list。
- [ ] 增加 todo info，显示实际数据路径、存储类型、格式版本，不暴露任务正文。
- [ ] 老 my_tasks.json 采用显式迁移/import，不能偷偷从某个工作目录自动覆盖新目录。
- [ ] 用 pyproject.toml 声明构建后端、元数据、Python 要求、依赖、dev extra 和命令入口。
- [ ] 保留 app.py 为薄兼容入口时说明行为变化；原数字菜单如保留，只是同一业务层的另一界面，不复制规则。

### 打包配置应包含什么

以下是 P3 的最小参考骨架，需配合 src/todo_cli/cli.py 中真正存在的 main 实现；dev 列表中的工具在各阶段逐步加入。版本号是项目自己的目标版本，不是宣称已发布。

```toml
[build-system]
requires = ["setuptools>=68"]
build-backend = "setuptools.build_meta"

[project]
name = "jouqi-todo-cli"
version = "0.4.0"
description = "A local-first task manager"
readme = "README.md"
requires-python = ">=3.12"
dependencies = ["platformdirs"]

[project.scripts]
todo = "todo_cli.cli:main"

[project.optional-dependencies]
dev = ["pytest", "pytest-cov", "ruff", "mypy", "build"]

[tool.setuptools.packages.find]
where = ["src"]
```

代码包名 todo_cli、发行包名 jouqi-todo-cli、终端命令 todo 是三种不同的名字，必须能解释。公开发布前另外确认名称占用和选择许可证，不凭空宣称项目已获得某种授权。

配置和包目录建立后才能执行：

```bash
python -m pip install -e ".[dev]"
python -m todo_cli --help
todo --help
python -m pytest -q
python -m build
```

### 验收

在项目目录外执行 todo list，仍看到同一数据；--data-dir 能隔离演示数据。用 subprocess.run 测 help、成功操作、非法参数、缺失 ID 和返回码。另建干净虚拟环境安装构建出的 wheel，不靠编辑安装或源码路径也能运行；测试不能通过修改 sys.path 掩盖打包错误。

## 9. P4：补齐日常任务管理

按以下顺序逐项实现，每项都走“规则 → 测试 → 业务 → CLI → 文档”。此阶段不加新的第三方运行包。

### 9.1 编辑与重新打开

- [ ] todo edit ID --title / --description / --priority，未传的字段保留。
- [ ] 没传任何编辑字段时返回输入错误，不写盘。
- [ ] todo reopen ID 将完成任务改回未完成。
- [ ] 重复 done 或 reopen 视作成功且不改变数据；updated_at 在无实际变化时保持不变。
- [ ] 找不到 ID 返回明确错误，其他任务不受影响。

### 9.2 查询、排序、统计

目标命令：

```bash
todo list --status pending --priority high
todo list --search "pytest"
todo list --sort priority
todo list --sort due
todo list --json
todo stats
```

- [ ] status 支持 all/pending/done；默认 all。
- [ ] search 同时搜索标题与描述，casefold 后子串匹配；不将用户文本当正则。
- [ ] 多过滤条件按 AND 组合；空结果是成功，不是程序错误。
- [ ] 优先级排序显式定义 high > medium > low，不用字母顺序。
- [ ] 默认按 ID 升序；due 排序按日期升序，未设日期排最后，同值按 ID。
- [ ] --json 输出稳定字段的 JSON 数组，不混入提示、颜色或日志。
- [ ] stats 返回总数、已完成、未完成、逾期数；空列表完成率约定为 0。

验收：组合过滤、中文、大小写、同优先级排序、空结果、统计守恒（总数=完成+未完成）。

### 9.3 截止日期

```bash
todo add "完成存储测试" --due 2026-11-15
todo edit 1 --due 2026-11-20
todo edit 1 --clear-due
todo list --overdue
```

- [ ] --due 用 date.fromisoformat 校验；--due 与 --clear-due 互斥。
- [ ] 默认今天由本机日期得到，但注入到服务便于测试。
- [ ] 已完成任务不算逾期。
- [ ] 测试闰年、非法日、当天、昨天、未设日期、跨月。
- [ ] 不在此阶段承诺后台提醒；程序退出后不会自行运行。

### 9.4 导入导出

```bash
todo export tasks-backup.json
todo import tasks-backup.json --dry-run
todo import tasks-backup.json
```

- [ ] 导出带版本信息，目标已存在默认拒绝；显式 --overwrite 才覆盖。
- [ ] 导入支持当前格式与经过校验的旧列表格式，先完整验证再写入。
- [ ] 默认采用“追加导入”：为导入条目分配新 ID，输出条数和必要的 ID 映射。
- [ ] 同一文件重复导入会产生重复任务，明确提示并要求 --yes 确认；不擅自按标题去重。
- [ ] --dry-run 只报告将发生的变化，绝不修改任务、next_id 或数据库。
- [ ] 全部成功或全部失败，不允许一半写入后遇到坏数据。
- [ ] JSON 原始备份/恢复与追加导入是不同概念；本版不提供危险的直接覆盖恢复命令。
- [ ] 大文件设定合理大小/条数上限并给出错误；上限值写进文档与边界测试。

交付 v0.5、命令示例和一次使用自己的学习任务做的演示。能关闭参考答案独立完成一个新过滤条件。

## 10. P5：SQLite、事务与迁移

这是连接你现有 MySQL 知识与 Python 工程的阶段。SQLite 不需要额外数据库服务，适合本地工具。它不会让项目自动变成高并发系统；要测真实行为并说明范围。

### 最小表设计

tasks 表至少包含：

- id INTEGER PRIMARY KEY AUTOINCREMENT：满足本项目删除后不复用 ID 的要求。
- title TEXT NOT NULL；description TEXT NOT NULL。
- done INTEGER NOT NULL，CHECK 只能为 0/1。
- priority TEXT NOT NULL，CHECK 固定三种值。
- created_at / updated_at TEXT NOT NULL；due_date TEXT 可空。
- schema_meta 或 PRAGMA user_version 记录数据库版本，选择一种并记录理由。

Python 领域校验与数据库约束相互补充。时间/日期统一转为约定的 ISO 字符串，不依赖隐式日期适配。标题去空白、长度等规则也需在入口校验；SQL 中 CHECK 的覆盖范围写清楚。

### 实施顺序

- [ ] 先为 P2 的存储行为写出一个最小 TaskRepository Protocol：add/get/list/update/delete，避免泛化成万能 CRUD 框架。
- [ ] 把已有 JSON 实现适配接口，跑通原有业务；再编写 SQLite 实现。
- [ ] 用同一组契约测试验证两个实现可满足共同行为；不要要求数据库每次整表 load/save。
- [ ] 在业务事务中完成读改写；更新使用 UPDATE 指定字段，禁止先读全表再整体覆盖。
- [ ] 所有用户值用 ? 占位符绑定；排序列只能从白名单映射，不能直接拼接输入。
- [ ] 明确事务起止、commit/rollback 和连接关闭；不要假设 with connection 自动关闭连接。
- [ ] 对每次操作创建受控连接；配置合理 timeout，锁冲突超时要给出可理解错误。
- [ ] 测试两个独立连接的写入和冲突。不要仅因加了 WAL 就宣称不会锁库。
- [ ] 初期保持一个明确默认存储，v0.6 起默认 SQLite；JSON 保留作为迁移和交换格式，避免让用户长期维护两份“主数据”。
- [ ] 明确数据库路径，同样受 --data-dir 控制，todo info 可查看。
- [ ] 写一个版本升级脚本/函数，当前版本初始化一次；未知高版本只读失败，不自动覆盖。
- [ ] 用 EXPLAIN QUERY PLAN 验证一个实际筛选查询，再决定是否加 done/priority 等组合索引；记录写入开销，不能把“用了索引”当性能成绩。

### 旧数据迁移的独立验收

目标命令可设计为：

```bash
todo migrate-json ./my_tasks.json --dry-run
todo migrate-json ./my_tasks.json
```

规则：

1. 只允许迁移到空数据库；非空时拒绝并建议普通 import，避免 ID 冲突。
2. 支持原始列表与 P2 版本格式；原始列表分配 ID，P2 格式保留已有 ID。
3. 备份源文件，验证所有条目和 ID、next_id；一个事务写入新库。
4. 对 P2 中比最大 ID 更大的 next_id，显式维护数据库序列高水位，不能因删除过高 ID 而复用历史 ID。
5. 完成后核对条数、ID、字段和后续新建 ID；记录源路径/内容摘要及迁移状态，重复迁移拒绝重复插入。
6. 中途报错回滚、源文件不变；迁移成功后也不自动删除源文件。
7. 在临时目录测试：空数据、损坏数据、部分非法、目标非空、重复迁移、模拟异常、ID 高水位。
8. 文档说明失败后的恢复办法；演练从备份重新迁移到一个全新目录。

### 能力验收

解释事务与原子文件替换各自解决什么；参数化 SQL 为什么防止值注入；索引为什么不总是越多越好；SQLite 与自己服务器上的 MySQL 在部署和写入并发上有何取舍。交付 v0.6、迁移报告和 docs/decisions/002-storage.md。

## 11. P6：测试体系、CI、日志与依赖管理

### 测试分层

| 测试层 | 关注点 | 依赖 |
| --- | --- | --- |
| 业务单元 | 规则、ID、过滤、日期、无实际变化 | 内存仓库或简单数据对象，固定时间 |
| 存储集成 | 序列化、约束、事务、迁移、失败保护 | tmp_path 下真实文件/SQLite |
| CLI 黑盒 | 参数、输出、退出码、跨进程重启 | subprocess + 独立数据目录 |
| 安装冒烟 | wheel 安装、入口和资源路径 | 干净虚拟环境，离开仓库目录运行 |
| API 选修 | HTTP 状态、校验、服务复用 | TestClient + 独立测试数据库 |

必须学会的 pytest 用法：

- assert 断言可观察结果，而非测试私有函数调用次数。
- fixture 负责测试数据与清理，tmp_path 保证不碰真实数据。
- parametrize 整理多组非法输入；raises 验证异常类型。
- monkeypatch 替换环境/时钟/文件边界；capsys 检查输出。
- subprocess 测返回码，设置 timeout 避免交互挂死。
- 不按实现逐行抄测试；每个重要测试能解释“错误版本会怎么失败”。

### 自动检查实施顺序

- [ ] 先用 Ruff 默认规则及 import 排序，跑格式化后确认没有业务变化。
- [ ] 对所有公共业务函数和存储边界补类型，mypy 从核心模块逐步扩展到整个 src/todo_cli。
- [ ] pytest-cov 收集主进程单元/集成测试覆盖率；子进程覆盖需额外配置，本版不要把 CLI 子进程默认算进去。
- [ ] 起步看遗漏行，v1.0 争取核心业务/存储分支覆盖率达到 80%；覆盖不足时解释未测分支，不用无意义断言凑数。
- [ ] .github/workflows/ci.yml 对 pull_request 和 push 运行；先 Ubuntu，再补 Windows。
- [ ] CI 验证 Python 3.12/3.13，矩阵至少包括 Ubuntu 与 Windows。
- [ ] 工作流读取仓库、安装环境、安装依赖、Ruff、mypy、pytest、构建 wheel。
- [ ] 构建产物再做一次干净环境安装验证，上传测试报告与构建产物供检查。
- [ ] 故意提交一次会失败的测试到练习分支，观察 CI 红灯，再修复；不在 main 保留故障。
- [ ] CI 权限设为满足检查所需的最小范围，如 contents: read；不需要部署密钥。

目标检查命令（相应配置和目录存在后）：

```bash
python -m ruff check .
python -m ruff format --check .
python -m mypy src/todo_cli
python -m pytest -q --cov=todo_cli --cov-branch --cov-report=term-missing
python -m build
```

### 日志与错误

- [ ] 默认只输出必要用户结果；--verbose 开启调试日志。
- [ ] 日志记录时间、级别、操作、错误类型，必要时包含任务 ID。
- [ ] 不记录完整任务正文或导入内容；可能含个人信息。
- [ ] 可预期错误给简短提示；调试模式才展示异常栈。
- [ ] 数据库锁定、磁盘错误、权限错误不可伪装成成功。

### 依赖管理

pyproject.toml 是直接依赖的声明来源。开发时选择的兼容范围要有依据；到发布时记录实际验证的完整环境。先不用同时引入 Poetry、uv、pip-tools 多套管理方式。

- [ ] 在干净开发环境安装后生成 requirements-dev.lock.txt：python -m pip freeze > requirements-dev.lock.txt。
- [ ] 检查文件：若有 -e 本地路径或当前项目条目，删除该条；不得提交机器私有路径。记录生成时的系统和 Python 版本。
- [ ] CI 安装锁定依赖后，使用 python -m pip install --no-deps -e . 安装项目；重新建环境验证不存在漏依赖。
- [ ] freeze 文件是该环境的快照，不宣称天然跨平台。矩阵出现平台依赖差异时用环境标记或分平台文件，并重新验证。
- [ ] 每次主动升级依赖都跑测试，记录变更原因；避免悄悄跟随最新版导致别人无法复现。

.gitignore 补上测试缓存、Ruff/mypy 缓存、coverage 产物、dist/build、egg-info、演示数据、数据库及备份。测试夹具若需提交，用明确目录和例外规则，不能把所有 *.json 无差别忽略。

## 12. 逐步形成的目标结构

这是 v1.0 参考结构，P1 不需要一次创建全部空文件。模块确有职责后再拆，避免只有一行转发的多层封装。

| 路径 | 职责 |
| --- | --- |
| pyproject.toml | 包元数据、依赖、入口、工具配置 |
| requirements-dev.lock.txt | 已验证开发环境的依赖快照 |
| src/todo_cli/__init__.py | 包标识，避免导入时做 I/O |
| src/todo_cli/__main__.py | python -m todo_cli 入口 |
| src/todo_cli/cli.py | argparse、输出和退出码 |
| src/todo_cli/models.py | Task、Priority、序列化约定 |
| src/todo_cli/service.py | 业务用例和规则 |
| src/todo_cli/errors.py | 领域和存储错误 |
| src/todo_cli/config.py | 数据目录解析和路径优先级 |
| src/todo_cli/repositories/base.py | 最小仓库接口 |
| src/todo_cli/repositories/json_repo.py | 过渡期 JSON、旧格式读取/验证 |
| src/todo_cli/repositories/sqlite_repo.py | SQLite 访问及事务 |
| src/todo_cli/migration.py | 旧格式/数据库升级和校验 |
| tests/unit/ | 业务模型和服务测试 |
| tests/integration/ | 文件、数据库、迁移测试 |
| tests/cli/ | 命令行黑盒测试 |
| tests/fixtures/ | 无个人内容的测试样本 |
| tests/conftest.py | 共享 fixture，避免塞业务实现 |
| .github/workflows/ci.yml | 自动检查 |
| docs/baseline.md | 起点和缺陷复现 |
| docs/decisions/ | 模型、存储、兼容策略的决策记录 |
| docs/demo.md | 可照做的演示脚本 |
| docs/learning-log.md | 每周学习证据 |
| README.md | 当前版本用户指南 |
| CHANGELOG.md | 实际版本变化 |
| aim.md | 本路线图和勾选进度 |

允许根据实际变化调整文件名；依赖方向保持清楚：CLI 调用 service，service 依赖领域模型与存储接口，具体仓库负责 I/O。业务层不能反向 import CLI，不能把 argparse 的 Namespace 当成领域模型到处传。

## 13. P7：发布 v1.0 与证明自己学会了

### 发布清单

- [ ] 在干净环境从仓库安装，按 README 能完成一次完整操作。
- [ ] wheel/sdist 中包含正确代码和说明，不包含个人数据、缓存或本地绝对路径。
- [ ] 当前版本测试、CI、类型与格式检查通过。
- [ ] 选择许可证后才补 LICENSE；不把“公开仓库”直接等同于任意授权。
- [ ] README 展示功能、安装、典型命令、存储位置、迁移、测试、设计限制和演示。
- [ ] CHANGELOG 只记录真实完成内容，版本号与 pyproject 一致。
- [ ] 本地制作 v1.0.0 标签和发布说明；是否推送标签、创建 Release 或发布 PyPI，由当次任务明确执行。
- [ ] GitHub Release 可附 wheel、sdist；PyPI 发布是额外选择，不是完成项目的必要条件。
- [ ] 保存一次 3～5 分钟录屏或截图序列：安装、添加、筛选、完成、重启、迁移、失败保护。
- [ ] docs/demo.md 使用 --data-dir 指向演示目录，别人照做不影响个人数据。
- [ ] 至少邀请一名同学按 README 运行一次；把真实反馈记录为 issue，尚未获得反馈不能写成已验证。

### 一份真实的工程证据包

1. 需求到实现：每个阶段至少有一个清晰 PR，描述问题、行为、测试和限制。
2. 缺陷到修复：保存 2～3 个真实案例，例如损坏 JSON 保护、列表 ID 错位、迁移回滚。
3. 决策到验证：解释为何 argparse、为何先 JSON 后 SQLite、为何暂不引入 ORM。
4. 自动化：链接 CI 结果，附可复现命令和实际环境。
5. 性能实验：用固定种子造 1000/10000 条合成任务，分别测过滤或查询，记录环境、方法、实际结果；没有测量不能写“性能提升 XX%”。
6. 个人理解：关闭项目后实现一个小功能，再说明如何接回原结构。

### 现场自测题

- 从终端输入 todo done 7 到数据库提交，中间经过哪些函数？
- 数据库提交失败时，用户看到什么？内存、文件和日志会怎样？
- 为何 dataclass 类型注解不能挡住不合法 JSON？
- 为什么 task ID 不能使用过滤后的位置？
- 删除最高 ID 后如何保证下一个 ID 不复用？
- 临时文件替换、事务、备份分别保障什么？
- 如何证明迁移失败不损坏原数据？
- 若把数据目录改到不存在/只读的位置，怎么测？
- 为什么 editable 安装成功不等于 wheel 能用？
- 为何 100% 覆盖率也不能保证业务正确？
- 如果新增“按描述关键词筛选”，你能否不看答案独立完成？
- 如果需要多人共享，你现有方案哪些假设会失效？

### 简历描述模板（完成后据实填）

“独立开发 Python 本地任务管理工具，基于 argparse 提供任务管理、筛选与导入导出；使用 SQLite 事务持久化，并实现旧 JSON 数据迁移及异常回滚；通过 pytest、类型检查和 GitHub Actions 验证，在 Windows/Linux 完成安装测试并提供 wheel 发布产物。”

只写实际完成的部分。测试数量、覆盖率、性能数字都从报告填写；该项目能展示工程基本功，不能单独证明所有岗位要求，也不能替代算法、网络、操作系统等基础学习。

## 14. P8：FastAPI 后端扩展（v1.0 后选修）

进入条件：CLI v1.0 已完成，能解释并独立改动 service/repository，确实想进一步展示 Python 后端能力。不要在前面遇到困难时不断换技术栈。

### 目标

让 CLI 和本地 HTTP API 复用同一套业务服务。此扩展先是**仅监听本机的单用户 API**，不具备用户认证和数据隔离，不直接暴露公网。

### 实施顺序

- [ ] 学 HTTP 方法、URL、JSON、请求头、状态码、同步请求与超时。
- [ ] 安装 fastapi、uvicorn、pydantic；httpx 作为测试/客户端依赖。
- [ ] pyproject 增加 api extra，dev extra 加 httpx；以后用 pip install -e ".[dev,api]"，避免 CLI 用户被迫安装 API。
- [ ] 创建 api.py，路由只做校验、调用 service、映射响应。
- [ ] 建立 Pydantic 的 Create/Update/Response 模型，区分“字段未传”与“显式清空”。
- [ ] 为请求注入独立受控仓库连接；不要让线程共享全局 sqlite3 连接。
- [ ] 优先普通 def 路由配同步 sqlite3；不把阻塞 I/O 直接放进 async def 后宣称异步。
- [ ] 完成以下接口及自动文档；每个接口注明成功与失败响应。
- [ ] 为每个测试注入独立数据库路径，使用 TestClient，不能访问个人数据库。
- [ ] CLI 和 API 对相同输入给出一致业务结果，业务规则不能复制两份。
- [ ] 最后再考虑用容器演示，先在本机验证安装和启动。

目标接口：

| 方法与路径 | 行为 | 关键响应 |
| --- | --- | --- |
| GET /health | 进程健康，不暴露配置秘密 | 200 |
| POST /tasks | 创建任务 | 201；校验失败 422 |
| GET /tasks | 过滤、分页 | 200，列表及分页信息 |
| GET /tasks/{id} | 查看单条 | 200 / 404 |
| PATCH /tasks/{id} | 部分更新，包括完成状态 | 200 / 404 / 422 |
| DELETE /tasks/{id} | 删除 | 204，无响应体 / 404 |

分页建议 limit 默认 20、最大 100，offset 非负；排序稳定。领域输入错误和存储错误在 API 边界统一映射，不能把所有异常都伪装成 404。写明这不是多用户服务。

代码和 extras 就绪后的开发命令：

```bash
python -m pip install -e ".[dev,api]"
python -m uvicorn todo_cli.api:app --host 127.0.0.1 --port 8000 --reload
```

验收：创建、查询、分页、更新、删除、未知 ID、非法日期、空输入、重复操作、数据库异常；通过 /docs 演示；测试路由层之外仍保留业务单元测试。开发 reload 不用于生产部署。

### API 之后的升级触发条件

| 扩展 | 什么时候有必要 | 到时才学的内容 |
| --- | --- | --- |
| SQLAlchemy + Alembic | 要迁移到服务器数据库或更复杂模型时 | ORM 映射、Session、事务、显式数据库迁移 |
| MySQL 驱动 | 明确需要 MySQL 共享服务时 | PyMySQL 等驱动、连接配置、连接池、集成测试 |
| 登录与权限 | 真实多用户与公网服务之前 | 密码哈希、认证、授权、所有权隔离、密钥管理 |
| Docker | 需要交付可运行 API 环境时 | 镜像、非 root、数据卷、端口、持久化、日志 |
| 前端 | 确实需要图形界面时 | 先做最小页面/API 调用，再选框架 |
| 后台提醒 | 有明确触发与调度需求时 | 常驻进程、任务调度、重复执行和可靠性 |

这些不计入 v1.0 必做项。若未来安排实施，再为选定扩展单独补需求、包版本、验收和部署边界。

## 15. 官方学习入口：按阶段查阅，不用通读

以下为实施时可直接查阅的官方文档。以项目选择的 Python 版本为准；不要因为在线文档展示了更新特性，就直接写进要求支持 3.12 的代码。

| 主题 | 文档 | 先读什么 |
| --- | --- | --- |
| Python 模块与包 | https://docs.python.org/3.12/tutorial/modules.html | __name__、包、导入 |
| sys | https://docs.python.org/3.12/library/sys.html | argv、exit、stderr、executable |
| 路径 | https://docs.python.org/3.12/library/pathlib.html | Path、读写、目录 |
| JSON | https://docs.python.org/3.12/library/json.html | load/dump、JSONDecodeError |
| 临时文件 | https://docs.python.org/3.12/library/tempfile.html | NamedTemporaryFile、跨平台注意事项 |
| 数据模型 | https://docs.python.org/3.12/library/dataclasses.html | dataclass、field、asdict |
| 日期时间 | https://docs.python.org/3.12/library/datetime.html | date、时区、ISO |
| CLI | https://docs.python.org/3.12/library/argparse.html | 子命令、choices、错误提示 |
| SQLite | https://docs.python.org/3.12/library/sqlite3.html | 占位符、事务、连接生命周期 |
| logging | https://docs.python.org/3.12/library/logging.html | 级别、处理器、异常 |
| pytest | https://docs.pytest.org/en/stable/ | 入门、fixture、参数化、tmp_path、monkeypatch |
| platformdirs | https://platformdirs.readthedocs.io/ | user_data_path 与目录覆盖 |
| Python 打包 | https://packaging.python.org/en/latest/guides/writing-pyproject-toml/ | scripts、dependencies、optional-dependencies |
| 构建发布 | https://packaging.python.org/en/latest/tutorials/packaging-projects/ | 包目录、build、wheel |
| Ruff | https://docs.astral.sh/ruff/ | check、format、pyproject 配置 |
| mypy | https://mypy.readthedocs.io/en/stable/getting_started.html | 注解、错误、逐步检查 |
| 覆盖率 | https://pytest-cov.readthedocs.io/en/latest/ | --cov、分支、报告 |
| CI | https://docs.github.com/en/actions/tutorials/build-and-test-code/python | Python、矩阵、测试、构建产物 |
| API 选修 | https://fastapi.tiangolo.com/tutorial/ | 请求体、状态码、Depends、Testing |
| Pydantic 选修 | https://docs.pydantic.dev/latest/ | BaseModel、Field、序列化 |

包的精确版本在实际引入时选择兼容版本并测试、锁定。本路线图没有虚构“已经验证的一整套最新依赖版本”。

## 16. 每周复盘与完成定义

每周在 docs/learning-log.md 新增一条，不能只写“学了 SQLite”：

```markdown
## 第 N 周
- 本周需求：
- 完成的提交/PR：
- 我独立写出的部分：
- 参考文档：
- AI 帮助了什么，我如何验证：
- 遇到的真实错误与根因：
- 新增测试及其能发现的错误：
- 手动验证步骤与结果：
- 能否不看代码解释本周改动：
- 尚未通过的验收：
- 下周只推进的一项：
```

单项功能的完成定义：

- [ ] 正常路径和至少一个有意义的失败路径明确。
- [ ] 相关测试与现有测试都通过。
- [ ] 失败时不会静默破坏既有数据。
- [ ] 输出、错误、返回码与文档一致。
- [ ] 提交不包含真实数据或环境私有路径。
- [ ] 可以用自己的话解释实现和取舍。
- [ ] 可以关闭参考资料后重写关键的小段逻辑。
- [ ] 进度只勾选实际完成并验证的内容。

## 17. 今天就开始的第一张任务卡

**任务：让“损坏 JSON 不得覆盖原文件”成为第一项工程改进。**

1. 新建工作分支，例如 fix/protect-invalid-json。
2. 在 tests/test_storage.py 用 tmp_path 写入坏 JSON，保存原始字节。
3. 先写一个会在当前实现上失败的测试：读取应报告明确错误，不能返回可写的空列表。
4. 给 load_tasks 增加可注入的 path，定义存储异常，修改 app 的启动错误处理。
5. 用启动失败/中止流程验证不会继续走退出保存，原始字节保持不变。
6. 再测文件不存在仍能正常从空任务开始，防止修坏正常首次启动。
7. 跑 python -m pytest -q，记录测试结果与一次手动复现。
8. 提交一个小 PR，只解决这张任务卡。

本周只把 P0 和这张卡做透。等你能解释“如何证明原文件没有被覆盖”，再接着完成 P1 的其他条目。
