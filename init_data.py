from app import User, Transaction, db

new_user = User(id=0)
new_tr = Transaction(id=0,user_id=0,amount=100,company="blah")
db.session.add(new_user)
db.session.add(new_tr)
db.session.commit()
