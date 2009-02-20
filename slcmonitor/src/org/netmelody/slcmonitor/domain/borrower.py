import core

from google.appengine.ext import db

class Borrower(core.AbstractBorrower):
  identity = db.UserProperty()
  # Collection of Loans