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
class bank_User(db.Model):
    __tablename__ = "bank_user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    balance = db.Column(db.String)
    transactions = db.relationship("Transaction", backref='bank_user', lazy=True)

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

class Transaction(db.Model):
    __tablename__ = 'transaction'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('bank_user.id'))
    amount = db.Column(db.String)
    company = db.Column(db.String)
    time = db.Column(db.String)
    category = db.Column(db.String)

db.create_all()

manager = flask.ext.restless.APIManager(app, flask_sqlalchemy_db=db)

manager.create_api(bank_User, methods=['GET', 'POST', 'PATCH' 'DELETE'], max_page_size=0, allow_patch_many=True, allow_delete_many=True)
manager.create_api(Transaction, methods=['GET', 'POST', 'DELETE'], max_page_size=0)

if __name__ == '__main__':
    app.debug = True
    app.run()