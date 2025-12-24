import random as rd 
computer_guess_number = rd.choices(["c","C++","Java","Python","JavaScript","Ruby","Go","Swift","Kotlin","PHP"])
print("Welcome to the Number Guessing Game!")
print("Computer has selected ")
user_attempts = 5

for attempt in range(user_attempts):
    user_guess = input("Enter your guess (programming language): ")
    if user_guess == computer_guess_number:
        print("Congratulations! You've guessed the programming language.")
        break
    else:
        print("Incorrect guess! Try again.")
    user_attempts -= 1
    print(f"You have {user_attempts} attempts left.")
else:
    print(f"Sorry, you've used all your attempts. The programming language was {computer_guess_number}.")