import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
db = SQLAlchemy(app)

# Create our database model
class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    transactions = db.relationship("Transaction", backref='user', lazy=True)

    def __init__(self, id):
        self.id = id

class Transaction(db.Model):
    __tablename__ = 'transaction'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    amount = db.Column(db.Float)
    company = db.Column(db.String)
    time = db.Column(db.DateTime)

# endpoint to create new user
@app.route("/user", methods=["POST"])
def add_user():
    user_id = request.json['id']

    new_user = User(user_id)

    db.session.add(new_user)
    db.session.commit()

    return jsonify(new_user)

# endpoint to create a transaction
@app.route("/transaction", methods=["POST"])
def add_transaction():
    trans_id = request.json('id')
    trans_user_id = request.json('user_id')
    trans_amount = request.json('amount')
    trans_company = request.json('company')
    trans_time = request.json('time')

    new_transaction = Transaction(trans_id, trans_user_id, trans_amount, trans_company, trans_time)

    db.session.add(new_transaction)
    db.session.commit()

# endpoint to show transactions by user
@app.route("/transaction/user/<id>", methods=["GET"])
def get_trans_by_user(q_user_id):
    all_transactions = Transaction.query(Transaction.user_id).filter(Transaction.user_id == q_user_id)
    result = transaction_schema.dump(all_transactions)
    return jsonify(result.data)

# endpoint to show all users
@app.route("/user", methods=["GET"])
def get_user():
    all_users = User.query.all()
    result = user_schema.dump(all_users)
    return jsonify(result.data)

# endpoint to get user detail by id
@app.route("/user/<id>", methods=["GET"])
def user_detail(id):
    user = User.query.get(id)
    return user_schema.jsonify(user)



if __name__ == '__main__':
    app.debug = True
    app.run()