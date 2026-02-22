class Admin: 
    def login(self): 
        print("Admin Login Successful") 
class User: 
    def login(self): 
        print("User Login Successful") 
class Guest: 
    def login(self): 
        print("Guest Login Limited Access") 
for obj in [Admin(), User(), Guest()]: 
    obj.login() 