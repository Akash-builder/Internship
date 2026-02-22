class Book: 
    def __init__(self, title, author): 
        self.title = title 
        self.author = author 
    def show_details(self): 
        print("Title:", self.title) 
        print("Author:", self.author) 
b = Book("Python Basics", "Guido") 
b.show_details() 