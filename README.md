<div align="center">

# 🤖 智能跨境电商一站式平台

### 从商品分析到多平台刊登，多个 AI Agent 协作完成视觉内容生产 —— **你能实时看到每个 Agent 的思考与协作过程**

**基于 LangGraph 的多 Agent 协作 · 跨境电商智能融合 · 可观测 Agent 工作台**

[![Author](https://img.shields.io/badge/Author-shushanxiang-blue.svg)](https://github.com/shushanxiang)
[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg?logo=python&logoColor=white)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-teal.svg?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Vue 3](https://img.shields.io/badge/Vue-3.4-42b883.svg?logo=vue.js&logoColor=white)](https://vuejs.org/)
[![LangGraph](https://img.shields.io/badge/LangGraph-powered-orange.svg)](https://langchain-ai.github.io/langgraph/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16%20%2B%20pgvector-336791.svg?logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)

**作者 / 维护者：shushanxiang**

</div>

> 💡 **一句话介绍**：**AgenticCommerce（CBCF Platform）** 用一张 LangGraph 状态图编排多个专业 Agent，自动完成跨境电商的商品分析、AI 文案、图片／视频生成、合规检查、多平台刊登全流程；并通过一个 DevTools 风格的可观测工作台，让你实时看到每个 Agent 的提示词、传递参数与协作轨迹。

---

## 📑 目录

- [✨ 这是什么](#-这是什么)
- [🚀 核心特性](#-核心特性)
- [🏗️ 系统架构](#️-系统架构)
- [⚡ 快速开始](#-快速开始)
- [🔑 访问地址与默认账号](#-访问地址与默认账号)
- [⚙️ 环境变量](#️-环境变量)
- [📁 项目结构](#-项目结构)
- [🛠️ 技术栈](#️-技术栈)
- [🧪 开发与测试](#-开发与测试)
- [🩺 常见问题排查](#-常见问题排查)
- [🗺️ 路线图](#️-路线图)
- [📄 许可证](#-许可证)

---

## ✨ 这是什么

**智能跨境电商融合平台**是一个面向跨境电商的 **多 Agent 协作系统**，利用 LangGraph 状态图驱动多个专业 Agent 协同工作，自动完成从商品分析到视觉内容生成、合规检查、多平台刊登的全流程。

- 📦 **商品信息分析** — Agent 自动提取卖点、分析目标人群
- ✍️ **AI 文案生成** — 平台风格适配、LLM 多级降级策略
- 🖼️ **图片生成** — 多模型通道 + 异步调用
- 🎬 **视频生成** — 分镜脚本设计 + 视频生成（JWT 鉴权 + 任务轮询）
- ✅ **合规检查** — 广告法禁词检测、平台规则验证
- 🌐 **多平台刊登** — Amazon / eBay / Shopify 适配器，凭证加密存储
- 📚 **RAG 知识增强** — PGVector 向量检索 + Graph RAG + 记忆库
- 🔬 **Agent 可观测工作台** — DAG 流程图 + 提示词轨迹 + 实时协作视图
- 📊 **AI 会话追踪** — Token 消耗统计与内容检索
- 🔌 **多模型厂商切换** — 支持多家 LLM／图片／视频厂商丝滑切换

> 💡 **适合谁？** 跨境电商从业者、AI 应用开发者、LangChain／LangGraph 学习者、对 Agent 可观测性感兴趣的研究者。

---

## 🚀 核心特性

| 特性 | 描述 |
|------|------|
| 🔬 **Agent 可观测工作台** | DAG 流程图（AntV G6）+ 提示词轨迹 + WebSocket 实时协作 |
| 🤖 **多 Agent 协作** | 视觉生成 Agent + 刊登 Agent + RAG 增强 Agent，统一由 LangGraph 编排 |
| 🔄 **LangGraph 工作流** | 条件路由、状态累加（`Annotated[..., add]`）、stream 模式实时回调 |
| 🖼️ **图片生成** | 多模型通道，异步调用与结果回传 |
| 🎬 **视频生成** | HS256 JWT 鉴权 + 异步任务轮询 |
| 📚 **RAG 增强** | PGVector + 本地 BGE-large-zh／云端 Embedding 双通道 |
| 🕸️ **Graph RAG** | 知识图谱实体／关系 + 社区摘要 + 混合检索（RRF 融合） |
| ✅ **合规检查** | 广告法禁词 + 平台规则校验 |
| 🌐 **多平台刊登** | Amazon / eBay / Shopify 适配器与推送服务 |
| 🔄 **多模型通道** | OpenAI 兼容协议 + 各厂商原生 SDK |
| 📊 **会话追踪** | Token 统计、内容检索 |
| 🔐 **认证鉴权** | JWT 登录 + API Token（SHA256 + Scope）+ 多租户隔离 |
| 🛡️ **优雅降级** | 无 API Key 时自动 Mock，LLM 降级链 |
| 🎨 **管理后台** | Vue 3 + Element Plus，覆盖商品／任务／知识库／刊登／会话等页面 |
| 🔌 **多厂商切换** | 模型厂商配置系统，支持 DB 驱动 + Settings 回退 |

---

## 🏗️ 系统架构

```
┌──────────────────────────────────────────────────────────────┐
│                    Vue 3 管理后台（Vite / 端口 5173）          │
│  仪表盘 │ 商品管理 │ 任务管理 │ 知识库 │ 刊登工具 │ AI 会话     │
│         │          │ Agent 可观测工作台 │         │           │
└──────────────────────────┬───────────────────────────────────┘
                           │ REST API  ·  WebSocket（/api、/ws 代理）
┌──────────────────────────▼───────────────────────────────────┐
│                   FastAPI API 层（端口 8002）                  │
│  认证：JWT / API Token（SHA256 + Scope）   租户隔离：tenant_id  │
└──────────────────────────┬───────────────────────────────────┘
                           │
┌──────────────────────────▼───────────────────────────────────┐
│                     LangGraph 工作流引擎                       │
│                                                               │
│  视觉生成工作流：                                              │
│  Orchestrator → RequirementAnalyzer → CreativePlanner         │
│      → VisualDesigner → [ImageGenerator | VideoGenerator]     │
│      → QualityReviewer → END                                  │
│                                                               │
│  刊登工作流：                                                  │
│  ImportProduct → [AssetOptimizer | Copywriter] → Compliance    │
│      → PlatformAdapter → Push                                 │
│                                                               │
│  知识库工作流：                                                │
│  Ingestion → Graph / 向量入库 → HybridRetriever → Rerank      │
└───────┬──────────────┬──────────────┬────────────────────────┘
        │              │              │
 ┌──────▼──────┐ ┌─────▼─────┐ ┌─────▼──────┐
 │   LLM 厂商   │ │  图片厂商  │ │  视频厂商   │
 │ (OpenAI兼容) │ │  (多模型)  │ │  (分镜设计) │
 └──────┬──────┘ └─────┬─────┘ └─────┬──────┘
        │              │              │
 ┌──────▼──────────────▼──────────────▼────────────┐
 │ PostgreSQL 16 + pgvector │  Redis  │  文件存储    │
 │  业务表 / 向量 / 图谱     │ 任务状态 │  本地 / OSS  │
 └─────────────────────────────────────────────────┘
```

---

## ⚡ 快速开始

### 方式一：Windows 一键脚本（面向课堂 / 教学推荐 ⭐⭐⭐⭐⭐）

项目根目录已提供开箱即用的一键脚本：

| 脚本文件 | 说明 | 适用场景 |
|---------|------|---------|
| [**`一键初始化环境.bat`**](一键初始化环境.bat) | 创建 Conda `cbcf` 虚拟环境，安装 Python 与 npm 依赖，生成 `.env` | 新电脑首次配置 |
| [**`一键启动.bat`**](一键启动.bat) | 检测端口占用，分别在独立窗口启动后端（`8002`）与前端（`5173`），并自动打开浏览器 | **日常使用（最常用）** |
| [**`一键停止.bat`**](一键停止.bat) | 释放 `8002` 与 `5173` 端口占用 | 结束实验 / 端口冲突时 |

```text
1.（仅新电脑首次）双击【一键初始化环境.bat】
2. 双击【一键启动.bat】→ 浏览器自动打开 http://localhost:5173/
3. 使用完毕后双击【一键停止.bat】退出
```

> ⚠️ **注意**：本方式仍需 PostgreSQL 与 Redis 可用，否则登录与数据接口会报错（排查方法见 [常见问题排查](#-常见问题排查)）。

---

### 方式二：Docker 部署

> 🖥️ 目标机器只需安装 [Docker Desktop](https://www.docker.com/products/docker-desktop/)。

```bash
# 1. 进入项目目录
cd cbcf-platform

# 2.（首次）准备环境变量文件，按需填入 API Key
#    不填也能跑：Mock 模式会自动降级生成占位资产
cp .env.example .env

# 3. 一键构建并启动（含 PostgreSQL 16 + pgvector + Redis）
docker compose up -d --build

# 4. 访问
#   前端:          http://localhost:3000
#   后端 API 文档:  http://localhost:8000/docs
#   健康检查:       http://localhost:8000/api/v1/health
```

`docker-compose.yml` 的服务与端口映射：

| 服务 | 镜像 | 端口映射 |
|------|------|---------|
| `app` | 自建（`Dockerfile`） | `8000:8000` |
| `frontend` | 自建（`Dockerfile.frontend`，Nginx） | `3000:80` |
| `postgres` | `pgvector/pgvector:pg16` | `5433:5432` |
| `redis` | `redis:7-alpine` | `6380:6379` |

> ⏳ **首次启动说明**：本地 Embedding 模型（`BAAI/bge-large-zh`，约 1.2GB）会在首次使用时下载，期间 RAG 检索暂不可用，其余功能正常；下载失败会自动降级，不影响演示。模型与数据持久化在 `models` 卷与 `pgdata` / `redis_data` 卷中，二次启动无需重新下载。

<details>
<summary>共享模式（复用已有 PostgreSQL + Redis）</summary>

```bash
# 首次使用需手动启用 pgvector 扩展
docker exec <postgres容器名> psql -U postgres -d cbcf -c "CREATE EXTENSION IF NOT EXISTS vector;"

docker compose -f docker-compose.shared.yml up -d --build
```
</details>

---

### 方式三：本地 Conda 命令行开发

```bash
# 0. 前置条件：PostgreSQL（含 pgvector）与 Redis 已启动
#    若使用 Docker 容器承载依赖服务，请先确保 Docker Desktop 正在运行

# 0.1 首次使用需启用 pgvector 扩展
docker exec <postgres容器名> psql -U postgres -d cbcf -c "CREATE EXTENSION IF NOT EXISTS vector;"

# 1. 创建并激活 conda 虚拟环境
conda create -n cbcf python=3.13 -y
conda activate cbcf

# 2. 安装后端依赖
pip install -r requirements.txt

# 3. 配置环境变量（务必与实际的数据库 / Redis 端口一致）
cp .env.example .env

# 4. 启动后端（默认端口 8002）
python main.py

# 5. 新开终端，启动前端（默认端口 5173）
cd frontend
npm install
npm run dev
```

> 🛡️ **Mock 模式**：`.env` 默认 `ALLOW_MOCK_ASSETS=true`，未配置 API Key 时会自动降级生成占位资产，便于无 Key 体验完整流程。数据持久化与 RAG 知识库仍需要 PostgreSQL 与 Redis 支持。

---

## 🔑 访问地址与默认账号

| 项目 | 地址 |
|------|------|
| 前端管理后台 | http://localhost:5173/ |
| 后端 API 文档（Swagger） | http://localhost:8002/docs |
| 后端健康检查 | http://localhost:8002/api/v1/health |

> 🔌 前端开发服务器已配置代理：`/api`、`/ws` → `http://127.0.0.1:8002`（见 [frontend/vite.config.ts](frontend/vite.config.ts)）。

**默认开发账号**（由初始化脚本创建）：

| 用户名 | 密码 |
|--------|------|
| `admin` | `admin123` |

若账号不存在，可执行初始化脚本，或直接在注册页面 `http://localhost:5173/register` 注册新账号（注册时自动创建独立工作空间／租户）。

---

## ⚙️ 环境变量

### 必填（Mock 模式下可不填）

| 变量 | 说明 |
|------|------|
| `QWEN_API_KEY` | LLM API Key（百炼 OpenAI 兼容模式） |

### 核心可选

| 变量 | 默认值 | 说明 |
|------|--------|------|
| `LLM_PROVIDER` | `qwen` | LLM 提供商：`qwen`（OpenAI 兼容）/ `dashscope`（SDK） |
| `QWEN_API_BASE` | — | LLM OpenAI 兼容端点 |
| `QWEN_LLM_MODEL` | `qwen-plus` | LLM 模型名称 |
| `DASHSCOPE_API_KEY` | — | 图片生成 API Key（可与 `QWEN_API_KEY` 共用） |
| `SENSENOVA_API_KEY` | — | 商汤 SenseNova API Key |
| `KLING_ACCESS_KEY` | — | 视频生成（可灵 AI）Access Key |
| `KLING_SECRET_KEY` | — | 视频生成（可灵 AI）Secret Key |
| `RAG_ENABLED` | `true` | 启用 RAG 知识检索 |
| `EMBEDDING_PROVIDER` | `local` | Embedding 通道：`local`（BGE-large-zh）或 `qwen` |
| `EMBEDDING_MODEL` | `BAAI/bge-large-zh` | 本地 Embedding 模型名称 |
| `QWEN_EMBEDDING_DIMENSIONS` | `1024` | 千问 Embedding 维度（须与 DB 向量列一致） |
| `RETRIEVAL_TOP_K` | `5` | 检索返回数量 |
| `SIMILARITY_THRESHOLD` | `0.5` | 相似度阈值 |
| `POSTGRES_HOST` | `localhost` | PostgreSQL 主机 |
| `POSTGRES_PORT` | `5432` | PostgreSQL 端口（**须与实际服务一致**） |
| `POSTGRES_USER` | `postgres` | PostgreSQL 用户名 |
| `POSTGRES_PASSWORD` | — | PostgreSQL 密码 |
| `POSTGRES_DB` | `cbcf` | PostgreSQL 数据库名 |
| `REDIS_URL` | `redis://localhost:6379/0` | Redis 连接 URL（**须与实际服务一致**） |
| `HOST` / `PORT` | `0.0.0.0` / `8002` | 后端监听地址与端口 |
| `STORAGE_TYPE` | `local` | 存储类型：`local` 或 `oss` |
| `STORAGE_PATH` | `./output` | 本地存储路径 |
| `AUTH_ENABLED` | `false` | 是否启用 Token 鉴权 |
| `CREDENTIALS_ENCRYPTION_KEY` | — | 适配器凭证加密密钥（Fernet） |
| `CORS_ALLOW_ORIGINS` | `http://localhost:5173,...` | 允许的跨域来源，逗号分隔 |
| `ALLOW_MOCK_ASSETS` | `true` | 无 API Key 时允许 Mock 降级生成占位资产 |

> 📌 **命名提醒**：`Settings` 未设置 `env_prefix`，高级 RAG 配置的键名必须与字段名完全一致（例如 `RERANKER_ENABLED`，而非 `RAG_RERANKER_ENABLED`），否则该配置会静默失效。

完整配置与注释见 [`.env.example`](.env.example)。

---

## 📁 项目结构

```
cbcf-platform/
├── main.py                       # FastAPI 应用入口（含 lifespan 初始化）
├── run_workflow.py               # CLI 工作流运行脚本
├── src/                          # 后端源码
│   ├── agents/                   # Agent 实现
│   │   ├── base.py               #   Agent 基类
│   │   ├── orchestrator.py       #   编排调度
│   │   ├── requirement_analyzer.py / creative_planner.py
│   │   ├── visual_designer.py / image_generator.py / video_generator.py
│   │   ├── quality_reviewer.py
│   │   ├── rag_*.py              #   RAG 增强 Agent
│   │   └── listing_*.py          #   刊登 Agent（导入/优化/文案/合规/适配器/推送）
│   ├── graph/                    # LangGraph 状态图与工作流
│   │   ├── state.py / workflow.py            #   视觉生成工作流
│   │   └── listing_state.py / listing_workflow.py  # 刊登工作流
│   ├── api/                      # API 层
│   │   ├── router/               #   路由（products / tasks / knowledge / listing /
│   │   │                         #         dashboard / assets / auth / model_providers ...）
│   │   ├── schema/               #   请求 / 响应模型
│   │   └── service/              #   Redis 客户端、任务管理、资产落库、会话记录
│   ├── clients/                  # 外部服务客户端（LLM / 图片 / 视频 / Embedding）
│   ├── rag/                      # RAG 检索管道
│   │   ├── retriever.py / embeddings.py / chunker.py
│   │   ├── hybrid_retriever.py / reranker.py / query_rewriter.py
│   │   └── graph_builder.py / graph_memory.py / memory_store.py
│   ├── knowledge/                # 知识库：ingestion / graph / workflow
│   ├── db/                       # 数据库：SQLAlchemy 模型、仓储、向量存储
│   ├── models/                   # 领域模型（product / creative / storyboard / assets / listing）
│   ├── storage/                  # 文件存储抽象（本地 / 工厂）
│   ├── auth/                     # 认证上下文与 API Token
│   └── config/                   # 配置管理（pydantic-settings）
├── frontend/                     # Vue 3 前端
│   └── src/
│       ├── views/                #   页面：仪表盘 / 商品 / 任务 / 工作台 / 知识库 /
│       │                         #         刊登 / AI 会话 / 模型厂商 / 登录注册
│       ├── components/           #   布局组件 + workbench/ Agent 可观测工作台组件
│       ├── api/ types/ stores/   #   接口调用层 / TS 类型 / Pinia 状态
│       ├── composables/          #   useTaskWebSocket（任务实时推送）
│       └── workflow/             #   DAG 拓扑与节点渲染
├── tests/                        # 测试用例（agents / api / db / graph / rag / models ...）
├── scripts/                      # 初始化与辅助脚本（seed、迁移、启动等）
├── docs-site/                    # MkDocs 文档站点
├── docker-compose.yml            # Docker 编排（独立部署）
├── docker-compose.shared.yml     # Docker 编排（复用已有依赖服务）
├── Dockerfile / Dockerfile.frontend
├── init.sql                      # 数据库初始化 SQL
└── pyproject.toml                # 项目配置（依赖 / ruff / mypy / pytest）
```

---

## 🛠️ 技术栈

| 层级 | 技术 | 说明 |
|------|------|------|
| **工作流引擎** | LangChain / LangGraph | `langchain>=1.0.0`、`langgraph>=1.0.0` |
| **后端框架** | FastAPI + Pydantic v2 + SQLAlchemy 2.0（async） | `uvicorn` 运行 |
| **语言模型** | OpenAI 兼容协议 + DashScope 原生 SDK | `langchain-openai`、`dashscope` |
| **图片生成** | 多模型通道（DashScope 万象 / OpenAI 兼容 / 商汤） | 异步调用 + 结果回传 |
| **视频生成** | 可灵 AI（JWT 鉴权 + 任务轮询） | `pyjwt` |
| **向量检索** | PGVector + BGE-large-zh（本地 Embedding） | `sentence-transformers`（`rag` 可选依赖） |
| **图谱检索** | Graph RAG（实体／边／社区摘要） | `python-igraph`、`leidenalg` |
| **数据库** | PostgreSQL 16 + pgvector、Redis | `asyncpg`、`pgvector`、`redis` |
| **存储** | 本地文件系统 / 云存储 OSS | `STORAGE_TYPE` 切换 |
| **前端** | Vue 3 + TypeScript + Element Plus + Pinia + Vue Router + AntV G6 | Vite 5 构建 |
| **部署** | Docker Compose + Nginx | — |
| **质量工具** | pytest（asyncio）/ ruff / mypy | 覆盖率门槛 80% |

---

## 🧪 开发与测试

```bash
# 运行测试
python -m pytest

# 带覆盖率报告
python -m pytest --cov=src --cov-report=html

# 代码格式化
ruff format .

# Lint 检查
ruff check .

# 类型检查
mypy src/
```

- 测试配置见 `pyproject.toml`：`asyncio_mode = "auto"`，覆盖率 `fail_under = 80`。
- 自定义标记：`slow`、`integration`、`e2e`。
- 提交规范：`feat` / `fix` / `docs` / `refactor` / `test`。

---

## 🩺 常见问题排查

### 1. 页面提示「服务器内部错误」

绝大多数情况下是**依赖服务未就绪**，而非代码问题。排查顺序：

```bash
# ① 确认依赖容器在运行（本地常用方式）
docker ps --filter "name=cbcf"

# ② 确认后端能连上 Redis / PostgreSQL
#    查看后端日志是否出现类似报错：
#    redis.exceptions.ConnectionError ... Connect call failed ('127.0.0.1', 6381)
#    Connect call failed ('127.0.0.1', 5434)

# ③ 核对 .env 中的端口与实际服务端口是否一致
#    REDIS_URL / POSTGRES_PORT
```

常见原因：**Docker Desktop 引擎没有启动**，导致承载 PostgreSQL / Redis 的容器处于停止状态，此时登录、创建商品等接口都会抛连接异常并被全局异常处理器转换为 500。

### 2. 没有大模型 API Key 能用吗？

可以。`.env` 默认 `ALLOW_MOCK_ASSETS=true`，系统会生成 Mock 占位资产，可完整体验 Agent 工作流与可观测工作台。

### 3. 想切换真实模型？

编辑根目录 `.env`，填写 `QWEN_API_KEY`（LLM）、`DASHSCOPE_API_KEY`（图片）、`KLING_ACCESS_KEY` / `KLING_SECRET_KEY`（视频）等，保存后重启后端即可。

### 4. 端口被占用？

双击 [`一键停止.bat`](一键停止.bat) 释放 `8002` / `5173`，或改用 `docker compose` 部署（`8000` / `3000`）。

### 5. 首次启动较慢？

首次会下载本地 Embedding 模型（约 1.2GB）；Docker 方式下后端镜像因内置 `sentence-transformers`（含 PyTorch）体积较大，首次构建耗时属正常现象。

---

## 🗺️ 路线图

- [x] **v0.1.0** — LangGraph 多 Agent 视觉生成工作流 + RAG 知识库 + 合规检查 + Vue 3 管理后台
- [x] **v0.2.0** — 多模型厂商对接 + AI 会话追踪 + Agent 可观测工作台（DAG + 提示词轨迹）
- [ ] **v0.3.0** — 高级 RAG（HyDE / 多查询重写）+ GraphRAG 增强 + 生产级刊登
- [ ] **v0.4.0** — Agent 自适应重试与自愈 + 工作流可视化编辑器
- [ ] **v1.0.0** — 多租户 SaaS 化 + 插件式 Agent 市场 + 生产就绪

---

## 📄 许可证

本项目基于 [Apache License 2.0](LICENSE) 开源。


---

参考项目：

 GitHub 仓库：https://github.com/haowlai/AgenticCommerce

  GitHub 仓库：https://github.com/liangdabiao/amazon-sorftime-research-MCP-skill

  GitHub 仓库：https://github.com/adongwanai/AgentGuide



 ---

<div align="center">

**智能跨境电商融合平台** — 让 AI Agent 协作改变跨境电商内容生产方式

作者：**shushanxiang**

</div>
