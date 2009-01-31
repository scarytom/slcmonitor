import lender
import rate
from google.appengine.ext import db

class RateChange(db.Model):
    startDate = db.DateProperty()
    rate = db.ReferenceProperty(Rate)
    lender = db.ReferenceProperty(Lender, collection_name='rateChanges')