""""
    Saul Toribio
    1/28/25
    CSE012 Spring 2024: Week 2 Coding Assignment
    IDE: VSCode; Python: 3.12.7

    Week 2 Coding Assignment: Your Adventure
    This module simulates a simple text-based adventure game where the
    character encounters monsters, finds potions, and navigates
    based on user input.
"""

import random

# Declaring Variables
# Used to store important information.
INITIAL_HEALTH = 100
PLAYER_HEALTH = INITIAL_HEALTH
MONSTER_HEALTH = 75
HAS_TREASURE = False

if __name__ == "__main__":
    DIRECTION = random.choice(["left", "right"])

    match DIRECTION:
        case "left":
            print(f"You decided to walk on the left path.\n")
            print(f"You encounter a friendly gnome who heals you for 10 health points.\n")

            PLAYER_HEALTH += 10
            if (PLAYER_HEALTH > INITIAL_HEALTH):
                PLAYER_HEALTH = 100
        case "right":
            print(f"You decided to walk on the right path.\n")
            print(f"You fall into a pit and lose 15 health points.\n")

            PLAYER_HEALTH -= 15
            if (PLAYER_HEALTH < 0):
                PLAYER_HEALTH = 0
                print(f"You are barely alive!\n")

    print(f"You encountered a monster!\n")
    HAS_TREASURE = random.choice([True, False])

    LOOP = True
    while (LOOP == True):
        print(f"You strike the monster for 15 damage!\n")
        MONSTER_HEALTH -= 15

        CRIT = int(random.random() * 2)
        match CRIT:
            case 0:
                print(f"The monster hits you for 10 damage!\n")
                PLAYER_HEALTH -= 20
            case 1:
                print(f"The monster lands a critical hit for 20 damage!\n")
                PLAYER_HEALTH -= 20
        
        if (PLAYER_HEALTH < 0):
            print("Game Over!\n")
            LOOP = False
        elif (MONSTER_HEALTH <= 0):
            print(f"You defeated the monster!\n")

            match HAS_TREASURE:
                case False:
                    print(f"The monster did not have the treasure. You continue your journey.\n")
                case True:
                    print(f"You found the hidden treasure! You win!\n")
            LOOP = False
