class ATM: 
    def __init__(self, pin, balance=0): 
        self.__pin = pin 
        self.balance = balance 
    def withdraw(self, entered_pin, amount): 
        if entered_pin != self.__pin: 
            print("Invalid PIN") 
            return 
        if amount <= self.balance: 
            self.balance -= amount 
            print("Withdraw Successful. Balance:", self.balance) 
        else: 
            print("Insufficient Balance") 
atm = ATM(1234, 5000) 
atm.withdraw(1234, 1000) 