class Car:
    def __init__(self, fuel):
        self.__fuel = fuel
    
    def refuel(self, amount):
        if amount > 0:
            self.__fuel += amount
            print(f"Fuel added: {amount}")
        else:
            print("Invalid fuel amount")
