from loan import Loan
from google.appengine.ext import db
from google.appengine.ext.db import polymodel

class Transaction(polymodel.PolyModel):
  date = db.DateProperty()
  amount = db.IntegerProperty()
  loan = db.ReferenceProperty(Loan, collection_name='transactions')
    
class Withdrawal(Transaction):
  None

class DatedRepayment(Transaction):
  None

class DistributedRepayment(Transaction):
  None