from maple_app.routes.home import home_bp

def register_blueprints(app):
    """모든 Blueprint를 Flask 앱에 등록"""
    app.register_blueprint(home_bp)
    # app.register_blueprint(api_bp)  # 추후 API 라우터 추가
