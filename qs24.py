# 24. Implement the game rock, paper, scissors , Rock smashes scissors.  Paper covers rock.  Scissors cut paper

import random

def get_player_choice(player_name):
    while True:
        try:
            user_input = input(f"{player_name}, enter your choice (rock, paper, or scissors): ").lower()
            if user_input in ["rock", "paper", "scissors"]:
                return user_input
            else:
                print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")
        except KeyboardInterrupt:
            print("\nGame interrupted. Exiting.")
            exit()

def get_opponent_choice(is_computer, opponent_name):
    if is_computer:
        return random.choice(["rock", "paper", "scissors"])
    else:
        return get_player_choice(opponent_name)

def determine_winner(player_choice, opponent_choice):
    winning_conditions = {
        'rock': 'scissors',
        'paper': 'rock',
        'scissors': 'paper'
    }
    if player_choice == opponent_choice:
        return "Tie"
    elif winning_conditions[player_choice] == opponent_choice:
        return "Player"
    else:
        return "Opponent"

def play_game(player_name, play_with_computer, opponent_name=None):
    player_score = 0
    opponent_score = 0
    num_rounds = 0
    while True:
        try:
            num_rounds = int(input("Enter the number of rounds you want to play: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    print("\nWelcome to the Rock, Paper, Scissors Game!")

    if play_with_computer:
        print("You are playing against the computer.")
    else:
        print(f"You are playing against {opponent_name}.")

    for round_num in range(1, num_rounds + 1):
        print(f"\nRound {round_num}:")
        player_choice = get_player_choice(player_name)
        opponent_choice = get_opponent_choice(play_with_computer, opponent_name)
        print(f"{player_name}'s choice: {player_choice}")
        if play_with_computer:
            print(f"Computer's choice: {opponent_choice}")
        else:
            print(f"{opponent_name}'s choice: {opponent_choice}")

        winner = determine_winner(player_choice, opponent_choice)
        if winner == "Player":
            print(f"{player_name} wins!")
            player_score += 1
        elif winner == "Opponent":
            if play_with_computer:
                print("Computer wins!")
            else:
                print(f"{opponent_name} wins!")
            opponent_score += 1
        else:
            print("It's a tie!")

    print("\nGame Over!")
    print(f"{player_name}'s score: {player_score}")
    if play_with_computer:
        print("Computer's score: ", opponent_score)
    else:
        print(f"{opponent_name}'s score: {opponent_score}")

    if player_score > opponent_score:
        print(f"Congratulations, {player_name} wins!")
    elif player_score < opponent_score:
        print(f"Sorry, {opponent_name} wins. Better luck next time!")
    else:
        print("It's a tie overall!")

player_name = input("Enter your name: ")
while True:
    try:
        play_with_computer_input = input("Do you want to play with the computer? (y/n): ").lower()
        if play_with_computer_input not in ['y', 'n']:
            raise ValueError("Invalid input. Please enter 'y' or 'n'.")
        play_with_computer = play_with_computer_input == "y"
        break
    except ValueError as e:
        print(e)

if not play_with_computer:
    opponent_name = input("Enter your opponent's name: ")
    play_game(player_name, play_with_computer, opponent_name)
else:
    play_game(player_name, play_with_computer)


#=====================OUTPUT=============================
    
# Enter your name: sree
# Do you want to play with the computer? (y/n): y
# Enter the number of rounds you want to play: 3

# Welcome to the Rock, Paper, Scissors Game!
# You are playing against the computer.

# Round 1:
# sree, enter your choice (rock, paper, or scissors): rock
# sree's choice: rock
# Computer's choice: paper
# Computer wins!

# Round 2:
# sree, enter your choice (rock, paper, or scissors): paper
# sree's choice: paper
# Computer's choice: scissors
# Computer wins!

# Round 3:
# sree, enter your choice (rock, paper, or scissors): paper
# sree's choice: paper
# Computer's choice: scissors
# Computer wins!

# Game Over!
# sree's score: 0
# Computer's score:  3
# Sorry, None wins. Better luck next time!