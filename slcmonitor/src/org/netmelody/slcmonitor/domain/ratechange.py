import core

from google.appengine.ext import db

class RateChange(core.AbstractRateChange):
    startDate = db.DateProperty()