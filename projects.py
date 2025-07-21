class rectangle:
    def __init__(self, length, breadth):
        self.length =length
        self.breadth =breadth

    def area(self):
        return self.breadth*self.length
    
rect = rectangle(5,3)
print(rect.area())