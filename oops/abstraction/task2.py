"""
Create a program to simulate a Call Handling System using Object-Oriented Programming (OOP) concepts in Python.
The program must demonstrate the use of the following OOP principles:

1.Abstraction
2.Inheritance
3.Encapsulation
4.Polymorphism

Requirements:
1. Employee Classes
Create three classes named:
	Respondent
	Manager
	Director

Each class should have a constructor that accepts id and name.
The constructor should initialize:

	==>rank
		3 for Respondent
		2 for Manager
		1 for Director

	==>free → a boolean variable initialized to True

2. Common Methods (Demonstrating Abstraction & Inheritance)
Implement the following methods in all three classes:

	receive_call()
	Prints:
	"call received by <employee name>"
	and sets free to False

	end_call()
	Prints:
	"call ended"
	and sets free to True

	is_free()
	Returns the value of free

	get_rank()
	Returns the value of rank

3. Call Class

Create a class Call with a constructor that accepts:
	id
	name of the caller

It should initialize a variable assigned to False.

4. CallHandler Class

Create a class CallHandler with three class variables:
	respondents
	managers
	directors

5. Employee Management (Encapsulation)

Implement an add_employee() method in CallHandler that:
	Accepts an employee object
	Adds it to the appropriate list based on their rank

6. Call Dispatching (Polymorphism)

Implement a dispatch_call() method in CallHandler that:

Accepts a Call object
Assigns the call to the first available employee, checking in the order:

	Respondent → Manager → Director

Calls receive_call() on the assigned employee
Sets the call’s assigned variable to True
If no employee is free, prints:
"Sorry! All employees are currently busy."

7. Object Creation
Create:
	3 Respondent objects
	2 Manager objects
	1 Director object
Add them to the system using add_employee().

8. Call Assignment

Create a Call object and demonstrate how it is assigned to an employee using the dispatch_call() method.
"""
from abc import ABC, abstractmethod
class Employee(ABC):
    def __init__(self, id, name, rank):
        self.id = id
        self.name = name
        self.rank = rank
        self.free = True

    @abstractmethod
    def receive_call(self):
        pass

    @abstractmethod
    def end_call(self):
        pass

    def is_free(self):
        return self.free

    def get_rank(self):
        return self.rank
class Respondent(Employee):
    def __init__(self, id, name):
        super().__init__(id, name, rank=3)

    def receive_call(self):
        print(f"call received by {self.name}")
        self.free = False

    def end_call(self):
        print("call ended")
        self.free = True
class Manager(Employee):
    def __init__(self, id, name):
        super().__init__(id, name, rank=2)

    def receive_call(self):
        print(f"call received by {self.name}")
        self.free = False

    def end_call(self):
        print("call ended")
        self.free = True
class Director(Employee):
    def __init__(self, id, name):
        super().__init__(id, name, rank=1)

    def receive_call(self):
        print(f"call received by {self.name}")
        self.free = False

    def end_call(self):
        print("call ended")
        self.free = True
class Call:
    def __init__(self, id, caller_name):
        self.id = id
        self.caller_name = caller_name
        self.assigned = False
class CallHandler:
    respondents = []
    managers = []
    directors = []

    @classmethod
    def add_employee(cls, employee):
        if isinstance(employee, Respondent):
            cls.respondents.append(employee)
        elif isinstance(employee, Manager):
            cls.managers.append(employee)
        elif isinstance(employee, Director):
            cls.directors.append(employee)

    @classmethod
    def dispatch_call(cls, call):
        for employee in cls.respondents + cls.managers + cls.directors:
            if employee.is_free():
                employee.receive_call()
                call.assigned = True
                return
        print("Sorry! All employees are currently busy.")
# Creating employees
respondent1 = Respondent(1, "Alice")
respondent2 = Respondent(2, "Bob")
respondent3 = Respondent(3, "Charlie")
manager1 = Manager(4, "David")
manager2 = Manager(5, "Eve")
director1 = Director(6, "Frank")
# Adding employees to the CallHandler
CallHandler.add_employee(respondent1)
CallHandler.add_employee(respondent2)
CallHandler.add_employee(respondent3)
CallHandler.add_employee(manager1)
CallHandler.add_employee(manager2)
CallHandler.add_employee(director1)
# Creating a Call object
call1 = Call(101, "George")
# Dispatching the call
CallHandler.dispatch_call(call1)
