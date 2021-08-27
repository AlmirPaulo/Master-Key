from flask import redirect, url_for
from . import jwt
from .models import Master_Password
from werkzeug.security import check_password_hash

def verify_login(tested_passwd):
        mp = Master_Password.query.filter_by(id=1).first()
        if mp:
            if check_password_hash(mp.mp, tested_passwd):
                #jwt login
                try:
                    msg = 'Logged in succesfully!'
                    return msg
                finally:
                    redirect(url_for(...)) #redirect to main page
            else:
                msg = 'Incorrect password.'
                return msg
        else:
            msg = 'You do not have a Master Password. Create one first.'
            return msg
