import core

from google.appengine.ext import db
from google.appengine.ext.db import polymodel

class Transaction(core.AbstractTransaction):
  date = db.DateProperty()
  amount = db.IntegerProperty()
  
  def type(self):
      return self.__class__.__name__
    
class Withdrawal(Transaction):
  None

class DatedRepayment(Transaction):
  None

class DistributedRepayment(Transaction):
  None