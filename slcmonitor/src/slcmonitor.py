from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

from org.netmelody.slcmonitor.controllers.maincontroller import MainPage
from org.netmelody.slcmonitor.controllers.lendercontroller import ManageLenders
from org.netmelody.slcmonitor.controllers.lendercontroller import AddLender
from org.netmelody.slcmonitor.controllers.lendercontroller import EditLender
from org.netmelody.slcmonitor.controllers.lendercontroller import AddRateChange
from org.netmelody.slcmonitor.controllers.borrowercontroller import ManageBorrowers
from org.netmelody.slcmonitor.controllers.borrowercontroller import AddBorrower


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