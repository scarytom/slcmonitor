import cgi

from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db

from org.netmelody.slcmonitor.domain.lender import Lender

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
            <form action="/sign" method="post">
              <div><textarea name="content" rows="3" cols="60"></textarea></div>
              <div><input type="submit" value="Sign Guestbook"></div>
            </form>
            <a href="lenders">Manage Lenders</a>
          </body>
        </html>""")
    else:
      self.redirect(users.create_login_url(self.request.uri))

class ManageLenders(webapp.RequestHandler):
  def get(self):
    self.response.out.write('<html><body>')

    lenders = db.GqlQuery("SELECT * FROM Lender ORDER BY name")

    for lender in lenders:
      self.response.out.write('Lender <b>%s</b>' % cgi.escape(lender.name))

    # Write the submission form and the footer of the page
    self.response.out.write("""
          <form action="/addlender" method="post">
            <div><textarea name="lenderName" rows="1" cols="60"></textarea></div>
            <div><input type="submit" value="Add Lender"></div>
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
                                      ('/addlender', AddLender)],
                                     debug=True)
def main():
  run_wsgi_app(application)

if __name__ == "__main__":
  main()