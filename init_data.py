from app import bank_User, Transaction, db

new_user = bank_User(name="test",balance=10000)
new_tr = Transaction(user_id=0,amount=100,company="blah",categor="luxury")

new_user.transactions.append(new_tr)
db.session.add(new_user)
db.session.commit()
