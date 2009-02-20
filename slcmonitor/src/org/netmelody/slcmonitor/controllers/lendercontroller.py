import cgi
import os

from google.appengine.api import users
from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.db import djangoforms

from org.netmelody.slcmonitor.domain.lender import Lender
from org.netmelody.slcmonitor.domain.ratechange import RateChange
from org.netmelody.slcmonitor.domain.rate import Rate

from org.netmelody.slcmonitor.controllers.ratechangecontroller import RateChangeForm

class ManageLenders(webapp.RequestHandler):
  def get(self):
    lenders = Lender.gql('')
    
    template_values = {
      'lenders': lenders
    }
    
    path = os.path.join(os.path.dirname(__file__), '../templates/lenderlist.html')
    self.response.out.write(template.render(path, template_values))

class AddLender(webapp.RequestHandler):
    def post(self):
        lender = Lender()
        lender.name = self.request.get('lenderName')
        lender.put()
        self.redirect('/lenders')
        
class DeleteLender(webapp.RequestHandler):
    def post(self):
        lender = Lender.get(self.request.get('lenderKey'))
        lender.delete()
        self.redirect('/lenders')

class EditLender(webapp.RequestHandler):
    def get(self):
        lender = Lender.get(self.request.get('lenderKey'))
        
        template_values = {
            'lender': lender,
            'form': RateChangeForm()
        }
    
        path = os.path.join(os.path.dirname(__file__), '../templates/ratechangelist.html')
        self.response.out.write(template.render(path, template_values))
