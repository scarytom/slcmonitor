from google.appengine.ext import db

class Borrower(db.Model):
  identity = db.UserProperty()
  # Collection of Loans