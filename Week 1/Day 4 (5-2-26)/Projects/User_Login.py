FILENAME = "user.txt" 
# ---------------- Register ---------------- 
def register_user(): 
    try: 
        username = input("Enter new username: ") 
        password = input("Enter new password: ") 
        with open(FILENAME, "a") as file: 
            file.write(f"{username},{password}\n") 
        print("User Registered Successfully!\n") 
    except Exception as e: 
        print("Error while registering user:", e) 
# ---------------- Login ---------------- 
def login_user(): 
    try: 
        username_input = input("Enter username: ") 
        password_input = input("Enter password: ") 
        with open(FILENAME, "r") as file: 
            for line in file: 
                username, password = line.strip().split(",") 
                if username_input == username and password_input == password: 
                    print("Login Successful!\n") 
                    return 
 
        print("Invalid Username or Password!\n") 
 
    except FileNotFoundError: 
        print("Error: user.txt file not found! Please register first.\n") 
 
    except Exception as e: 
        print("Unexpected Error:", e) 
 
 
# ---------------- View Users ---------------- 
def view_users(): 
    try: 
        with open(FILENAME, "r") as file: 
            data = file.readlines() 
 
            if len(data) == 0: 
                print("No users found!\n") 
                return 
 
            print("\n--- Registered Users ---") 
            for line in data: 
                username, password = line.strip().split(",") 
                print("Username:", username) 
            print() 
 
    except FileNotFoundError: 
        print("Error: user.txt file not found!\n") 
 
    except Exception as e: 
        print("Unexpected Error:", e) 
 
 
# ---------------- Main Menu ---------------- 
def main(): 
    while True: 
        print("===== User Login System =====") 
        print("1. Register") 
        print("2. Login") 
        print("3. View Users") 
        print("4. Exit") 
 
        choice = input("Enter choice: ") 
 
        if choice == "1": 
            register_user() 
        elif choice == "2": 
            login_user() 
        elif choice == "3": 
            view_users() 
        elif choice == "4": 
            print("Exiting... Thank you!") 
            break 
        else: 
            print("Invalid Choice! Try again.\n") 
 
 
main()