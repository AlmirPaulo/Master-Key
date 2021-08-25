from flask import request, url_for, redirect
from werkzeug.security import generate_password_hash
from . import db
from .pass_gen import generate_password
from .models import Master_Password


abc = 'qwertyuiopasdfghjklzxcvbnm'

def validations(tested_string, check_string):
    # if db_check:
    #     return f'You already have a Master Password. {db_check}'

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
    mp = request.form.get('mp')
    repeat_mp = request.form.get('repeat-mp')
    hint = request.form.get('hint')

    if validations(mp, repeat_mp) == 'OK':
        pass
        #here goes the register process
    else:
        return validations(mp, repeat_mp)
