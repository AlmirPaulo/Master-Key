from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os

app = Flask(__name__)
login_manager = LoginManager()
db = SQLAlchemy()


def create_db():
    if os.path.exists("./passwords.db") == False:
        with app.app_context():
            return db.create_all()


# Factory
def create_app():
    from .views import home, login, register
    from .models import Master_Password, Passwords

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///./passwords.db"
    app.config["SECRET_KEY"] = str(os.urandom(24))
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["DEBUG"] = True
    app.config["ENV"] = "development"

    CORS(app)
    db.init_app(app)
    login_manager.init_app(app)
    create_db()

    @login_manager.user_loader
    def load_user(id):
        return Master_Password.query.get(int(id))

    return app
