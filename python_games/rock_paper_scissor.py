import random as rd
user_score = 0
computer_score = 0

def rock_paper_scissors(player1, player2):
    choice = ['rock', 'paper', 'scissors']
    if player1 not in choice or player2 not in choice:
        return "Invalid input! Choose rock, paper, or scissors."
    if (player1 == 'rock' and player2 == 'scissors') or (player1 == 'scissors' and player2 == 'paper') or (player1 == 'paper' and player2 == 'rock'):
        return "Player 1 wins!"
    elif player1 == player2:
        return "It's a tie!"
    else:
        return "Player 2 wins!"

rd.randrange(1,3)
for _ in range(1,11):  
    player1 = input("Enter choice (rock, paper, scissors): ").lower()
    player2 = rd.choice(['rock', 'paper', 'scissors'])

    print("player1 choice:", player1)
    print("player2 choice:", player2)

    result = rock_paper_scissors(player1, player2)
    print("Result:", result)
    if result == "Player 1 wins!":
        user_score += 1
    elif result == "Player 2 wins!":
        computer_score += 1

print("Final Score - Your score:", user_score, ", Computer score:", computer_score ," ,ties:", 10 - (user_score + computer_score))