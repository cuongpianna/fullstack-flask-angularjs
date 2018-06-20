from datetime import datetime

from sqlalchemy import null

from app import db


def getdate():
    return datetime.now()

class Users(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(64),unique=True)
    email = db.Column(db.String(64),unique=True)
    password_hash = db.Column(db.String(255))
    avartar = db.Column(db.String(255))
    date_of_birth = db.Column(db.DATE,nullable=True,default=getdate())
    timestamp = db.Column(db.Date,default=getdate())
