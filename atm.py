class Atm (object):
    def __init__(self,withdrawl,balanceEnquiry):
        self.withdrawl=withdrawl
        self.balanceEnquiry=balanceEnquiry
        
        
    def withdrawl(self):
        print("money withdrawl successfully")
    def balanceEnquiry(self):
        print("total balance in account")  
    
account1= Atm("money withdrwal","8889")     
print(account1.balanceEnquiry)

account2=Atm("money withdrwal","7799")
print(account2.withdrawl)

          
