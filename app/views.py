from flask import render_template, request
from . import app
from .register import create_mp

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if  request.method == 'POST':
        return create_mp()


    return render_template('register.html')
