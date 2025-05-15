from flask import Flask

from .user import user_bp

def register_blueprints(app: Flask) -> None:
    """注册所有蓝图至Flask中"""
    app.register_blueprint(user_bp)

