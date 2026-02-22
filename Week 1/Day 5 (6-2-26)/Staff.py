class Staff: 
    def __init__(self, name): 
        self.name = name 
class Teacher(Staff): 
    def teach(self): 
        print(self.name, "is teaching") 
t = Teacher("Akash") 
t.teach() 