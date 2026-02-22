users = ["akash", "rahul", "neha"]
roles = ["admin", "user", "manager"]
username = input("Enter username: ").lower()
role = input("Enter role: ").lower()

if username in users and role in roles:
    print("✅ Login successful!")
    print("Role assigned:", role)
else:
    print("Access denied. Invalid username or role.")
