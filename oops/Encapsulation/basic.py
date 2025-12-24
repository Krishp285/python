# Encapsulation : Wrapping data and methods into a single unit (class) and restricting access to some components.

# private member access 
# single unit

# methods :- 
# 1. getter -  to get the value of private member
# 2. setter - to set the value of private member


class Person:
    def __init__(self, name, age):
        self.__name = name      # private member
        self.__age = age        # private member

    # getter for name
    def get_name(self):
        return self.__name

    # setter for name
    def set_name(self, name):
        self.__name = name

    # getter for age
    def get_age(self):
        return self.__age 

    # setter for age
    def set_age(self, age):
       self.__age = age

person = Person("Alice", 30)
print(person.get_name())  # Output: Alice
print(person.get_age())   # Output: 30