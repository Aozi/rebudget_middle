import csv
import json
import requests
import pandas as pd

#with open('sdata.csv') as f:
#    columns = ("date", "amount", "place", "category")
#    reader = csv.DictReader(f, columns)
#    rows = list(reader)
#with open('output.json', 'w') as f:
#    json.dump(rows, f, indent=4)

transactions = json.load(open("output.json"))

for trans in transactions:
    amount_in_float = trans['amount']
    amount_in_float = amount_in_float.replace(",",".")
    print amount_in_float

