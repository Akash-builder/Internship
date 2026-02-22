class Person: 
    def __init__(self, name, age): 
        self.name = name 
        self.age = age 
class Employee(Person): 
    def __init__(self, name, age, employee_id): 
        super().__init__(name, age) 
        self.employee_id = employee_id 
e = Employee("Akash", 21, "EMP101") 
print(e.name, e.age, e.employee_id) 