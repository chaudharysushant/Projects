class Car:
    def __init__(self, fuel):
        self.__fuel = fuel

    def refuel(self, amount):
        if amount > 0:
            self.__fuel += amount
            print(f"Fuel added: {amount}")
        else:
            print("Invalid fuel amount")

    def drive(self, distance):
        fuel_required = distance * 0.2 
        if self.__fuel >= fuel_required:
            self.__fuel -= fuel_required
            print(f"Drove {distance} km. Remaining fuel: {self.__fuel:.2f} liters")
        else:
            print(f"Not enough fuel to drive {distance} km")

    def get_fuel(self):
        return self.__fuel


class Vehicle:
    def move(self):
        print("Vehicle is moving!!!")


class Bike(Vehicle):
    def move(self):
        print("Bike is riding on the road!!!")


class Truck(Vehicle):
    def move(self):
        print("Truck is hauling goods")


car1 = Car(10)
car1.refuel(20)
car1.drive(50)

bike1 = Bike()
bike1.move()

truck1 = Truck()
truck1.move()
