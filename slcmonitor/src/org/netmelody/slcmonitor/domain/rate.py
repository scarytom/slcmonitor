import core

from google.appengine.ext import db

class Rate(core.AbstractRate):
    value = db.IntegerProperty()