import random

# Define the choices
choices = {1: "✊", 2: "✋", 3: "✌"}

# Get the player's choice
player = int(input("Enter 1 for Rock (✊), 2 for Paper (✋), or 3 for Scissors (✌): "))

# Check if the player input is valid
if player not in choices:
    print("Invalid input! Please enter 1, 2, or 3.")
else:
    # Get the computer's choice
    computer = random.randint(1, 3)

    # Print out the choices
    print(f"You chose {choices[player]}.")
    print(f"The computer chose {choices[computer]}.")

    # Determine the winner
    if player == computer:
        print("It's a tie!")
    elif (player == 1 and computer == 3) or (player == 2 and computer == 1) or (player == 3 and computer == 2):
        print("You win!")
    else:
        print("You lose!")
