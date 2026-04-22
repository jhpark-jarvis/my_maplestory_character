from maple_app import app
from config import Config

if __name__ == '__main__':
    app.config.from_object(Config)
    app.config['JSON_AS_ASCII'] = False  # JSON 응답에서 한글이 깨지지 않도록 설정
    app.run(debug=True)