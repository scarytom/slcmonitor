from google.appengine.ext import db

class Lender(db.Model):
    name = db.StringProperty
    # List of rate changes