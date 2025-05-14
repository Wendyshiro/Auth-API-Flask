import os
from flask import Flask
from config import Config
from app.models import db
from app.routes.auth_routes import auth_bp
from flask_jwt_extended import JWTManager

jwt = JWTManager()
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    print("DB URI:", app.config.get("SQLALCHEMY_DATABASE_URI"))
    db.init_app(app)
    jwt.init_app(app)
    app.register_blueprint(auth_bp, url_prefix='/api/auth')

    return app


