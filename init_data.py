from app import bank_User, Transaction, db

new_user = bank_User(name="test",balance=10000)

db.session.add(new_user)
db.session.commit()
