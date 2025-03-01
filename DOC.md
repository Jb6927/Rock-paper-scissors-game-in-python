# Rock Paper Scissors Game in python - Documentation

## Overview
This Python script implements the classic Rock-Paper-Scissors game. The user competes against the computer, which makes a random selection from the three possible moves.

## How It Works
1. The user is prompted to enter their move (rock, paper, or scissors).
2. The input is validated to ensure it's a valid choice.
3. The computer randomly selects one of the three moves.
4. The script determines the winner based on the game rules:
   - Rock beats Scissors
   - Scissors beat Paper
   - Paper beats Rock
   - If both players choose the same move, it's a draw.
5. The result is displayed to the user.

## Code Explanation
```python
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

    

```

## Enhancements
- Add a loop to allow multiple rounds of gameplay.
- Implement a score-tracking system.
- Improve user interface with a graphical version using Tkinter or PyGame.
- Allow the user to play against another human player instead of the computer.

## Conclusion
This Rock-Paper-Scissors script is a simple Python program that demonstrates user input handling, randomization, and basic game logic. It can be further enhanced with additional features to improve gameplay and user experience.

