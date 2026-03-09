# abstraction  : 
"""
means  hiding implementation details and showing only essential  detalis and  features to user.
in python abstraction mainly achieved by using  class and  function.
    1. class : from abc import  ABC  == > ABC ==> abstract base class
    2. method/ function  : @abstractmethod  == > abstract method
    
==> abstract class can't be instantiated.
==> you can't create an object of an abstract class.
    
"""

from abc import ABC, abstractmethod

class vehicle(ABC):   # abstract  base class 
    
    def __init__(self,brand,fuel):
        self.brand=brand 
        self._fuel = fuel  # protected 
        self.__engine= "END123"  # private 
        
    @abstractmethod
    def mileage(self):
        pass 
    def get_engine_no(self):
        return self.__engine
    
class car(vehicle):
    def __init__(self, brand, fuel):
        super().__init__(brand, fuel)  # calling abstract class constructor  
        
    def mileage(self):
        return "15 km/l"
    
c=car("BMW","petrol")
print("brand of car name is  : ",c.brand)
print("fuel of car is : ",c._fuel)
print("engine no of car is : ",c.get_engine_no())
print("mileage of car is : ",c.mileage())

# print(c.__engine)  # it given error . 

"""
pure virtuall function  = 0 
"""

