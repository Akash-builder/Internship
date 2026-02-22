import numpy as np 
emp_id = np.array([201, 202, 203, 204, 205]) 
emp_name = np.array(["Akash", "Ravi", "Priya", "Anjali", "Kiran"]) 
age = np.array([22, 25, 28, 30, 35]) 
salary = np.array([28000, 35000, 42000, 50000, 60000]) 
# 1) Total salary 
total_salary = np.sum(salary) 
# 2) Minimum salary 
min_salary = np.min(salary) 
# 3) Maximum salary 
max_salary = np.max(salary) 
# 4) Average age 
avg_age = np.mean(age) 
# 5) Total employees 
total_employees = len(emp_id) 
# 6) Correlation between age and salary 
correlation = np.corrcoef(age, salary)[0, 1] 
print("Employee IDs:", emp_id) 
print("Employee Names:", emp_name) 
print("Ages:", age) 
print("Salaries:", salary) 
print("\n1) Total Salary:", total_salary) 
print("2) Minimum Salary:", min_salary)
print("3) Maximum Salary:", max_salary) 
print("4) Average Age:", avg_age) 
print("5) Total Employees:", total_employees) 
print("6) Correlation (Age vs Salary):", correlation)