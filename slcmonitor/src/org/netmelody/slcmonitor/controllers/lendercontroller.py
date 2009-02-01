import cgi
import os

from google.appengine.api import users

from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app

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

class EditLender(webapp.RequestHandler):
    def get(self):
        lender = Lender.get(self.request.get('lenderKey'))
        self.response.out.write('<html><body>')
        self.response.out.write('Lender <b>%s</b>' % cgi.escape(lender.name))
        rateChanges = lender.rateChanges
        self.response.out.write('<ul>')
        for rateChange in rateChanges:
            self.response.out.write('<li>rate: %ld</li>' % rateChange.rate.value)
        self.response.out.write('</ul>')
        
        # Write the submission form and the footer of the page
        self.response.out.write("""
          <form action="/addratechange" method="post">
            <div><input type="text" name="startDate"/></div>
            <div><input type="text" name="amount"/></div>
            <div><input type="hidden" name="lenderKey" value="%s"/></div>
            <div><input type="submit" value="Add Rate Change"/></div>
          </form>
        </body>
      </html>""" % lender.key())
        self.response.out.write('</body></html>')

class AddRateChange(webapp.RequestHandler):
    def post(self):
        rate = Rate()
        rate.value = int(self.request.get('amount'))
        rate.put()
        
        rateChange = RateChange()
        rateChange.lender = Lender.get(self.request.get('lenderKey'))
        #rateChange.startDate = self.request.get('startDate')
        rateChange.rate = rate
        rateChange.put()
        self.redirect('/lenders')