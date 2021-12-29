import random as rand
win = 0 
lose = 0 
tie = 0
score = 100
name = input("Please Enter your name: ")
print("Welcome to Rock, Paper, Scissors Game\n")
print(f"[{name}]")
print("[You have been given 100 credits]")
print("\n######## Rules #########")
print("1 - Each win gives you 10 credits")
print("2 - Each lose costs you 10 credits")
print(f"\nLet's Start the Game {name}!")
      

while True:
    user_action = input("Enter a choice (rock, paper, scissors): ")
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = rand.choice(possible_actions)
    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
        result = 'none'
    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
            result = 'win'
        else:
            print("Paper covers rock! You lose.")
            result = 'lose'
    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win!")
            result = 'win'
        else:
            print("Scissors cuts paper! You lose.")
            result = 'lose'
    elif user_action == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
            result = 'win'
        else:
            print("Rock smashes scissors! You lose.")
            result = 'lose'

    if result == 'win':
        win += 1
        score += 10
    elif result == 'lose':
        lose += 1
        score -= 10
    else:
        tie += 1

    play_again = input("\nPlay again? (y/n): ")
    if play_again.lower() != "y":
        break

print('Your total wins are', win, '.') 
print('Your total losses are', lose, '.') 
print('Your total ties are', tie, '.') 

if win > lose:
    print(f"\n{name} has won the game")
    print(f"Your total score is {score}")
elif lose > tie:
    print("\n{name} have lost the game")
    print(f"Your total score is {score}")
else:
    print("\nIt's a tie ")
    print(f"Your total score is {score}")
