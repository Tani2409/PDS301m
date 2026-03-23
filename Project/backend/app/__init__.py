from flask import Flask
from flask_cors import CORS
from flasgger import Swagger

def create_app():
    app = Flask(__name__)
    CORS(app)
    Swagger(app)
    
    # Đăng ký Blueprint từ routes.py
    from .routes import api_bp
    app.register_blueprint(api_bp)
    
    return app
