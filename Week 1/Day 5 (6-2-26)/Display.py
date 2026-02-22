class Student: 
    def display(self): 
        print("Student Display Called") 
class Employee: 
    def display(self): 
        print("Employee Display Called") 
def show(obj): 
    obj.display() 
show(Student()) 
show(Employee())