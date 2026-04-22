import os
from flask import Flask
from config import Config

app = Flask(__name__,
            template_folder=os.path.join(os.path.dirname(__file__), 'templates'),
            static_folder=os.path.join(os.path.dirname(__file__), 'static'))

# 설정 로드 (세션 사용을 위해 필수)
app.config.from_object(Config)

# Blueprint 등록
from maple_app.routes import register_blueprints
register_blueprints(app)