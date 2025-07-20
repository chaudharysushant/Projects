class car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
    
    def drive(self):
        print(f"{self.brand} is driving.")

car1 = car("Toyota", "Red")
print(car1.brand)
print(car1.color)
car1.drive()