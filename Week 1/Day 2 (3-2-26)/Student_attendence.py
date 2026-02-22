present_students = ["akash", "rahul", "neha", "priya","leo"]
total_classes = 50
student_name = input("Enter student name: ").lower()
print("total classes: 50")
attended_classes=int(input("Enter the no of classes attended : "))
attendance_percentage = (attended_classes / total_classes) * 100

if attendance_percentage >= 75:
    status = "Eligible"
else:
    status = "Not Eligible"

print("Attendance %:", attendance_percentage)
print("Status:", status)
