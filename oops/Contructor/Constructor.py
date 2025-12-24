# Constructor :- A constructor is a special method in Python classes that is automatically called when an object of the class is created. It is typically used to initialize the attributes of the object.

# Types of Constructors:

# 1. Default Constructor: A constructor that does not take any parameters and initializes the object with default values.

class DefaultConstructor:
    def __init__(self):
        print("Default Constructor called")

dc = DefaultConstructor()


# 2. Parameterized Constructor: A constructor that takes parameters to initialize the object with specific values.

class ParameterizedConstructor:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

pc = ParameterizedConstructor("Krish", 21)
pc.display()

# 3. Non -Parameterized Constructor: A constructor that does not take any parameters but initializes the object with predefined values.
class NonParameterizedConstructor:
    def __init__(self):
        self.name = "krish patel"
        self.age = 21

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

npc = NonParameterizedConstructor()
npc.display()

# 4. Copy Constructor: A constructor that creates a new object as a copy of an existing object.
class CopyConstructor:
    def __init__(self, Parent):
        self.name = Parent.name
        self.age = Parent.age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

original = ParameterizedConstructor("Krish k patel ", 21)
copy = CopyConstructor(original)
copy.display()


# Contructor Overloading:
class ConstructorOverloading:
    def __init__(self):
        print("Constructor with no parameters called")
    def __init__(self, name):
        self.name = name
        print(f"Constructor with one parameter called: Name = {self.name}")

    def display(self):
        print("contructor method , first init called ")
    def display1(self):
        print(f"contructor method , second init called : Name = {self.name}")

#co = ConstructorOverloading() # error will occur due to constructor overloading not being supported in Python
co1 = ConstructorOverloading("Krish") # this will work because it matches the second constructor definition
co1.display1()