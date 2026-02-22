import numpy as np 
np.random.seed(1) 
salary = np.random.normal(50000, 8000, 50)  # 50 employees 
salary = np.round(salary, 2) 
print("Mean Salary:", np.mean(salary)) 
print("Max Salary:", np.max(salary)) 
print("Total Salary:", np.sum(salary)) 