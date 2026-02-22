cgpa=float(input("Enter your CGPA: "))
yos=int(input("Enter the year of study: "))
score=int(input("Enter the test score: "))

if cgpa<7.0:
    print("Not Eligibile. Reqired more than 7 CGPA.")
elif yos<3:
    print("Not Eligibile. Only 3rd and above are allowed.")
elif score<60:
    print("Not Eligibile. Required score is 60 or more.")
else:
    print("You are Eligibile for the Internship.")