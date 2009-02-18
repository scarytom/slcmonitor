from borrower import Borrower
from lender import Lender
from transaction import Withdrawal
from transaction import DatedRepayment
from transaction import DistributedRepayment
from google.appengine.ext import db

class Loan(db.Model):
    title = db.StringProperty()
    lender = db.ReferenceProperty(Lender, collection_name='loans')
    borrower = db.ReferenceProperty(Borrower, collection_name='loans')
    
    def makeWithdrawal(self, date, amount):
        __createTransaction(Withdrawal(), date, amount)

    def makeDatedRepayment(self, date, amount):
        __createTransaction(DatedRepayment(), date, amount)
        
    def makeDistributedRepayment(self, date, amount):
        __createTransaction(DistributedRepayment(), date, amount)
        
    def __createTransaction(self, transaction, date, amount):
        transaction.amount = amount
        transaction.date = date
        transaction.loan = self
        transaction.put()