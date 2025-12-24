# Introduction to OOP in Python
# class : A blueprint for creating objects. It defines a set of attributes and methods that the created objects will have.
# object : An instance of a class. It is created using the class blueprint and can have its own unique data.

# types of class :-

# 1. public class : A class that can be accessed from anywhere in the program.
# 2. private class : A class that can only be accessed from within its own class.
# 3. protected class : A class that can be accessed from within its own class and by subclasses.

# Example of a public class
class PublicClass:
    name = "krish"
    age = 24

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")
p = PublicClass()
# p.display()

p.name = "patel"
p.age = 25  
p.display()


class employee :
    name ="krish patel"  # public ==> name age  salary 
    age =21 
    salary =110000000 
    
    def display(self):  # self  ==>  keyword ==> current  object / member data access self ,  method  ==>  access  
        print(f"Name : {self.name} , Age : {self.age} , Salary : {self.salary} ")
        
e=employee()
e.display()  
print(e.name)

e.name ="krishna"
e.display()

# Example of a private class
class PrivateClass:
    __name = "krish"
    __age = 24

    def display(self):
        print(f"Name: {self.__name}, Age: {self.__age}")

pc = PrivateClass()
pc.display()

