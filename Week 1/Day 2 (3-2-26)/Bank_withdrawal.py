account = {}

account["name"] = input("Enter account holder name: ")
account["balance"] = float(input("Enter current balance: "))
account["status"] = input("Enter account status (active/inactive): ").lower()

withdraw_amount = float(input("Enter withdrawal amount: "))

if account["status"] != "active":
    print("Withdrawal denied: Account inactive")

elif withdraw_amount <= 0:
    print("Invalid withdrawal amount")

elif withdraw_amount > account["balance"]:
    print("Withdrawal denied: Insufficient balance")

else:
    account["balance"] -= withdraw_amount
    print("\n Withdrawal successful")
    print("Account Holder:", account["name"])
    print("Remaining Balance:", account["balance"])
