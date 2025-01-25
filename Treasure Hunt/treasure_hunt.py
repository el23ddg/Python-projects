# Text-based Treasure Hunt Game with Combat and Score System

# Define the game world
rooms = {
    "hall": {
        "description": "You are in a grand hall with doors leading north, east, and west.",
        "exits": {"north": "kitchen", "east": "dungeon", "west": "armory"},
        "items": [],
        "enemy": None
    },
    "kitchen": {
        "description": "You are in a kitchen. It smells of burnt toast.",
        "exits": {"south": "hall"},
        "items": ["knife"],
        "enemy": None
    },
    "dungeon": {
        "description": "You are in a dark dungeon. You can hear chains rattling.",
        "exits": {"west": "hall", "north": "treasure room"},
        "items": ["key"],
        "enemy": {"name": "Goblin", "health": 30, "damage": 10}
    },
    "armory": {
        "description": "You are in an armory filled with old, rusted weapons. There's a door leading east.",
        "exits": {"east": "hall"},
        "items": ["shield"],
        "enemy": {"name": "Skeleton Warrior", "health": 40, "damage": 15}
    },
    "treasure room": {
        "description": "You have found the treasure room! Glittering gold is everywhere.",
        "exits": {},
        "items": ["treasure"],
        "enemy": None
    }
}

# Player state
player = {
    "location": "hall",
    "inventory": [],
    "health": 100,
    "damage": 10,  # Base damage
    "score": 0  # Player's score
}

# Display the current room
def display_room():
    location = player["location"]
    print("\n" + rooms[location]["description"])
    if rooms[location]["items"]:
        print("You see:", ", ".join(rooms[location]["items"]))
    if rooms[location]["enemy"]:
        enemy = rooms[location]["enemy"]
        print(f"An enemy is here: {enemy['name']} (Health: {enemy['health']})")
    print("Exits:", ", ".join(rooms[location]["exits"].keys()))

# Handle combat
def combat():
    location = player["location"]
    enemy = rooms[location]["enemy"]
    if not enemy:
        print("There's nothing to fight here.")
        return

    print(f"\nYou engage in combat with {enemy['name']}!")

    while enemy["health"] > 0 and player["health"] > 0:
        action = input("\nDo you want to 'attack' or 'run'? ").strip().lower()

        if action == "attack":
            # Player attacks the enemy
            enemy["health"] -= player["damage"]
            print(f"You attack the {enemy['name']} and deal {player['damage']} damage.")
            
            if enemy["health"] <= 0:
                print(f"You defeated the {enemy['name']}!")
                player["score"] += 20  # Increase score for defeating an enemy
                rooms[location]["enemy"] = None  # Remove the enemy from the room
                print(f"Your score is now: {player['score']}")
                return
            
            # Enemy attacks the player
            player["health"] -= enemy["damage"]
            print(f"The {enemy['name']} attacks you and deals {enemy['damage']} damage.")
            print(f"Your health: {player['health']}")
        elif action == "run":
            print("You run away!")
            return
        else:
            print("Invalid action. Try 'attack' or 'run'.")

    # Check if the player is defeated
    if player["health"] <= 0:
        print("You have been defeated! Game Over.")
        exit()

# Handle player actions
def take_action(action):
    if action in rooms[player["location"]]["exits"]:
        player["location"] = rooms[player["location"]]["exits"][action]
        display_room()
    elif action.startswith("take "):
        item = action.split("take ", 1)[1]
        if item in rooms[player["location"]]["items"]:
            player["inventory"].append(item)
            rooms[player["location"]]["items"].remove(item)
            print(f"You took the {item}.")
            player["score"] += 10  # Increase score for collecting an item
            print(f"Your score is now: {player['score']}")

            # Special effects for items
            if item == "knife":
                player["damage"] += 10
                print("You equip the knife. Your damage increases to:", player["damage"])
            elif item == "shield":
                player["health"] += 20
                print("You equip the shield. Your health increases to:", player["health"])
            elif item == "treasure":
                print("Congratulations! You found the treasure and won the game!")
                print(f"Your final score: {player['score']}")
                exit()
        else:
            print("You can't take that.")
    elif action == "inventory":
        print("Your inventory:", ", ".join(player["inventory"]))
    elif action == "fight":
        combat()
        if rooms[player["location"]]["enemy"] is None:
            print("You are safe now. Continue exploring!")
    elif action == "quit":
        print("Thanks for playing!")
        print(f"Your final score: {player['score']}")
        return False
    else:
        print("Invalid action.")
    return True

# Main game loop
def main():
    print("Welcome to the Treasure Hunt!")
    print("Type 'fight' to engage in combat if an enemy is present.")
    display_room()
    while True:
        action = input("\nWhat do you want to do? ").strip().lower()
        if not take_action(action):
            break

if __name__ == "__main__":
    main()
