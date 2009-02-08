import cgi

from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db

from org.netmelody.slcmonitor.domain.lender import Lender
from org.netmelody.slcmonitor.domain.borrower import Borrower
from org.netmelody.slcmonitor.domain.ratechange import RateChange
from org.netmelody.slcmonitor.domain.rate import Rate

class ManageBorrowers(webapp.RequestHandler):
  def get(self):
    borrowers = Borrower.gql('')
    
    template_values = {
      'borrowers': borrowers
    }
    
    path = os.path.join(os.path.dirname(__file__), '../templates/borrowerlist.html')
    self.response.out.write(template.render(path, template_values))

class AddBorrower(webapp.RequestHandler):
    def post(self):
        borrower = Borrower()
        borrower.identity = users.get_current_user()
        borrower.put()
        self.redirect('/borrowers')
        
class DeleteBorrower(webapp.RequestHandler):
    def post(self):
        borrower = Borrower.get(self.request.get('borrowerKey'))
        borrower.delete()
        self.redirect('/borrowers')
