from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)
    
    # Đăng ký các route
    from .routes import register_routes
    register_routes(app)
    
    return app
