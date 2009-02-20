import cgi
import os

from google.appengine.api import users
from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.db import djangoforms

from org.netmelody.slcmonitor.domain.loan import Loan
from org.netmelody.slcmonitor.domain.transaction import Transaction

class EditTransaction(webapp.RequestHandler):
  def get(self):
    transaction = Transaction.get(self.request.get('transactionKey'))
    
    template_values = {
      'transaction' : borrower
    }
    
    path = os.path.join(os.path.dirname(__file__), '../templates/transactiondetail.html')
    self.response.out.write(template.render(path, template_values))
    
class DeleteTransaction(webapp.RequestHandler):
    def post(self):
        transaction = Transaction.get(self.request.get('transactionKey'))
        transaction.delete()
        self.redirect('/editloan?loanKey=%s' % transaction.loan.key())

class TransactionForm(djangoforms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['date', 'amount']
        
class AddTransaction(webapp.RequestHandler):
    def post(self):
        data = TransactionForm(data=self.request.POST)
        loan = Loan.get(self.request.get('loanKey'))
        
        if data.is_valid():
            transaction = data.save(commit=False)
            loan.makeWithdrawal(transaction.date, transaction.amount)
        
        self.redirect('/editloan?loanKey=%s' % loan.key())