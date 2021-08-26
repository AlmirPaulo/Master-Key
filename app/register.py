from flask import request, url_for, redirect
from werkzeug.security import generate_password_hash
from . import db
from .models import Master_Password

abc = 'qwertyuiopasdfghjklzxcvbnm'

def validations(tested_string, check_string):
    db_check = Master_Password.query.filter_by(id=1).first()
    if db_check:
        return f'You already have a Master Password.'

    if any(i in tested_string for i in '0123456789') == False:
        return 'Your Master Password must to be alpanumeric.'

    elif any(i in tested_string for i in abc) == False:
        return 'Your Master Password must to be alpanumeric.'

    elif any(i in tested_string for i in abc.upper()) == False:
        return 'Your Master Password must to have uppercase and lowercase letters.'

    elif len(tested_string) < 8:
        return 'Your Master Password must to be at least 8 characters longer.'
    
    elif tested_string != check_string:
        return 'Passwords do not match.'
    
    else:
        return 'OK'


def create_mp():
    data = request.get_json()
    print(data)
    mp = data['mp']
    hint = data['hint']
    repeat_mp = data['repeat_mp']

    if validations(mp, repeat_mp) == 'OK':

        db.session.add(Master_Password(mp=generate_password_hash(mp, 'sha256'), hint=hint))
        db.session.commit()
        return 'Master Password created Succesfully!\nNow you may Login.'
    else:
        return validations(mp, repeat_mp)
