students = []

n = int(input("Enter number of students: "))

for i in range(n):
    name = input(f"Enter name of student {i+1}: ")
    cgpa = float(input(f"Enter CGPA of {name}: "))

    students.append({"name": name, "cgpa": cgpa})

print("\nShortlisted Students (CGPA ≥ 7):")

for student in students:
    if student["cgpa"] >= 7:
        print("Students Eligibile for Internship/n")
        print(student["name"], "-", student["cgpa"])

