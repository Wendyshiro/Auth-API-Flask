# config.py
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    JWT_SECRET_KEY ='your_jwt_secret_key'
    SECRET_KEY = os.environ.get('SECRET_KEY', 'supersecretkey')
    SQLALCHEMY_DATABASE_URI = os.environ.get='sqlite:///' +os.path.join(basedir,'site.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
