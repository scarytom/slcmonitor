from borrower import Borrower
from lender import Lender
from google.appengine.ext import db

class Loan(db.Model):
    title = db.StringProperty()
    lender = db.ReferenceProperty(Lender, collection_name='loans')
    borrower = db.ReferenceProperty(Borrower, collection_name='loans')
