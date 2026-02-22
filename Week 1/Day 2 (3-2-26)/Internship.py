student = {}

student["name"] = input("Enter student name: ")
student["cgpa"] = float(input("Enter CGPA: "))
student["year"] = int(input("Enter year of study: "))
student["skill_score"] = int(input("Enter skill test score: "))

if student["cgpa"] >= 7.0 and student["year"] >= 3 and student["skill_score"] >= 60:
    print("\n", student["name"], "is eligible for internship")
else:
    print("\n", student["name"], "is not eligible for internship")
