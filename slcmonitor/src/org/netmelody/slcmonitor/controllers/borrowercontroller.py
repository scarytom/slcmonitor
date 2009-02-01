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
    self.response.out.write('<html><body>')

    borrowers = Borrower.gql('')
    
    self.response.out.write('<ul>')
    for borrower in borrowers:
      self.response.out.write('<li>Borrower <b>%s</b></li>' % cgi.escape(borrower.identity.nickname()))
    self.response.out.write('</ul>')
    
    # Write the submission form and the footer of the page
    self.response.out.write("""
          <form action="/addborrower" method="post">
            <div><input type="submit" value="Add Borrower"></div>
          </form>
        </body>
      </html>""")

class AddBorrower(webapp.RequestHandler):
    def post(self):
        borrower = Borrower()
        borrower.identity = users.get_current_user()
        borrower.put()
        self.redirect('/borrowers')