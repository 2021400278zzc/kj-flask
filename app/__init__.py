import logging
import os
from flask import Flask, send_from_directory
from flask_cors import CORS
from app.modules.jwt import jwt
from app.modules.logger import console_handler, file_handler
from app.modules.sql import db, migrate
from app.views import register_blueprints
from config import Config
from app.modules.sched import init_schedulers


def create_app() -> Flask:
    """创建app必要的操作"""
    app = Flask(__name__, static_folder='../dist/', static_url_path='/')
    app.config.from_object(Config)

    # 配置 CORS，允许所有源和所有请求头
    CORS(app, 
        resources={r"/*": {
            "origins": "*",  # 允许所有源
            "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
            "allow_headers": "*",  # 允许所有请求头
            "supports_credentials": True
        }})

    jwt.init_app(app)

    db.init_app(app)
    migrate.init_app(app, db)
    
    # 注册所有蓝图
    register_blueprints(app)

    # 获取项目根目录路径
    root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    # 配置静态文件路由
    @app.route('/public/<path:filename>')
    def public_files(filename):
        return send_from_directory(os.path.join(root_path, 'public'), filename)
    @app.route('/')
    def serve_index():
        return send_from_directory('../dist', 'index.html')
    
    @app.route('/<path:filename>')
    def serve_static(filename):
        return send_from_directory('../dist', filename)

    # # 初始化所有定时任务调度器
    # schedulers = init_schedulers(app)
    # app.schedulers = schedulers  # 可选：将调度器保存在app对象中，以便后续访问

    app.logger.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.addHandler(console_handler)

    return app
