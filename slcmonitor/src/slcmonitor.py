import cgi

from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db

from org.netmelody.slcmonitor.domain.lender import Lender
from org.netmelody.slcmonitor.domain.borrower import Borrower

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
          </body>
        </html>""")
    else:
      self.redirect(users.create_login_url(self.request.uri))

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

class ManageLenders(webapp.RequestHandler):
  def get(self):
    self.response.out.write('<html><body>')

    lenders = Lender.gql('')
    
    self.response.out.write('<ul>')
    for lender in lenders:
      self.response.out.write('<li>Lender <b>%s</b></li>' % cgi.escape(lender.name))
    self.response.out.write('</ul>')
      
    # Write the submission form and the footer of the page
    self.response.out.write("""
          <form action="/addlender" method="post">
            <div><input type="text" name="lenderName"/></div>
            <div><input type="submit" value="Add Lender"/></div>
          </form>
        </body>
      </html>""")

class AddLender(webapp.RequestHandler):
    def post(self):
        lender = Lender()
        lender.name = self.request.get('lenderName')
        lender.put()
        self.redirect('/lenders')

application = webapp.WSGIApplication(
                                     [('/', MainPage),
                                      ('/lenders', ManageLenders),
                                      ('/addlender', AddLender),
                                      ('/borrowers', ManageBorrowers),
                                      ('/addborrower', AddBorrower)],

                                     debug=True)
def main():
  run_wsgi_app(application)

if __name__ == "__main__":
  main()