import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy import text
from sqlalchemy.orm import relationship
import flask.ext.restless

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
db = SQLAlchemy(app)
ma = Marshmallow(app)
session = db.sessionmaker(bind=db.get_engine())

# Create our database model
class bank_User(db.Model):
    __tablename__ = "bank_user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    balance = db.Column(db.Float)
    transactions = db.relationship("Transaction", backref='bank_user', lazy=True)

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

class Transaction(db.Model):
    __tablename__ = 'transaction'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('bank_user.id'))
    amount = db.Column(db.Float)
    company = db.Column(db.String)
    time = db.Column(db.DateTime)
    category = db.Column(db.String)

db.create_all()

#manager = flask.ext.restless.APIManager(app, flask_sqlalchemy_db=db)

#manager.create_api(bank_User, methods=['GET', 'POST', 'PATCH' 'DELETE'], allow_patch_many=True, allow_delete_many=True)
#manager.create_api(Transaction, methods=['GET', 'POST', 'DELETE'])

class bank_UserSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id','name', 'balance','transactions')

class TransactionSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id', 'user_id','amount','company','time','category')


user_schema = bank_UserSchema()
users_schema = bank_UserSchema(many=True)

tran_schema = TransactionSchema()
trans_schema = TransactionSchema(many=True)


# endpoint to create new user
@app.route("/user", methods=["POST"])
def add_user():
    name = request.json['name']
    balance = request.json['balance']

    new_user = bank_User(name, balance)

    db.session.add(new_user)
    db.session.commit()

    return jsonify(new_user)


# endpoint to show all users
#@app.route("/user", methods=["GET"])
#def get_user():
#    all_users = bank_User.query.all()
#    result = users_schema.dump(all_users)
#    return jsonify(result.data)


@app.route("/transaction",methods=["POST"])
def add_transaction():
    user_id = request.json['user_id']
    amount = request.json['amount']
    company = request.json['company']
    time = request.json['time']
    category = request.json['category']

    new_transaction = Transaction(user_id,amount,company,time,category)

    db.session.add(new_transaction)
    db.session.commit()

    return jsonify(new_transaction)

@app.route("/transaction",methods=["GET"])
def get_transactions():
    all_transactions = Transaction.query.all()
    result = trans_schema.dump(all_transactions)
    return jsonify(result.data)

@app.route("/golden_value",methods=['GET'])
def get_golden_value():
    #Use the machine learning algorithms here to analyze the database and find a proper golden value




if __name__ == '__main__':
    app.debug = True
    app.run()