attendance = []
present_count = 0

n = int(input("Enter number of employees: "))

for i in range(n):
    status = input(f"Employee {i+1} (P/A): ").upper()
    attendance.append(status)
    
for status in attendance:
    if status == "P":
        present_count += 1

print("\nEmployees Present:", present_count)
print("Employees Absent :", n - present_count)
