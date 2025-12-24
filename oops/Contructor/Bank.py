# Bank 

class Bank:
    def __init__(self,name,bank_name,account_no,balance,pin):
        self.name = name
        self.bank_name = bank_name
        self.account_no = account_no
        self.balance = balance
        self.pin = pin
        

    def display(self):
        print(f"Account Holder: {self.name}")
        print(f"Bank Name: {self.bank_name}")
        print(f"Account Number: {self.account_no}")
        print(f"Balance: ${self.balance}")

    def deposit(self,amount):
        self.balance += amount
        print(f"Deposited: ${amount}. New Balance: ${self.balance}")

    def withdraw(self,amount):
        if self.balance - amount >=10000:
            print(f"Withdraw of ${amount} denied. {self.balance}Minimum balance of $10,000 must be maintained.")
            self.balance -= amount
            print(f"Withdrew: ${amount}. New Balance: ${self.balance}")
        else:
            print(f"Withdraw of ${amount} denied. Minimum balance of $10,000 must be maintained.")

    def check_balance(self):
        print(f"Current Balance: ${self.balance}")  

    def validate_pin(self,entered_pin):
        if self.pin == entered_pin:
            print("PIN validation successful.")
            return True
        else:
            print("Invalid PIN.")
            return False
        
    def pin_set(self,pin):
        if len(str(pin)) == 4:
            self.pin = pin  
            print("PIN set successfully.")
            return True
        else:
            print("PIN must be a 4-digit number.")
            return False
        
account_holder_name = input("Enter account holder name: ")
Bank_name = input("Enter bank name: ")
account_number = input("Enter account number: ")
initial_balance = float(input("Enter initial balance: (must be at least $11,000) "))
pin = int(input("Set your account PIN: "))


b = Bank(account_holder_name,Bank_name,account_number,initial_balance,pin)



if b.pin_set(pin):
    entered_pin = input("Enter your PIN to check balance: ")
    if b.validate_pin(int(entered_pin)):
        b.display()
        deposit = float(input("Enter amount to deposit: "))
        b.deposit(deposit)
        withdraw = float(input("Enter amount to withdraw: "))
        b.withdraw(withdraw)