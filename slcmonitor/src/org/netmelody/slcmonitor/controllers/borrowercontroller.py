import cgi
import os

from google.appengine.api import users
from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.db import djangoforms

from org.netmelody.slcmonitor.domain.borrower import Borrower

class ManageBorrowers(webapp.RequestHandler):
  def get(self):

    user = users.get_current_user()
    q = Borrower.gql('WHERE identity = :1', user)
    currentBorrower = q.get()
    
    borrowers = Borrower.gql('')
    
    template_values = {
      'currentBorrower' : currentBorrower,
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
