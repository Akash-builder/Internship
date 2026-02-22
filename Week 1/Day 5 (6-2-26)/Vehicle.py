class Vehicle: 
    def start(self): 
        print("Vehicle Started") 
class Car(Vehicle): 
    pass 
class Bus(Vehicle): 
    pass 
class Bike(Vehicle): 
    pass 
c = Car() 
b = Bus() 
bk = Bike() 
c.start() 
b.start() 
bk.start() 