import cgi
import os

from google.appengine.api import users

from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.db import djangoforms

from org.netmelody.slcmonitor.domain.lender import Lender
from org.netmelody.slcmonitor.domain.borrower import Borrower
from org.netmelody.slcmonitor.domain.ratechange import RateChange
from org.netmelody.slcmonitor.domain.rate import Rate

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

class RateChangeForm(djangoforms.ModelForm):
    class Meta:
        model = RateChange
        fields = ['startDate']
    rateValue = djangoforms.forms.IntegerField()
        
class EditLender(webapp.RequestHandler):
    def get(self):
        lender = Lender.get(self.request.get('lenderKey'))
        
        template_values = {
            'lender': lender,
            'form': RateChangeForm(),
        }
    
        path = os.path.join(os.path.dirname(__file__), '../templates/ratechangelist.html')
        self.response.out.write(template.render(path, template_values))

class AddRateChange(webapp.RequestHandler):
    def post(self):
        data = RateChangeForm(data=self.request.POST)
        if data.is_valid():
            rateChange = data.save(commit=False)
        
            rate = Rate()
            rate.value = data._cleaned_data()['rateValue']
            rate.put()
        
            rateChange.lender = Lender.get(self.request.get('lenderKey'))
            rateChange.rate = rate
            rateChange.put()
        self.redirect('/editlender?lenderKey=%s' % rateChange.lender.key())
       
class DeleteRateChange(webapp.RequestHandler):
    def post(self):
        rateChange = RateChange.get(self.request.get('rateChangeKey'))
        rateChange.delete()
        self.redirect('/editlender?lenderKey=%s' % rateChange.lender.key())

class EditRateChange(webapp.RequestHandler):
    def get(self):
        rateChange = RateChange.get(self.request.get('rateChangeKey'))
        form = RateChangeForm(instance=rateChange)
        
        template_values = {
            'rateChange': rateChange,
            'form': RateChangeForm()
        }
    
        path = os.path.join(os.path.dirname(__file__), '../templates/editratechange.html')
        self.response.out.write(template.render(path, template_values))
    def post(self):
        data = RateChangeForm(data=self.request.POST)
        if data.is_valid():
            rateChange = data.save(commit=False)
        
            existingRateChange = RateChange.get(self.request.get('rateChangeKey'))
            
            existingRateChange.rate.value = data._cleaned_data()['rateValue']
            existingRateChange.rate.put()
        
            existingRateChange.startDate = rateChange.startDate
            existingRateChange.put()
        self.redirect('/editlender?lenderKey=%s' % existingRateChange.lender.key())