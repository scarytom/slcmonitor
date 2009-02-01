from org.netmelody.slcmonitor.controllers.maincontroller import MainPage
from org.netmelody.slcmonitor.controllers.lendercontroller import ManageLenders
from org.netmelody.slcmonitor.controllers.lendercontroller import AddLender
from org.netmelody.slcmonitor.controllers.lendercontroller import EditLender
from org.netmelody.slcmonitor.controllers.lendercontroller import AddRateChange
from org.netmelody.slcmonitor.controllers.borrowercontroller import ManageBorrowers
from org.netmelody.slcmonitor.controllers.borrowercontroller import AddBorrower

controller_map = [('/', MainPage),
                  ('/lenders', ManageLenders),
                  ('/addlender', AddLender),
                  ('/editlender', EditLender),
                  ('/addratechange', AddRateChange),
                  ('/borrowers', ManageBorrowers),
                  ('/addborrower', AddBorrower)]