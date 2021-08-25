from . import db

class Master_Password(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    mp = db.Column(db.String(), unique=True, nullable=False)
    hint = db.Column(db.String(255), unique=True, nullable=False) 

class Passwords(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    services = db.Column(db.String(255), unique=True, nullable=False) 

    passwords = db.Column(db.String(), unique=True, nullable=False) 

