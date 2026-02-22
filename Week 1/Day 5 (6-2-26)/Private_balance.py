class BankAccount: 
    def __init__(self, balance=0): 
        self.__balance = balance 
    def deposit(self, amount): 
        self.__balance += amount 
    def withdraw(self, amount): 
        if amount <= self.__balance: 
            self.__balance -= amount 
        else: 
            print("Insufficient Balance") 
    def get_balance(self): 
        return self.__balance 
acc = BankAccount(5000) 
acc.deposit(1000) 
acc.withdraw(2000) 
print("Balance:", acc.get_balance()) 