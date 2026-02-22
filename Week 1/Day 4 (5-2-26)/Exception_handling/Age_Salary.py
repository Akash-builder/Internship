try: 
    age = int(input("Enter Age: ")) 
    salary = float(input("Enter Salary: ")) 
    if age <= 0: 
        print("Invalid Age! Age must be greater than 0") 
    elif salary < 0: 
        print("Invalid Salary! Salary cannot be negative") 
    else: 
        print("Valid Input") 
        print("Age:", age) 
        print("Salary:", salary) 
except ValueError: 
    print("Invalid Input! Please enter correct numbers") 