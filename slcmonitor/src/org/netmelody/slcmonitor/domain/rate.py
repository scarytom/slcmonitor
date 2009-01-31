from google.appengine.ext import db

class Rate(db.Model):
    value = db.IntegerProperty()