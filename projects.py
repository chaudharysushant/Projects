class car:
    def __init__(self, fuel):
        self.__fuel = fuel
    

    def refuel(self,amount):
        if amount > 0: