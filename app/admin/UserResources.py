import os,werkzeug
from math import floor
from flask import request,jsonify,json, make_response

from flask_restful import Resource,marshal_with,reqparse
from flask_marshmallow import Schema
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage

from ..models.Users import Users
from app import ma,db, UPLOAD_FOLDER


class UserSchema(ma.ModelSchema):
    class Meta:
        model = Users
        fields = ('id','username','email','date_of_birth','avartar','timestamp')

userschema = UserSchema()
userschema = UserSchema(many=True)

parser = reqparse.RequestParser()
parser.add_argument('username',help = 'Không được trống trường này', required = True)
parser.add_argument('email',help = 'Không được trống trường này', required = True)
parser.add_argument('password',help = 'Không được trống trường này', required = True)
parser.add_argument('date_ob_birth')
parser.add_argument('avartar',type=werkzeug.datastructures.FileStorage,location='files')


class UsersResource(Resource):
    def get(self):
        limit = int(request.args.get('limit')) if request.args.get('limit') else 5
        offset = int(request.args.get('offset')) if request.args.get('offset') else 1
        users = Users.query.all()[(limit*(offset-1)):(limit*(offset-1)+limit)]
        total_users = len(Users.query.all())
        if type(total_users/limit) == int:
            last_page = floor(total_users / limit)
        else:
            last_page = floor(total_users / limit ) + 1
        #last_page = len(Users.query.all())/limit
        return jsonify({
            'last_page': last_page,
            'offset': offset,
            'limit': limit,
            'data':userschema.dump(users)
        })

    def post(self):
        data = parser.parse_args()
        user = Users.query.filter_by(username=data['username']).first()
        file = data['avartar']

        if user:
           return jsonify({'msg':'Tai khoan nay da ton tai'})
        user = Users.query.filter_by(email=data['email']).first()

        if user:
           return jsonify({'msg':'Email nay da ton tai'})

        if file:
            file.save(os.path.join(UPLOAD_FOLDER, file.filename))

        user = Users(username=data['username'],password_hash=data['password'],email=data['email'],avartar=os.path.join(UPLOAD_FOLDER,secure_filename(file.filename)))
        db.session.add(user)
        db.session.commit()
        return jsonify({'msg':'Tao tai khoan thanh cong'})


    def delete(self):
        Users.query.delete()
        db.session.commit()
        return jsonify({'msg':"Xoa thanh cong"})

class UserResource(Resource):
    def delete(self,id):
        user = Users.query.get(id)
        if user:
            db.session.delete(user)
            db.session.commit()
            msg = "Xoa thanh cong"
        else:
            msg = "Khong ton tai tai khoan"
        return jsonify({'msg':msg})

