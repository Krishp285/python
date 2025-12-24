import random as rd 
computer_guess_number = rd.randint(1, 20) 
print("Welcome to the Number Guessing Game!")
print("Computer has selected a number between 1 and 20.")
user_attempts = 5

for attempt in range(user_attempts):
    user_guess = int(input("Enter your guess (between 1 and 20): ")) 
    if user_guess == computer_guess_number:
        print("Congratulations! You've guessed the number.")
        break
    elif user_guess < computer_guess_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
    user_attempts -= 1
    print(f"You have {user_attempts} attempts left.")
else:
    print(f"Sorry, you've used all your attempts. The number was {computer_guess_number}.")