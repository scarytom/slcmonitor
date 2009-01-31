from lender import Lender
from rate import Rate
from google.appengine.ext import db

class RateChange(db.Model):
    startDate = db.DateProperty()
    rate = db.ReferenceProperty(Rate)
    lender = db.ReferenceProperty(Lender, collection_name='rateChanges')