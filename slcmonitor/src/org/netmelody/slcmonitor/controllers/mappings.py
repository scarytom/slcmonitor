from org.netmelody.slcmonitor.controllers.maincontroller import MainPage
from org.netmelody.slcmonitor.controllers.lendercontroller import ManageLenders
from org.netmelody.slcmonitor.controllers.lendercontroller import AddLender
from org.netmelody.slcmonitor.controllers.lendercontroller import DeleteLender
from org.netmelody.slcmonitor.controllers.lendercontroller import EditLender
from org.netmelody.slcmonitor.controllers.lendercontroller import AddRateChange
from org.netmelody.slcmonitor.controllers.lendercontroller import DeleteRateChange
from org.netmelody.slcmonitor.controllers.lendercontroller import EditRateChange
from org.netmelody.slcmonitor.controllers.borrowercontroller import ManageBorrowers
from org.netmelody.slcmonitor.controllers.borrowercontroller import AddBorrower

controller_map = [('/',               MainPage),
                  
                  # Lenders
                  ('/lenders',          ManageLenders),
                  ('/addlender',        AddLender),
                  ('/deletelender',     DeleteLender),
                  ('/editlender',       EditLender),
                  
                  # Rate Changes
                  ('/addratechange',    AddRateChange),
                  ('/deleteratechange', DeleteRateChange),
                  ('/editratechange',   EditRateChange),
                  
                  # Borrowers
                  ('/borrowers',      ManageBorrowers),
                  ('/addborrower',    AddBorrower)]