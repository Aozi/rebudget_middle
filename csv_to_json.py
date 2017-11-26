import csv
import json
import requests
import datetime


#with open('transactions.csv') as f:
#    columns = ("date", "amount", "place", "categories")
#    reader = csv.DictReader(f, columns)
#    rows = list(reader)
#with open('output.json', 'w') as f:
#    json.dump(rows, f, indent=4)



#transactions = json.load(open("output.json"))

#for trans in transactions:
#    r = requests.post("https://intense-shore-10684.herokuapp.com/api/transaction", json={
#        'user_id': 1,
#        'amount': float(trans['amount']),
#        'company': trans['place'],
#        'category':trans['categories'],
#        'time': trans['date']
#    })
#    print(r.status_code, r.reason)