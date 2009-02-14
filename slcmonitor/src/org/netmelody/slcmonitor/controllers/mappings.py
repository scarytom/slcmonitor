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
from org.netmelody.slcmonitor.controllers.borrowercontroller import DeleteBorrower
from org.netmelody.slcmonitor.controllers.loancontroller import ManageLoans
from org.netmelody.slcmonitor.controllers.loancontroller import AddLoan
from org.netmelody.slcmonitor.controllers.loancontroller import DeleteLoan
from org.netmelody.slcmonitor.controllers.loancontroller import EditLoan
from org.netmelody.slcmonitor.controllers.transactioncontroller import AddTransaction
from org.netmelody.slcmonitor.controllers.transactioncontroller import DeleteTransaction
from org.netmelody.slcmonitor.controllers.transactioncontroller import EditTransaction


controller_map = [('/',                  MainPage),
                  
                  # Lenders
                  ('/lenders',           ManageLenders),
                  ('/addlender',         AddLender),
                  ('/deletelender',      DeleteLender),
                  ('/editlender',        EditLender),
                  
                  # Rate Changes
                  ('/addratechange',     AddRateChange),
                  ('/deleteratechange',  DeleteRateChange),
                  ('/editratechange',    EditRateChange),
                  
                  # Borrowers
                  ('/borrowers',         ManageBorrowers),
                  ('/addborrower',       AddBorrower),
                  ('/deleteborrower',    DeleteBorrower),
                  
                  ('/loans',             ManageLoans),
                  ('/addloan',           AddLoan),
                  ('/deleteloan',        DeleteLoan),
                  ('/editloan',          EditLoan),
                  
                  ('/addtransaction',    AddTransaction),
                  ('/deletetransaction', DeleteTransaction),
                  ('/edittransaction',   EditTransaction)]