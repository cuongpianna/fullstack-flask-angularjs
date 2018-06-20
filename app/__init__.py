import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api
from flask_cors import CORS

UPLOAD_FOLDER = os.path.realpath('.') + '/uploads'

db = SQLAlchemy()
# api = Api()
ma = Marshmallow()

from config import config
from .models import Users
from .admin.UserResources import UsersResource, UserResource



def create_app(config_name):
    app = Flask(__name__,template_folder='templates')
    CORS(app,supports_credentials=True)
    app.config.from_object(config[config_name])
    db.init_app(app)
    ma.init_app(app)
    cor = CORS(app,resources={r"*": {"origins": "*"}})
    api = Api(app)
    api.add_resource(UsersResource,'/users')
    api.add_resource(UserResource,'/users/<id>')

    from .admin import users as users_admin
    app.register_blueprint(users_admin)

    return app