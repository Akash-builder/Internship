import csv 
from datetime import datetime 
# ----- Employees Data ----- 
total_employees = 0 
high_salary_count = 0 
with open("employee.csv", "r") as file: 
    reader = csv.DictReader(file) 
    for row in reader: 
        total_employees += 1 
        if int(row["salary"]) >= 60000: 
            high_salary_count += 1 
# ----- Log Error Data ----- 
error_count = 0 
with open("log.txt", "r") as file: 
    for line in file: 
        if "ERROR" in line: 
            error_count += 1 
# ----- Generate Report ----- 
today = datetime.now().strftime("%d-%m-%Y") 
report = f""" 
DAILY REPORT - {today} ----------------------- 
Total Employees         : {total_employees} 
High Salary Employees   
: {high_salary_count} 
Total Errors in Logs    : {error_count} 
""" 
with open("daily_report.txt", "w") as file: 
    file.write(report) 
print("Daily Report Generated Successfully!") 
print("Saved as daily_report.txt") 