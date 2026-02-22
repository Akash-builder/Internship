class Employee: 
    def __init__(self, name, salary): 
        self.name = name 
        self.salary = salary 
e1 = Employee("Hemanth", 50000) 
e2 = Employee("Raj", 35000) 
print(e1.name, e1.salary) 
print(e2.name, e2.salary) 