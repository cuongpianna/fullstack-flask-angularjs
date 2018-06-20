import os
from flask import request
from flask_script import Manager,Shell
from flask_migrate import Migrate, MigrateCommand
from flask_cors import CORS

from app import create_app,db

app = create_app('default')

@app.after_request
def set_allow_origin(resp):
    """ Set origin for GET, POST, PUT, DELETE requests """

    resp.headers['Access-Control-Allow-Origin'] = request.headers.get('Origin', '*')
    resp.headers['Access-Control-Allow-Credentials'] = 'true'
    resp.headers['Access-Control-Allow-Methods']     = 'POST, OPTIONS, GET, DELETE, PUT'
    resp.headers['Access-Control-Allow-Headers'] = request.headers.get(
        'Access-Control-Request-Headers', 'Authorization')
    if app.debug:
        resp.headers['Access-Control-Max-Age'] = '1'


    return resp
CORS(app)
manager = Manager(app)
migrate = Migrate(app,db)

manager.add_command("shell",Shell)
manager.add_command('db', MigrateCommand)

if __name__ == "__main__":
    manager.run()
