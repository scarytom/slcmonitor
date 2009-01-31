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
      self.response.out.write('<li>Lender <b>%s</b>' % cgi.escape(lender.name))
      self.response.out.write("""<form action="/editlender" method="post">
                                   <div><input type="hidden" name="lenderKey" value="%s"/></div>
                                   <div><input type="submit" value="Edit"/></div>
                                 </form></li>""" % lender.key())
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

class EditLender(webapp.RequestHandler):
    def post(self):
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

application = webapp.WSGIApplication(
                                     [('/', MainPage),
                                      ('/lenders', ManageLenders),
                                      ('/addlender', AddLender),
                                      ('/editlender', EditLender),
                                      ('/addratechange', AddRateChange),
                                      ('/borrowers', ManageBorrowers),
                                      ('/addborrower', AddBorrower)],

                                     debug=True)
def main():
  run_wsgi_app(application)

if __name__ == "__main__":
  main()