import os
from app import create_app
from config import Config
import logging
import sys
import pymysql
pymysql.install_as_MySQLdb()
# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler('app.log', encoding='utf-8')
    ]
)

port = os.getenv("PORT")
app = create_app()

if __name__ == "__main__":
    try:
        # 启动 Flask 应用
        app.run(
            host="0.0.0.0", 
            port=5002, 
            debug=True,
            use_reloader=False
        )
    except Exception as e:
        logging.error(f"应用启动失败: {str(e)}", exc_info=True)
        raise
    
