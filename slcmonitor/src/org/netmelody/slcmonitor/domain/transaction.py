import ledger
import money
from google.appengine.ext import db

class Transaction(db.Model):
    date = db.DateProperty()
    amount = db.ReferenceProperty(Money)
    ledger = db.ReferenceProperty(Ledger, collection_name='transactions')