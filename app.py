import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
import flask.ext.restless

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
db = SQLAlchemy(app)
session = db.sessionmaker(bind=db.get_engine())

# Create our database model
class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    balance = db.Column(db.Float)
    transactions = db.relationship("Transaction", backref='user', lazy=True)

    def __init__(self, id, name, balance):
        self.id = id
        self.name = name
        self.balance = balance

class Transaction(db.Model):
    __tablename__ = 'transaction'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    amount = db.Column(db.Float)
    company = db.Column(db.String)
    time = db.Column(db.DateTime)

db.create_all()

manager = flask.ext.restless.APIManager(app, flask_sqlalchemy_db=db)

manager.create_api(User, methods=['GET', 'POST', 'PATCH' 'DELETE'], allow_patch_many=True, allow_delete_many=True)
manager.create_api(Transaction, methods=['GET', 'POST', 'DELETE'])




if __name__ == '__main__':
    app.debug = True
    app.run()