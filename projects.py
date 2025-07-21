class animal:
    def __init__(self,name):
        self.name = name

        def speak(self):
            print(f"{self.name} makes a sound")

class dog(animal):
    def speak(self):
        print(f"{self.name}says woof")

Dog = dog("buddy")                    
dog.speak()