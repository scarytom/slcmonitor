import core

from transaction import Withdrawal
from transaction import DatedRepayment
from transaction import DistributedRepayment

from google.appengine.ext import db

class Loan(core.AbstractLoan):
    title = db.StringProperty()
    
    def _createTransaction(self, transaction, date, amount):
        transaction.amount = amount
        transaction.date = date
        transaction.loan = self
        transaction.put()
    
    def makeWithdrawal(self, date, amount):
        self._createTransaction(Withdrawal(), date, amount)

    def makeDatedRepayment(self, date, amount):
        self._createTransaction(DatedRepayment(), date, amount)
        
    def makeDistributedRepayment(self, date, amount):
        self._createTransaction(DistributedRepayment(), date, amount)
