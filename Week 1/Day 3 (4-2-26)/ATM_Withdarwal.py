def withdraw(balance, amount):
    if amount <= balance and amount % 100 == 0:
        balance = balance - amount
        print("Transation Sucessful")
        print("Current balance : ",balance)
    else:
        print("Transation Failed")
        return "Invalid withdrawal request"

current_balance = float(input("Enter the current ammount :"))
withdraw_amount = float(input("Enter the withdrawal amount : "))

result = withdraw(current_balance, withdraw_amount)

print( result)
