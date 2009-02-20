import core

from google.appengine.ext import db
from google.appengine.ext.db import polymodel

class Transaction(core.AbstractTransaction):
  date = db.DateProperty()
  amount = db.IntegerProperty()
    
class Withdrawal(Transaction):
  None

class DatedRepayment(Transaction):
  None

class DistributedRepayment(Transaction):
  None