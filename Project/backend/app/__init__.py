from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app) # Cho phép cross-origin requests

    # Đăng ký các routes
    from app.routes import api_bp
    app.register_blueprint(api_bp)

    return app
