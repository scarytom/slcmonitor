from google.appengine.ext import db
#from ratechange import RateChange

class Lender(db.Model):
    name = db.StringProperty()
    # List of rate changes
    
#    def currentRate(self):
#        q = RateChange.all()
#        q.filter(lender, self)
#        q.order(-startDate)
#        
#        return q.fetch(1)[0]