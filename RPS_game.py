import random

# Create a user freindly RPS game
def play():
    user_score = 0
    computer_score = 0 

    print('Welcome to the rock, paper, scissors game!')
    print("Instructions: Enter 'rock', 'paper', 'scissors' to play. ")

    while True:
        user_choice = input('Enter the choice (rock, paper, scissors): ').strip().lower()
        if user_choice not in ['rock', 'paper', 'scissors']:
            print ('Invalid input. Please enter valid choice.')
            continue

        computer_choice = get_computer_choice()
        result = winner(user_choice, computer_choice)
        
        if result == 'user':
            user_score += 1
        elif result == 'computer':
            computer_score += 1

        display_winner(user_choice, computer_choice, result)

        if result == 'tie':
            print("It's a tie!")

        print(f'\nScore -> You: {user_score} | Computer: {computer_score}\n')
        
        if not play_again():
            print("\n Thanks for Playing!!")
            print(f"\nFinal Score -> You: {user_score} | Computer: {computer_score}\n")
            break

# get a computer choice 
def get_computer_choice():
    choices = ['rock', 'paper', 'scissors' ]
    return random.choice(choices)

# Decide how can be the Winner
def winner(user, computer):
    if user == computer:
        return 'tie'
    elif (user == 'rock' and computer == 'scissors') or (user == 'scissors' and computer == 'paper') or (user == 'paper' and computer == 'rock'):
        return 'user'
    else:
        return 'computer'

# Annunce the winner name  
def display_winner(user, computer, result):
    print(f'\nYour Choice : {user.capitalize()}')
    print(f'\nComputer Choice : {computer.capitalize()}')

    if result == 'tie':
        return ("It's a Tie")
    elif result == 'user':
        return ("Congratulations! You Win")
    else:
        return ("Sorry, You Lose. Better Luck next time!")

# Ask to play again
def play_again():
    while True:
        choice = input("Do you want to play again?? (y/n):").strip().lower()
        if choice in ['y', 'n']:
            return choice == 'y'
        print('Invalid..Please Enter y or n' )


if __name__ == "__main__":
    play()