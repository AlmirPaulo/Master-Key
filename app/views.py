from flask import render_template, request, jsonify
from . import app
from .register import create_mp
from .auth import verify_login
from .models import Passwords, Master_Password


@app.route('/')
def home():
    return render_template('index.html')

#Retirar quando em produção
@app.route('/checkdb')
def check_db():
    db_out1 = []
    db_out2 = []
    db_dict = {'Master_Password':db_out1, 'Passwords':db_out2}
    for i in range(10):
        out1 = Master_Password.query.filter_by(id=i).first()
        out2 = Passwords.query.filter_by(id=i).first()
        db_out1.append(str(out1))
        db_out2.append(str(out2))

    return jsonify(db_dict)

@app.route('/hint')
def hint():
    mp = Master_Password.query.filter_by(id=1).first()
    return jsonify(mp.hint)


@app.route('/login', methods=['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST':
        mp = request.data.decode('utf-8')
        msg = verify_login(mp)

    return render_template('login.html', msg = msg)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        return create_mp()


    return render_template('register.html')
