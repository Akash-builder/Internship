class Cat: 
    def sound(self): 
        print("Meow") 
class Dog: 
    def sound(self): 
        print("Bark") 
class Cow: 
    def sound(self): 
        print("Moo") 
for animal in [Cat(), Dog(), Cow()]: 
    animal.sound()