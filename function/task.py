# Royal Kids Bank :

# Design a Banking App in python  that has the following functionalities:-
# User can:-
# ◆OPEN ACCOUNT by username and password of his choice. On Opening account, his initial balance will be ₹ 25,000/-. 
# Once he opens account, he can login by re-entering the same username & password.
# ◆LOGIN is compulsory to perform any task such as withdrawal, deposit or balance check. If the user name or password do 
# not match, he can not Login. Once he is logged in, he can do as many transactions as he wants. He needs to Logout after 
# he finishes all the transactions
# ◆DEPOSIT will enable user to deposit amount of money of his choice. His balance should be updated after the task 
# completes.
# ◆WITHDRAW will enable user to withdraw amount of money of his choice. The only condition is that his balance at any 
# point can not go less than ₹10,000/-. If this can happen after his withdrawal, your program must not allow that
# transaction. His balance should be updated after the task completes.
# ◆CHECK BALANCE will show the latest updated balance to user.
# ◆LOGOUT will exit the user from the program
# You should use these functions in your program: login(), deposit(), withdraw(), checkBalance()

accounts = {}

def open_account(username, password):
    if username in accounts:
        print("Account already exists.")
        return False
    accounts[username] = {'password': password, 'balance': 25000}
    print("Account opened successfully!")
    return True

def login(username, password):
    user = accounts.get(username)
    if user and user['password'] == password:
        print("Login successful!")
        return True
    print("Invalid username or password.")
    return False

def deposit(username, amount):
    if amount <= 0:
        print("Invalid deposit amount.")
        return
    accounts[username]['balance'] += amount
    print(f"Deposited ₹{amount}. New balance: ₹{accounts[username]['balance']}")

def withdraw(username, amount):
    if amount <= 0:
        print("Invalid withdrawal amount.")
        return
    if accounts[username]['balance'] - amount < 10000:
        print("Cannot withdraw. Balance cannot go below ₹10,000.")
        return
    accounts[username]['balance'] -= amount
    print(f"Withdrew ₹{amount}. New balance: ₹{accounts[username]['balance']}")

def checkBalance(username):
    print(f"Current balance: ₹{accounts[username]['balance']}")

def main():
    logged_in = False
    current_user = None
    while True:
        print("\n1. Open Account\n2. Login\n3. Deposit\n4. Withdraw\n5. Check Balance\n6. Logout\n7. Exit")
        choice = input("Enter choice: ")
        if choice == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")
            open_account(username, password)
        elif choice == '2':
            username = input("Enter username: ")
            password = input("Enter password: ")
            if login(username, password):
                logged_in = True
                current_user = username
        elif choice == '3':
            if not logged_in:
                print("Please login first.")
                continue
            amount = int(input("Enter amount to deposit: "))
            deposit(current_user, amount)
        elif choice == '4':
            if not logged_in:
                print("Please login first.")
                continue
            amount = int(input("Enter amount to withdraw: "))
            withdraw(current_user, amount)
        elif choice == '5':
            if not logged_in:
                print("Please login first.")
                continue
            checkBalance(current_user)
        elif choice == '6':
            if logged_in:
                print("Logged out.")
                logged_in = False
                current_user = None
            else:
                print("No user is logged in.")
        elif choice == '7':
            print("Exiting program.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()


