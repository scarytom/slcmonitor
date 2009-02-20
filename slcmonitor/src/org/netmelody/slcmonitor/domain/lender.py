import core

from google.appengine.ext import db

class Lender(core.AbstractLender):
    name = db.StringProperty()
    # List of rate changes
    
    def currentRate(self):
        latest = None
        for rateChange in self.rateChanges:
            if (latest == None) or (latest.startDate == None) or (rateChange.startDate > latest.startDate):
                latest = rateChange
        
        if latest:
            return latest.rate.value
            
            #q = RateChange.all()
            #q.filter(lender, self)
            #q.order(-startDate)
            #return q.fetch(1)[0]