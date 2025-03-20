"""
    Saul Toribio
    2/27/25
    CSE012 Spring 2025: Week 6 Coding Assignment
    IDE: VSCode; Python: 3.12.7
"""

import datetime
import json

# ================== Week 6 Functions ==================

def initialize_log(log_file):
    """Initializes the adventure log by writing a header with the current timestamp."""
    try:
        now = datetime.datetime.now()
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

        with open(log_file, 'w', encoding="utf-8") as file:
            file.write(f"Adventure Log Started: {timestamp}\n")

        print(f"Adventure log initialized in {log_file}")
    except IOError as ioerror:
        print("Error initializing adventure log: Could not write to file.\n")
        raise ioerror

def finalize_log(log_file):
    """Appends an 'Adventure Log Ended' message with a timestamp to the log file."""
    try:
        now = datetime.datetime.now()
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

        with open(log_file, 'a', encoding="utf-8") as file:
            file.write(f"[{timestamp}] - Adventurer exits the Caves of Orzammar. "
                       f"Adventure Log Ended: {timestamp}")
    except IOError as ioerror:
        print("Error finalizing adventure log: Could not write to file.\n")
        raise ioerror

def log_entry(log_file, entry):
    """Appends a new entry to the adventure log with the current timestamp."""
    try:
        now = datetime.datetime.now()
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

        with open(log_file, 'a', encoding="utf-8") as file:
            file.write(f"[{timestamp}] - {entry}\n")
    except IOError as ioerror:
        print("Error writing to adventure log: Could not write entry.\n")
        raise ioerror

def load_inventory(inventory_file):
    """Attempts to load inventory data from a JSON file."""
    try:
        with open(inventory_file, 'r', encoding="utf-8") as file:
            inventory = json.load(file)
        return inventory
    except FileNotFoundError:
        print(f"Inventory file not found. Creating a new one: {inventory_file}")
        inventory = {}
        return inventory
    except json.JSONDecodeError:
        print("Error loading inventory: Invalid JSON format. Starting with an empty inventory.\n")
        inventory = {}
        return inventory
    except IOError as ioerror:
        print("Error loading inventory: Could not read inventory file.\n")
        raise ioerror

def save_inventory(inventory_file, inventory):
    """Saves the inventory dictionary to a JSON file."""
    try:
        with open(inventory_file, 'w', encoding="utf-8") as file:
            json.dump(inventory, file, indent=4)
        print(f"Inventory saved to {inventory_file}")
    except IOError as ioerror:
        print("Error saving inventory: Could not write to file.\n")
        raise ioerror

def add_item_to_inventory(inventory, item_name, quantity=1):
    """Adds an item to the inventory, increasing its quantity if it already exists."""
    if item_name in inventory:
        inventory[item_name] += quantity
    else:
        inventory[item_name] = quantity

    item_name_plural = f"{item_name}(s)" if quantity > 1 else item_name
    print(f"Added {quantity} {item_name_plural} to inventory.")

def display_inventory(inventory):
    """Displays the current inventory with item names and quantities."""
    if inventory:
        print("Current Inventory:")
        for item_name, quantity in inventory.items():
            print(f" - {item_name}: {quantity}")
    else:
        print("Inventory is empty.")

def main(log_file, inventory_file):
    """Main function to run the program."""
    initialize_log(log_file)
    log_entry(log_file, "Adventurer enters the Caves of Orzammar.")

    inventory = load_inventory(inventory_file)

    print("You stand at the entrance of the Caves of Orzammar.\n")
    while True:
        direction = input("Do you go left or right? (left/right): ").lower()
        print("")

        if direction == "left":
            log_entry(log_file, "Adventurer chose to go left.")
            print("You venture left and encounter a Goblin guarding a chest!\n")

            add_item_to_inventory(inventory, "Rusty Sword", 1)
            log_entry(log_file, "Found Rusty Sword.")

            print("You defeat the Goblin and find a Rusty Sword and a Potion inside the chest.\n")

            add_item_to_inventory(inventory, "Potion", 1)
            log_entry(log_file, "Found Potion.")

            break

        if direction == "right":
            log_entry(log_file, "Adventurer chose to go right.")

            print("You walk right and suddenly fall into a pit!\n")
            print("As you tumble down, you find a hidden passage "
                  "and a clue carved into the stone.\n")

            add_item_to_inventory(inventory, "Torch", 1)
            log_entry(log_file, "Found Torch.")

            log_entry(log_file, "Found a hidden passage with a riddle:")

            print("You light the torch and read the clue: "
                  "'The path forward is through the riddle.'\n")
            break

        print("Invalid input. Please enter 'left' or 'right'.\n")
        log_entry(log_file, "Invalid direction input received.")

    display_inventory(inventory)

    save_inventory(inventory_file, inventory)
    log_entry(log_file, "Inventory saved before exiting caves.")

    finalize_log(log_file)
    print("\nThanks for playing! You have exited the Caves of Orzammar.")

if __name__ == "__main__":
    LOG_FILE = "adventure_log.txt"
    INVENTORY_FILE = "inventory.json"
    main(LOG_FILE, INVENTORY_FILE)
