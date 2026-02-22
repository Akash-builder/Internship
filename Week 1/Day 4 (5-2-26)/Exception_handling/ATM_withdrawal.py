class ATMError(Exception): 
    pass 
def withdraw(balance, amount): 
    if amount <= 0: 
        raise ATMError("Amount must be greater than 0") 
    if amount % 100 != 0: 
        raise ATMError("Amount must be a multiple of 100") 
    if amount > balance: 
        raise ATMError("Insufficient Balance") 
    balance -= amount 
    return balance 
try: 
    balance = 5000 
    amount = int(input("Enter withdrawal amount: ")) 
    new_balance = withdraw(balance, amount) 
    print("Withdrawal Successful!") 
    print("Updated Balance:", new_balance) 
except ATMError as e: 
    print("ATM Withdrawal Failed:", e) 
except ValueError: 
    print("Invalid input! Enter numbers only.")