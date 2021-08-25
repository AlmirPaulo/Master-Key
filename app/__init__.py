from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
import os

app = Flask(__name__)
jwt = JWTManager()
db = SQLAlchemy()

def create_db():
    if os.path.exists('./passwords.db') == False:
        with app.app_context():
            return db.create_all()


#Factory
def create_app():
    from .views import home, login, register
    from .models import Master_Password, Passwords 
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./passwords.db'
    app.config['JWT_SECRET_KEY'] = str(os.urandom(24))
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['DEBUG'] = True
    app.config['ENV'] = 'development'

    db.init_app(app)
    jwt.init_app(app)
    create_db()

    return app
