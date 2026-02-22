class Shape: 
    def area(self): 
        pass 
class Circle(Shape): 
    def __init__(self, r): 
        self.r = r 
    def area(self): 
        return 3.14 * self.r * self.r 
class Rectangle(Shape): 
    def __init__(self, l, w): 
        self.l = l 
        self.w = w 
    def area(self): 
        return self.l * self.w 
c = Circle(5) 
r = Rectangle(10, 4) 
print("Circle Area:", c.area()) 
print("Rectangle Area:", r.area()) 