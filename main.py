# Importing the random module to generate a random move for the computer
import random  

# List of possible moves
my_list = ["rock", "paper", "scissors"]  

# Taking user input and converting it to lowercase to avoid case sensitivity issues
my_move = input("Enter your move (rock, paper, or scissors): ")

# Checking if the user input is valid
if my_move not in my_list:
    print("Invalid move! Please choose rock, paper, or scissors.")
else:
    # Randomly selecting a move for the computer
    computer_move = random.choice(my_list)  

    # Displaying both moves
    print(f"Your move: {my_move}, Computer move: {computer_move}")  

    # Checking for a draw
    if computer_move == my_move:     
        print("Match is a draw.")  

    # Checking if the user wins using logical conditions
    elif my_move=="rock":
        if computer_move=="scissors":
            print("Rock smashes scissors:you win")
        else:
            print("Computer win and lose:Batter luck next time")# If the user doesn't win and it's not a draw, the computer wins
    elif my_move=="scissors":
        if computer_move=="paper":
            print("scissors cut paper:you win")
        else:
            print("Computer win and lose:Batter luck next time")# If the user doesn't win and it's not a draw, the computer wins
    elif my_move=="paper":
        if computer_move=="rock":
            print("paper cover rock:you win")
        else:
            print("Computer win and lose:Batter luck next time") # If the user doesn't win and it's not a draw, the computer wins

    
