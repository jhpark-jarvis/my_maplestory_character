import os
from flask import Flask

app = Flask(__name__,
            template_folder=os.path.join(os.path.dirname(__file__), 'templates'),
            static_folder=os.path.join(os.path.dirname(__file__), 'static'))

# Blueprint 등록
from maple_app.routes import register_blueprints
register_blueprints(app)