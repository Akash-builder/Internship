class Student: 
    def __init__(self, name, rollno, marks): 
        self.name = name 
        self.rollno = rollno 
        self.marks = marks 
s1 = Student("Hemanth", 101, 85) 
s2 = Student("Raj", 102, 72) 
s3 = Student("Sita", 103, 90) 
for s in [s1, s2, s3]: 
    print(s.name, s.rollno, s.marks)