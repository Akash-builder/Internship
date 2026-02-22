stand_username="Raj@1947"
stand_password="12344321"
account_status="active"

username=input("Ener the username: ")
password=input("Enter the password: ")

if username!=stand_username:
    print("Username not found")
elif password!=stand_password:
    print("Incorrct password")
elif account_status!="active":
    print("Account is inactive")
else:
    print("Login sucessfull")