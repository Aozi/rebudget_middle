from app import db, User, Transaction

i = user.insert()
i.execute({id:1}, {id:2}, {id:3})

i2 = transaction.insert()
i2.execute(
	{
	"id":0, 
	"user_id":1,
	"amount":100,
	"company":"K Kauppa"
	},

	{
	"id":1, 
	"user_id":1,
	"amount":20,
	"company":"K Kauppa"
	},


	{
	"id":2, 
	"user_id":1,
	"amount":32,
	"company":"K Kauppa"
	},


	{
	"id":3, 
	"user_id":1,
	"amount":10,
	"company":"K Kauppa"
	},

	{
	"id":4, 
	"user_id":1,
	"amount":300,
	"company":"K Kauppa"

	}

	)