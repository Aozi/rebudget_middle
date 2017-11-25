from flask import Flask, request, jsonify
from flask.sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/INSERT_URL'
db = SQLAlchemy(app)

# Create our database model
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    transactions = relationship("Transaction")

    def __init__(self, id):
        self.id = id

class Transaction(db.Model):
    __tablename__ = 'transaction'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'))
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


# endpoint to show all users
@app.route("/user", methods=["GET"])
def get_user():
    all_users = User.query.all()
    result = users_schema.dump(all_users)
    return jsonify(result.data)

# endpoint to get user detail by id
@app.route("/user/<id>", methods=["GET"])
def user_detail(id):
    user = User.query.get(id)
    return user_schema.jsonify(user)



if __name__ == '__main__':
    app.debug = True
    app.run()