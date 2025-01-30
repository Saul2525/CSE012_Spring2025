""""
    Saul Toribio
    1/28/25
    CSE012 Spring 2024: Week 2 Coding Assignment
    IDE: VSCode; Python: 3.12.7
"""

import random

# Declaring Variables
# Used to store important information.
INITIAL_HEALTH = 100
PLAYER_HEALTH = INITIAL_HEALTH
MONSTER_HEALTH = 75

# Introduction
INTRO = (
    f"After having one of the most vivid nightmares of your life, "
    f"awoke in a cold sweat. Rather than awakening in your bed, you found yourself in a crop circle,\n"
    f"surrounded by towering walls of wheat, with no earthly idea of how you had gotten there. "
    f"Despite feeling disoriented and nauseated,\nyou noticed a path forward—your \"way out.\" "
    f"After walking for a while, you come across a fork in the path."
)
print(INTRO + "\n")

# Path Choice
# Again, I just used a switch-case statement to decide whether or not the program will randomly choose left or right.
# Once the program chooses, it will play out that case scenario.
match random.choice(["left", "right"]):
    case "left":
        print("You decided to walk on the left path.\n")
        print(
            "You encounter a friendly gnome\n"
            "heals you for 10 health points\n"
        )

        PLAYER_HEALTH += 10
        if PLAYER_HEALTH > INITIAL_HEALTH:
            PLAYER_HEALTH = 100
    case "right":
        print("You decided to walk on the right path.\n")
        print("You fall into a pit and lose 15 health points.\n")

        PLAYER_HEALTH -= 15
        if PLAYER_HEALTH < 0:
            PLAYER_HEALTH = 0
            print("You are barely alive!\n")

# Treasure Assignment
# The program decides to choose whether or not the monster has treasure.
print("You encountered a monster!\n")
HAS_TREASURE = random.choice([True, False])

# Combat Encounter
# Here, the program will run a loop of you fighting a monster, which will end when PLAYER_HEALTH or MONSTER_HEALTH == 0.
LOOP = True
while LOOP is True:
    # The player attacks first, doing a flat 15 damage.
    print("You strike the monster for 15 damage!\n")
    MONSTER_HEALTH -= 15

    # Then, if PLAYER_HEALTH > 0, the monster will attack, either doing 10 or 20 damage if it lands a crit.
    if PLAYER_HEALTH > 0:
        CRIT = int(random.random() * 2)
        match CRIT:
            case 0:
                print("The monster hits you for 10 damage!\n")
                PLAYER_HEALTH -= 10
            case 1:
                print("The monster lands a critical hit for 20 damage!\n")
                PLAYER_HEALTH -= 20

    # If PLAYER_HEALTH <= 0, then it will print "Game Over!", while if MONSTER_HEALTH <= 0, then it will run the Treasure Check.
    if PLAYER_HEALTH <= 0:
        print("Game Over!\n")
        LOOP = False
    elif MONSTER_HEALTH <= 0:
        print("You defeated the monster!\n")

        # Treasure Check
        # What is printed is dependent if HAS_TREASURE is true or false.
        match HAS_TREASURE:
            case False:
                print("The monster did not have the treasure.\n")
                break
            case True:
                print("You found the hidden treasure!\n")
                break
        LOOP = False
