class ATMError(Exception): 
    pass 
 
 
class ATM: 
    def __init__(self, name, pin, balance=0): 
        self.name = name 
        self.pin = pin 
        self.balance = balance 
 
    # ---------------- Deposit ---------------- 
    def deposit(self, amount): 
        if amount <= 0: 
            raise ATMError("Deposit amount must be greater than 0") 
 
        self.balance += amount 
        return self.balance 
 
    # ---------------- Withdraw ---------------- 
    def withdraw(self, amount): 
        if amount <= 0: 
            raise ATMError("Withdrawal amount must be greater than 0") 
 
        if amount % 100 != 0: 
            raise ATMError("Amount must be a multiple of 100") 
 
        if amount > self.balance: 
            raise ATMError("Insufficient Balance") 
 
        self.balance -= amount 
        return self.balance 
 
    # ---------------- Check Balance ---------------- 
    def check_balance(self): 
        return self.balance 
 
 
# ---------------- Main Program ---------------- 
def main(): 
    user = ATM("Akash", 2003, 5000) 
 
    print("===== Welcome to ATM Simulation =====") 
 
    try: 
        entered_pin = int(input("Enter PIN: ")) 
 
        if entered_pin != user.pin: 
            print("Invalid PIN! Access Denied.") 
            return 
 
        while True: 
            print("\n--- ATM MENU ---") 
            print("1. Deposit") 
            print("2. Withdraw") 
            print("3. Check Balance") 
            print("4. Exit") 
 
            choice = input("Enter your choice: ") 
 
            if choice == "1": 
                amount = float(input("Enter deposit amount: ")) 
                try: 
                    new_balance = user.deposit(amount) 
                    print("Deposit Successful!") 
                    print("Updated Balance:", new_balance) 
                except ATMError as e: 
                    print("Error:", e) 
 
            elif choice == "2": 
                amount = float(input("Enter withdrawal amount: ")) 
                try: 
                    new_balance = user.withdraw(amount) 
                    print("Withdrawal Successful!") 
                    print("Updated Balance:", new_balance) 
                except ATMError as e: 
                    print("Error:", e) 
 
            elif choice == "3": 
                print("Current Balance:", user.check_balance()) 
 
            elif choice == "4": 
                print("Thank you! Exiting ATM.") 
                break 
 
            else: 
                print("Invalid choice! Try again.") 
 
    except ValueError: 
        print("Invalid input! PIN must be a number.") 
 
main()