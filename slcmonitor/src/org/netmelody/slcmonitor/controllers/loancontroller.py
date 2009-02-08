import cgi

from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db

from org.netmelody.slcmonitor.domain.lender import Lender
from org.netmelody.slcmonitor.domain.loan import Loan
from org.netmelody.slcmonitor.domain.ratechange import RateChange
from org.netmelody.slcmonitor.domain.rate import Rate

class ManageLoans(webapp.RequestHandler):
  def get(self):
    loans = Loan.gql('')
    
    template_values = {
      'loans': loans
    }
    
    path = os.path.join(os.path.dirname(__file__), '../templates/loanlist.html')
    self.response.out.write(template.roan(path, template_values))

class AddLoan(webapp.RequestHandler):
    def post(self):
        loan = Loan()
        loan.name = self.request.get('loanName')
        loan.put()
        self.redirect('/loans')
        
class DeleteLoan(webapp.RequestHandler):
    def post(self):
        loan = Loan.get(self.request.get('loanKey'))
        loan.delete()
        self.redirect('/loans')