# combine example of abstraction, encapsulation, inheritance and polymorphism: 
from abc import ABC, abstractmethod

class bankaccount(ABC):
    def __init__(self, name, balance, pin):
        self.name = name 
        self._balance = balance 
        self.__pin = pin
        
    @abstractmethod
    def calculation_interest(self):
        pass 
    
    def get_balance(self):
        return self._balance

    def deposit(self, amt):
        self._balance += amt

    def verify_pin(self, entered_pin):
        return self.__pin == entered_pin

class savingaccount(bankaccount):
    
    def calculation_interest(self):
        return self._balance * 0.05
    
class currentaccount(bankaccount):
    
    def calculation_interest(self):
        return self._balance * 0.02 

# Create accounts with PIN
saving = savingaccount("krishna", 60000, 9000)
current = currentaccount("aashta", 90000, 9000)

# Menu system
while True:
    print("\n--- Bank Menu ---")
    print("a. Current Account")
    print("b. Saving Account")
    print("c. Exit")
    
    choice = input("Enter your choice (a/b/c): ").lower()
    
    if choice == 'c':
        print("Thank you for using our service!")
        break
    
    if choice == 'a':
        selected_account = current
    elif choice == 'b':
        selected_account = saving
    else:
        print("Invalid choice. Please try again.")
        continue
    
    # PIN verification
    entered_pin = int(input("Enter PIN: "))
    
    if selected_account.verify_pin(entered_pin):
        print("\n--- Account Details ---")
        print("Name of account is:", selected_account.name)
        print("Balance of account is:", selected_account.get_balance())
        print("Interest of account is:", selected_account.calculation_interest())
    else:
        print("Incorrect PIN. Access denied.")