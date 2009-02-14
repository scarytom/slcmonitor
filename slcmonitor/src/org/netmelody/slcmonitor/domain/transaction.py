from ledger import Ledger
from google.appengine.ext import db

class Transaction(db.Model):
    date = db.DateProperty()
    amount = db.IntegerProperty()
    ledger = db.ReferenceProperty(Ledger, collection_name='transactions')