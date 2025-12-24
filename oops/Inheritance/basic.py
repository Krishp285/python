# inheritance : it is a mechanism by which a new class (derived class) can inherit attributes and methods from an existing class (base class).

# Types of Inheritance:

# 1. Single Inheritance :- A derived class inherits from a single base class.

class Animal:
    def speak(self):
        return "Animal speaks"
class Dog(Animal):
    def bark(self):
        return "Dog barks"
dog = Dog()
print(dog.speak())  # Output: Animal speaks
print(dog.bark())   # Output: Dog barks

# 2. Multi-level Inheritance :- A derived class inherits from a base class, and another class inherits from the derived class.

class Vehicle:
    def start(self):
        return "Vehicle started"
class Car(Vehicle):
    def drive(self):
        return "Car is driving"
class SportsCar(Car):
    def turbo(self):
        return "SportsCar in turbo mode"
sports_car = SportsCar()
print(sports_car.start())  # Output: Vehicle started
print(sports_car.drive())  # Output: Car is driving
print(sports_car.turbo())  # Output: SportsCar in turbo mode


# 3. Hierarchical Inheritance :- Multiple derived classes inherit from a single base class.

class Shape:
    def area(self):
        return "Calculating area"       
class Circle(Shape):
    def area(self):
        return "Area of Circle"
class Square(Shape):
    def area(self):
        return "Area of Square"
circle = Circle()
square = Square()
print(circle.area())  # Output: Area of Circle
print(square.area())  # Output: Area of Square


# 4. Multiple Inheritance :- A derived class inherits from more than one base class.

class Father:
    def skills(self):
        return "Gardening, Programming"
class Mother:
    def skills(self):
        return "Cooking, Art"
class Child(Father, Mother):
    def skills(self):
        return f"Father's skills: {Father.skills(self)}, Mother's skills: {Mother.skills(self)}"
child = Child()
print(child.skills())  # Output: Father's skills: Gardening, Programming, Mother's skills: Cooking


# 5. Hybrid Inheritance :- A combination of two or more types of inheritance.

class A:
    def feature_a(self):
        return "Feature A"
class B(A):
    def feature_b(self):
        return "Feature B"
class C(A):
    def feature_c(self):
        return "Feature C"
class D(B, C):
    def feature_d(self):
        return "Feature D"
d = D()
print(d.feature_a())  # Output: Feature A
print(d.feature_b())  # Output: Feature B
print(d.feature_c())  # Output: Feature C
print(d.feature_d())  # Output: Feature D



