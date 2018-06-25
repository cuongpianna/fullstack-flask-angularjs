from flask import session,render_template

from ..models.Users import Users
from . import auth

@auth.route('/login')
def login():
    return render_template('auth/login.html')