FILENAME = "student.txt" 
# ------------------ Add Student ------------------ 
def add_student(): 
    try: 
        student_id = input("Enter Student ID: ") 
        name = input("Enter Student Name: ") 
        course = input("Enter Course: ") 
        with open(FILENAME, "a") as file: 
            file.write(f"{student_id},{name},{course}\n") 
        print("Student Added Successfully!\n") 
    except Exception as e: 
        print("Error while adding student:", e) 
# ------------------ View Students ------------------ 
def view_students(): 
    try: 
        with open(FILENAME, "r") as file: 
            data = file.readlines() 
            if len(data) == 0: 
                print("No student records found!\n") 
                return 
    
            print("\n--- Student Records ---") 
            for line in data: 
                student_id, name, course = line.strip().split(",") 
                print(f"ID: {student_id} | Name: {name} | Course: {course}") 
            print() 
    
    except FileNotFoundError: 
        print("File not found! No records available.\n") 
    
    except Exception as e: 
        print("Error while viewing students:", e) 
    
    
    # ------------------ Search Students ------------------ 
def search_student(): 
    try: 
        search_value = input("Enter Student ID or Name to Search: ").lower() 
    
        with open(FILENAME, "r") as file: 
            found = False 
    
            for line in file: 
                student_id, name, course = line.strip().split(",") 
    
                if search_value == student_id.lower() or search_value == name.lower(): 
                    print("\nStudent Found!") 
                    print(f"ID: {student_id} | Name: {name} | Course: {course}\n") 
                    found = True 
                    break 
    
            if not found: 
                print("Student not found!\n") 
    
    except FileNotFoundError: 
        print("File not found! No records available.\n") 
    
    except Exception as e: 
        print("Error while searching student:", e) 
    
    
    # ------------------ Main Menu ------------------ 
def main(): 
    while True: 
        print("===== Student Record Management =====") 
        print("1. Add Student") 
        print("2. View Students") 
        print("3. Search Student") 
        print("4. Exit") 
    
        choice = input("Enter your choice: ") 
    
        if choice == "1": 
            add_student() 
        elif choice == "2": 
            view_students() 
        elif choice == "3": 
            search_student() 
        elif choice == "4": 
            print("Exiting... Thank you!") 
            break 
        else: 
            print("Invalid Choice! Try again.\n") 
main()