import cgi
import os

from google.appengine.api import users
from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.db import djangoforms

from org.netmelody.slcmonitor.domain.loan import Loan
from org.netmelody.slcmonitor.domain.borrower import Borrower

class ManageLoans(webapp.RequestHandler):
  def get(self):
    borrower = Borrower.get(self.request.get('borrowerKey'))
    
    template_values = {
      'borrower' : borrower
    }
    
    path = os.path.join(os.path.dirname(__file__), '../templates/loanlist.html')
    self.response.out.write(template.render(path, template_values))

class AddLoan(webapp.RequestHandler):
    def post(self):
        borrower = Borrower.get(self.request.get('borrowerKey'))
        
        loan = Loan()
        loan.borrower = borrower
        loan.name = self.request.get('loanName')
        loan.put()
        self.redirect('/loans?borrowerKey=%s' % borrower.key())
        
class DeleteLoan(webapp.RequestHandler):
    def post(self):
        loan = Loan.get(self.request.get('loanKey'))
        loan.delete()
        self.redirect('/loans?borrowerKey=%s' % loan.borrower.key())
        
class EditLoan(webapp.RequestHandler):
    def get(self):
      loan = Loan.get(self.request.get('loanKey'))
      
      template_values = {
        'loan' : loan
      }
    
      path = os.path.join(os.path.dirname(__file__), '../templates/loandetail.html')
      self.response.out.write(template.render(path, template_values))