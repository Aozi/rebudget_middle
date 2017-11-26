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



transactions = json.load(open("output.json"))

02/05/2017

for trans in transactions:
    #print trans['place']
    #print float(trans['amount'])
    #print trans['categories']
    d = trans[datetime.datetime.strptime(trans['date'], "%d/%m/%Y")]
    print d

    r = requests.post("https://intense-shore-10684.herokuapp.com/api/transaction", json={
        'user_id': 1,
        'amount': float(trans['amount']),
        'company': trans['place'],
        'category':trans['categories'],
        'date': trans[datetime.datetime.strptime(trans['date'], "%d/%m/%Y")]})