from borrower import Borrower
from lender import Lender
from ledger import Ledger
from google.appengine.ext import db

class Loan(db.Model):
    title = db.StringProperty()
    lender = db.ReferenceProperty(Lender, collection_name='loans')
    borrower = db.ReferenceProperty(Borrower, collection_name='loans')
    withdrawals = db.ReferenceProperty(Ledger, collection_name='loan_w')
    datedRepayments = db.ReferenceProperty(Ledger, collection_name='loan_r')
    distributedRepayments = db.ReferenceProperty(Ledger, collection_name='loan_dr')