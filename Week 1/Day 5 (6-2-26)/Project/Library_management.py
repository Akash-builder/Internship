# ------------------------------- 
# Library Management System (OOPS) 
# Concepts: Class, Inheritance, Encapsulation 
# ------------------------------- 
class Book: 
    def __init__(self, book_id, title, author): 
        self.book_id = book_id 
        self.title = title 
        self.author = author 
        self.__available = True   # Encapsulation (private) 
    def is_available(self): 
        return self.__available 
    def borrow(self): 
        if self.__available: 
            self.__available = False 
            return True 
        return False 
    def return_book(self): 
        self.__available = True 
    def display(self): 
        status = "Available" if self.__available else "Borrowed" 
        print(f"{self.book_id} | {self.title} | {self.author} | {status}") 
 
 
# Inheritance Example 
class EBook(Book): 
    def __init__(self, book_id, title, author, file_size_mb): 
        super().__init__(book_id, title, author) 
        self.file_size_mb = file_size_mb 
 
    def display(self): 
        status = "Available" if self.is_available() else "Borrowed" 
        print(f"{self.book_id} | {self.title} | {self.author} | {status} | {self.file_size_mb}MB (EBook)") 
 
 
class Library: 
    def __init__(self): 
        self.books = [] 
 
    def add_book(self, book): 
        self.books.append(book) 
        print(f"Book added: {book.title}") 
 
    def view_books(self): 
        print("\n--- Library Books ---") 
        if len(self.books) == 0: 
            print("No books available!") 
            return 
 
        for book in self.books: 
            book.display() 
 
    def borrow_book(self, book_id): 
        for book in self.books: 
            if book.book_id == book_id: 
                if book.borrow(): 
                    print(f"Book borrowed successfully: {book.title}") 
                else: 
                    print(f"Book already borrowed: {book.title}") 
                return 
        print("Book not found!") 
 
    def return_book(self, book_id): 
        for book in self.books: 
            if book.book_id == book_id: 
                book.return_book() 
                print(f"Book returned successfully: {book.title}") 
                return 
        print("Book not found!") 
 
 
# ------------------------------- 
# Main Program (Testing) 
# ------------------------------- 
 
library = Library() 
 
b1 = Book(101, "Python Basics", "Guido") 
b2 = Book(102, "Java OOPS", "James") 
b3 = EBook(103, "AI Fundamentals", "Andrew", 15) 
library.add_book(b1) 
library.add_book(b2) 
library.add_book(b3) 
library.view_books() 
library.borrow_book(101) 
library.borrow_book(101) 
library.view_books() 
library.return_book(101) 
library.view_books() 