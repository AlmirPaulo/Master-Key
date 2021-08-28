from . import db

class Master_Password(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    mp = db.Column(db.String(), unique=True, nullable=False)
    hint = db.Column(db.String(255), unique=True, nullable=False) 

    def __repr__(self):
        return f'<Master_Password {self.mp} - {self.hint}>'

    def is_active(self):
        return True

    def is_authenticated(self):
        return True
    
    def get_id(self):
        return self.id

class Passwords(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    services = db.Column(db.String(255), unique=True, nullable=False) 

    passwords = db.Column(db.String(), unique=True, nullable=False) 

    def __repr__(self):
        return f'<Passwords {self.services}:{self.passwords}>'

