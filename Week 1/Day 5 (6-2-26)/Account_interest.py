class Account: 
    def __init__(self, balance): 
        self.balance = balance 
class SavingAccount(Account): 
    def calculate_interest(self): 
        return self.balance * 0.05 
s = SavingAccount(10000) 
print("Interest:", s.calculate_interest())