# The python Program Should also check whether the area of one Rectangle object is greater
#than another rectangle object by overloading > operator.
#Execute the method resolution order of the Circle class. 

from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height
    
    def  gt(self, other):
        if isinstance(other, Rectangle):
            return self.calculate_area() > other.calculate_area()
        return NotImplemented

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius * self.radius
    
rect = Rectangle(5, 10)
circle = Circle(7)
rect2 = Rectangle(6, 8) 

print("Area of Rectangle 1:", rect.calculate_area())
print("Area of Circle:", circle.calculate_area())
print("Area of Rectangle 2:", rect2.calculate_area())
print("Is Rectangle 1 area greater than Rectangle 2 area?", rect > rect2)

# Execute the method resolution order of the Circle class
print("\nMethod Resolution Order of Circle class:")
print(Circle.__mro__)