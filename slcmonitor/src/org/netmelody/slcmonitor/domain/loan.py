from borrower import Borrower
from lender import Lender
from google.appengine.ext import db

class Loan(db.Model):
    title = db.StringProperty()
    lender = db.ReferenceProperty(Lender, collection_name='loans')
    borrower = db.ReferenceProperty(Borrower, collection_name='loans')
    
    def makeWithdrawal(self, date, amount):
        transactionModule = __import__('transaction')
        __createTransaction(transactionModule.Withdrawal(), date, amount)

    def makeDatedRepayment(self, date, amount):
        transactionModule = __import__('transaction')
        __createTransaction(transactionModule.DatedRepayment(), date, amount)
        
    def makeDistributedRepayment(self, date, amount):
        transactionModule = __import__('transaction')
        __createTransaction(transactionModule.DistributedRepayment(), date, amount)
        
    def __createTransaction(self, transaction, date, amount):
        transaction.amount = amount
        transaction.date = date
        transaction.loan = self
        transaction.put()