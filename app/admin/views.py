from flask import render_template

from . import users

@users.route('/admin')
def users():
    return render_template('admin.html')