class Employee: 
    def calculate_salary(self): 
        return 30000 
class Manager(Employee): 
    def calculate_salary(self): 
        return 60000 
class Intern(Employee): 
    def calculate_salary(self): 
        return 15000 
m = Manager() 
i = Intern() 
print("Manager Salary:", m.calculate_salary()) 
print("Intern Salary:", i.calculate_salary()) 