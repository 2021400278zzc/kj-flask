 # 后端框架

## 项目介绍

这是一个基于Flask的后端框架，目前提供用户管理、部门管理、通知管理等功能示例。该框架使用现代化的技术栈，包括Flask、JWT认证、MySQL数据库和定时任务调度等。

## 技术栈

- **后端框架**：Flask 3.1.0
- **数据库**：MySQL (使用SQLAlchemy ORM)
- **认证**：JWT (Flask-JWT-Extended)
- **定时任务**：APScheduler
- **API文档**：Flask blueprints
- **其他工具**：Flask-Migrate, Flask-CORS, PyMySQL

## 项目结构

```
├── app/                        # 应用主目录
│   ├── controllers/            # 控制器层，处理业务逻辑
│   │   └── user.py             # 用户相关业务逻辑
│   │
│   ├── models/                 # 数据模型层，定义数据库模型
│   │   ├── __init__.py         # 模型初始化和通用基类
│   │   ├── department.py       # 部门模型
│   │   ├── member.py           # 成员模型
│   │   ├── notification.py     # 通知模型
│   │   └── period_task.py      # 定期任务模型
│   │
│   ├── modules/                # 功能模块
│   │   ├── jwt.py              # JWT认证模块
│   │   ├── logger.py           # 日志模块
│   │   ├── sql.py              # 数据库连接模块
│   │   └── sched/              # 定时任务调度模块
│   │       ├── __init__.py     # 调度器初始化
│   │       └── member_score_sched.py  # 成员评分定时任务
│   │
│   ├── utils/                  # 工具函数
│   │   ├── auth.py             # 认证相关工具
│   │   ├── constant.py         # 常量定义
│   │   ├── database.py         # 数据库工具函数
│   │   ├── logger.py           # 日志工具
│   │   ├── response.py         # API响应格式化
│   │   ├── task_parser.py      # 任务解析工具
│   │   └── utils.py            # 通用工具函数
│   │
│   ├── views/                  # 视图层，定义API路由
│   │   ├── __init__.py         # 蓝图注册
│   │   └── user.py             # 用户相关API路由
│   │
│   └── __init__.py             # 应用初始化和配置
│
├── config/                     # 配置文件
│   ├── __init__.py             # 配置初始化
│   ├── development.py          # 开发环境配置
│   └── production.py           # 生产环境配置
│
├── migrations/                 # 数据库迁移文件(Flask-Migrate)
│   └── ...                     # 自动生成的迁移脚本
│
├── dist/                       # 前端构建文件
│   └── ...                     # 前端静态资源
│
├── public/                     # 静态资源文件
│   └── ...                     # 如图片、样式表等
│
├── uploads/                    # 文件上传目录
│   └── ...                     # 用户上传的文件
│
├── .venv/                      # Python虚拟环境
│   └── ...                     # 虚拟环境文件
│
├── app.log                     # 应用日志文件
├── requirements.txt            # 依赖包列表
└── run.py                      # 应用入口，启动Flask服务器
```

### 核心目录与文件详解

#### 应用入口
- **run.py**: 应用程序入口点，负责创建和启动Flask应用

#### 应用核心(app/)
- **app/__init__.py**: 应用初始化，包括Flask应用创建、扩展初始化、蓝图注册等
- **app/views/**: 处理HTTP请求，定义API端点，路由请求到相应控制器
- **app/controllers/**: 包含业务逻辑，处理从视图传来的请求，与模型交互
- **app/models/**: 数据模型定义，反映数据库表结构，使用SQLAlchemy ORM
- **app/utils/**: 存放辅助函数，如响应格式化、日志记录、认证工具等
- **app/modules/**: 应用的各个功能模块，如JWT认证、定时任务等

#### 配置(config/)
- **config/__init__.py**: 配置初始化
- **config/development.py**: 开发环境配置
- **config/production.py**: 生产环境配置

#### 静态资源与前端
- **dist/**: 前端构建文件，通常由前端框架(如React, Vue)生成
- **public/**: 静态资源文件，如图片、样式表等

#### 系统核心功能
- **JWT认证**: 使用Flask-JWT-Extended实现的认证系统
- **数据库连接**: 使用SQLAlchemy实现的数据库ORM
- **定时任务**: 使用APScheduler实现的任务调度系统
- **日志系统**: 配置日志记录，输出到控制台和文件

## 功能特性

- 用户认证与授权（JWT）
- 部门管理
- 成员管理
- 通知系统
- 定时任务
- 跨域支持
- 文件上传/下载
- 日志系统

## 安装与运行

### 环境要求

- Python 3.8+
- MySQL 5.7+

### 安装步骤

1. 克隆仓库
```bash
git clone https://github.com/yourusername/oa后端框架.git
cd oa后端框架
```

2. 创建并激活虚拟环境
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/Mac
source .venv/bin/activate
```

3. 安装依赖
```bash
pip install -r requirements.txt
```

4. 配置环境变量
创建 `.env` 文件，包含以下配置：
```
SECRET_KEY=your_secret_key
DATABASE_URL=mysql://username:password@localhost/dbname
OPENAI_API_KEY=your_openai_api_key (可选)
```

5. 初始化数据库
```bash
flask db init
flask db migrate
flask db upgrade
```

6. 运行应用
```bash
python run.py
```

应用将在 http://localhost:5002 运行。

## API文档

主要API路由包含：

- 用户认证：`/api/auth/login`、`/api/auth/register`
- 用户管理：`/api/user`
- 部门管理：`/api/department`
- 通知管理：`/api/notification`

## 开发团队

- 您的名字/团队名称

## 许可证

[请在此处添加许可证信息]