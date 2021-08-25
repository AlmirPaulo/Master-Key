from flask import Flask

app = Flask(__name__)



#Factory
def create_app():
    from .views import home 
    return app
