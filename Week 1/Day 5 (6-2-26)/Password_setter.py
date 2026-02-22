class User: 
    def __init__(self, username, password): 
        self.username = username 
        self.__password = password 
    def set_password(self, new_password): 
        self.__password = new_password 
u = User("hemanth", "1234") 
u.set_password("abcd") 
print("Password Updated Successfully") 