import cgi

from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db

from org.netmelody.slcmonitor.domain.lender import Lender
from org.netmelody.slcmonitor.domain.borrower import Borrower
from org.netmelody.slcmonitor.domain.ratechange import RateChange
from org.netmelody.slcmonitor.domain.rate import Rate

class MainPage(webapp.RequestHandler):
  def get(self):
    user = users.get_current_user()

    if user:
        self.response.out.write("""
         <html>
          <body>
            <h1>SLC Monitor</h1>""")
        self.response.out.write('\n            Hello, ' + user.nickname() + '\n')
        self.response.out.write("""
            <ul>
            <li><a href="lenders">Manage Lenders</a></li>
            <li><a href="borrowers">Manage Borrowers</a></li>
            </ul>
            
            <a href="%s">log out</a>
          </body>
        </html>""" % users.create_logout_url("/"))
    else:
      self.redirect(users.create_login_url(self.request.uri))