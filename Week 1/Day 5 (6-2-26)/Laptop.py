class Laptop: 
    def __init__(self, brand, serial_no): 
        self.brand = brand 
        self.__serial_no = serial_no 
    def get_serial_no(self): 
        return self.__serial_no 
lap = Laptop("Dell", "D12345XYZ") 
print("Brand:", lap.brand) 
print("Serial:", lap.get_serial_no())