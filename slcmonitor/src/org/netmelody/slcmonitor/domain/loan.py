import borrower
import lender
import ledger
from google.appengine.ext import db

class Loan(db.Model):
    title = db.StringProperty()
    lender = db.ReferenceProperty(Lender)
    borrower = db.ReferenceProperty(Borrower, collection_name='loans')
    withdrawals = db.ReferenceProperty(Ledger)
    datedRepayments = db.ReferenceProperty(Ledger)
    distributedRepayments = db.ReferenceProperty(Ledger)