import csv 
high_salary_employees = [] 
with open("employee.csv", "r") as file: 
    reader = csv.DictReader(file) 
    for row in reader: 
        salary = int(row["salary"]) 
        if salary >= 60000: 
            high_salary_employees.append(row) 
print("High Salary Employees:") 
for emp in high_salary_employees: 
    print(emp)