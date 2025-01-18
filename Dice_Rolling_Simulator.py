# Dice Rolling Simulator in Python
import random
# Function to simulate rolling the dice
def roll_dice():
    return random.randint(1, 6)
# Main program loop
while True:
    # Ask the user if they want to roll the dice
    user_choice = input("Do you want to roll the dice? (yes/no): ")
    
    # Check if the user wants to roll the dice
    if user_choice == 'yes':
        print(f"You got a {roll_dice()}! 🎲")
    elif user_choice == 'no':
        print("Thank you for playing! See you soon.")
        break
    else:
        print("Invalid input. Please type 'yes' or 'no' and roll the dice again")



