# Author: Dhruv

# Inheritance + Method Overriding
# Create:
# Class Shape with method area() returning 0
# Class Rectangle that inherits Shape and overrides area() to return length × breadth

class Shape:
    def area(self):
        return 0    
    
class Rectangle(Shape):
    def __init__(self , length , breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length*self.breadth
    
shapes = [Shape(), Rectangle(4, 5)]

for s in shapes:
    print(s.area())