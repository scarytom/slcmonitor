from google.appengine.ext import db

class Ledger(db.Model):
    
    def getLoan(self):
        if (self.loan_w):
            return self.loan_w[0]
        if (self.loan_r):
            return self.loan_r[0]
        if (self.loan_dr):
            return self.loan_dr[0]
        
        