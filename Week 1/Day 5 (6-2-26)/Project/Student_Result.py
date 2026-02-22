class Student: 
    def __init__(self, name, rollno, marks): 
        self.name = name 
        self.rollno = rollno 
        self.__marks = marks   # private (Encapsulation) 
    def get_marks(self): 
        return self.__marks 
    def calculate_percentage(self): 
    # assuming marks out of 100 
        return self.__marks 
    def calculate_grade(self): 
        m = self.__marks 
        if m >= 90: 
            return "A+" 
        elif m >= 80: 
            return "A" 
        elif m >= 70: 
            return "B" 
        elif m >= 60: 
            return "C" 
        elif m >= 35: 
            return "Pass" 
        else: 
            return "Fail" 
    def display_result(self):   
        print("\n----- Student Result -----") 
        print("Name       :", self.name) 
        print("Roll No    :", self.rollno) 
        print("Marks      :", self.__marks) 
        print("Grade      :", self.calculate_grade()) 
# ------------------------- 
# Testing (Create Students) 
# ------------------------- 
s1 = Student("Akash", 101, 92) 
s2 = Student("Raj", 102, 68) 
s3 = Student("Sita", 103, 30) 
s1.display_result() 
s2.display_result() 
s3.display_result()