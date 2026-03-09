# Write a python program to create a Bus child class that inherits from the Vehicle class.
# In Vehicle class vehicle name, mileage and seatingcapacity as its data member. The default fare charge of any vehicle is 
# seating capacity * 100. If Vehicle is Bus instance, we need to add an extra 10% on full fare as a maintenance charge. So 
# total fare for bus instance will become the final amount = total fare + 10% of the total fare.
# Sample Output:
# The bus seating capacity is 50. so, the final fare amount should be 5000+500=5500.
# The car seating capacity is 5. so, the final fare amount should be 500.


class Vehicle:
    def __init__(self, name, mileage, seating_capacity):
        self.name = name
        self.mileage = mileage
        self.seating_capacity = seating_capacity

    def fare(self):
        return self.seating_capacity * 100
    
class Bus(Vehicle):
    def fare(self):
        base_fare = super().fare()
        maintenance_charge = 0.1 * base_fare
        total_fare = base_fare + maintenance_charge
        return total_fare
    
bus = Bus("School Volvo", 12, 50)
print(f"The bus seating capacity is {bus.seating_capacity}. so, the final fare amount should be {bus.fare()}.")
car = Vehicle("Sedan", 15, 5)
print(f"The car seating capacity is {car.seating_capacity}. so, the final fare amount should be {car.fare()}.")