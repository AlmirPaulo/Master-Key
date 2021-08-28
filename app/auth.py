from flask import redirect, url_for
from . import views
from flask_login import login_user, current_user
from .models import Master_Password
from werkzeug.security import check_password_hash
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s:%(module)s:%(levelname)s:%(message)s')

def verify_login(tested_passwd):
        master_passwd = Master_Password.query.filter_by(id=1).first()
        if master_passwd:
            if check_password_hash(master_passwd.mp, tested_passwd):
                if current_user.is_authenticated:
                    msg = 'You are already logged in.'
                    return msg
                else:
                    login_user(master_passwd)
                    msg = 'Logged in succesfully! Now you can see and create your passwords!'
                    return msg
            else:
                msg = 'Incorrect password.'
                return msg
        else:
            msg = 'You do not have a Master Password. Create one first.'
            return msg
