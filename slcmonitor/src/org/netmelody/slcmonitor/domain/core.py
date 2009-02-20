from google.appengine.ext import db
from google.appengine.ext.db import polymodel

class AbstractBase(polymodel.PolyModel):
    None

class AbstractBorrower(AbstractBase):
    None

class AbstractLender(AbstractBase):
    None
    
class AbstractLoan(AbstractBase):
    lender = db.ReferenceProperty(AbstractLender, collection_name='loans')
    borrower = db.ReferenceProperty(AbstractBorrower, collection_name='loans')
    
class AbstractRate(AbstractBase):
    None

class AbstractRateChange(AbstractBase):
    rate = db.ReferenceProperty(AbstractRate, collection_name='rateChanges')
    lender = db.ReferenceProperty(AbstractLender, collection_name='rateChanges')
    
class AbstractTransaction(AbstractBase):
    loan = db.ReferenceProperty(AbstractLoan, collection_name='transactions')