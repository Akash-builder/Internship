class Payment: 
    def pay(self, amount): 
        pass 
class EMI(Payment): 
    def pay(self, amount): 
        print("Paid using EMI:", amount) 
class CreditCard(Payment): 
    def pay(self, amount): 
        print("Paid using Credit Card:", amount) 
class DebitCard(Payment): 
    def pay(self, amount): 
        print("Paid using Debit Card:", amount) 
class Cash(Payment): 
    def pay(self, amount): 
        print("Paid using Cash:", amount) 
class UPI(Payment): 
    def pay(self, amount): 
        print("Paid using UPI:", amount) 
payments = [EMI(), CreditCard(), DebitCard(), Cash(), UPI()] 
for p in payments: 
    p.pay(1000) 