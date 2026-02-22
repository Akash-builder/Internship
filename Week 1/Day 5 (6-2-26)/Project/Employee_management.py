class Employee: 
    def __init__(self, emp_id, name, salary): 
        self.emp_id = emp_id 
        self.name = name 
        self.__salary = salary   # private variable (Encapsulation) 
    def get_salary(self): 
        return self.__salary 
    def calculate_salary(self): 
        # Base salary calculation 
        return self.__salary 
    def display(self): 
        print(f"{self.emp_id} | {self.name} | Salary: {self.calculate_salary()}") 
class Manager(Employee): 
    def __init__(self, emp_id, name, salary, bonus): 
        super().__init__(emp_id, name, salary) 
        self.bonus = bonus 
    def calculate_salary(self): 
        # Manager gets salary + bonus 
        return self.get_salary() + self.bonus 
class Intern(Employee): 
    def __init__(self, emp_id, name, salary, stipend): 
        super().__init__(emp_id, name, salary) 
        self.stipend = stipend 
    def calculate_salary(self): 
        # Intern gets salary + stipend 
        return self.get_salary() + self.stipend 
# ----------------------------------------- 
# Store multiple employees in a list 
# ----------------------------------------- 
 
employees = [] 
 
employees.append(Employee(101, "Akash", 30000)) 
employees.append(Manager(102, "Raj", 50000, 10000)) 
employees.append(Intern(103, "Sita", 15000, 5000)) 
employees.append(Manager(104, "Manu", 60000, 15000)) 
 
# ----------------------------------------- 
# Display Payroll 
# ----------------------------------------- 
 
print("\n----- PAYROLL REPORT -----") 
print("ID  | Name    | Total Salary") 
print("---------------------------") 
 
total_payroll = 0 
 
for emp in employees: 
    salary = emp.calculate_salary() 
    total_payroll += salary 
    print(f"{emp.emp_id} | {emp.name} | ₹{salary}") 
 
print("---------------------------") 
print("Total Payroll Amount = ₹", total_payroll) 