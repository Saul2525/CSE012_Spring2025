""""
    Saul Toribio
    1/28/25
    CSE012 Spring 2024: Week 2 Coding Assignment
    IDE: VSCode; Python: 3.12.7

    Week 2 Coding Assignment: Homie's Adventure
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

CHARACTER_NAME = "Homie"
STRENGTH = 75.5
HAS_SWORD = True
STRENGTH_MULTIPLIER = .5

STRENGTH_BOOST = 15.5
HEALTH_DECREASE = 20

HAS_TREASURE = False

# Introduction
# The "story," if you're being generous. I used a couple of f-strings because
# it's easier to type out, especially when using variables.
INTRO = (
    f"{CHARACTER_NAME}, after having one of the most vivid nightmares of his life, awoke "
    f"in a cold sweat. Rather than awakening in his bed, he found himself in a crop circle,\n"
    f"surrounded by towering walls of wheat, with no earthly idea of how he had gotten there. "
    f"Despite feeling disoriented and nauseated, he noticed a path forward—his \"way out.\""
)
print(INTRO + "\n")

if __name__ == "__main__":
    print(f"{CHARACTER_NAME} walks until he runs into a two-way intersection.\n")
    DIRECTION = random.choice(["left", "right"])

    match DIRECTION:
        case "left":
            print(f"{CHARACTER_NAME} decided to walk on the left path.\n")
            print(f"He encountered a friendly gnome who heals him for 10 health points.\n")

            PLAYER_HEALTH += 10
            if (PLAYER_HEALTH > INITIAL_HEALTH):
                PLAYER_HEALTH = 100
        case "right":
            print(f"{CHARACTER_NAME} decided to walk on the right path.\n")
            print(f"He, unfortunately, fell into a pit and lost 15 health points.\n")

            PLAYER_HEALTH -= 15
            if (PLAYER_HEALTH < 0):
                PLAYER_HEALTH = 0
                print(f"He's barely alive!\n")

    print(f"{CHARACTER_NAME} encountered a monster!\n")
    HAS_TREASURE = random.choice([True, False])

    LOOP = True
    while (LOOP == True):
        print(f"{CHARACTER_NAME} striked the monster for 15 damage!\n")
        MONSTER_HEALTH -= 15

        CRIT = int(random.random() * 2)
        match CRIT:
            case 0:
                print(f"The monster hits {CHARACTER_NAME} for 10 damage!\n")
                PLAYER_HEALTH -= 20
            case 1:
                print(f"The monster lands a critical hit for 20 damage!\n")
                PLAYER_HEALTH -= 20
        
        if (PLAYER_HEALTH < 0):
            print("Game Over!\n")
            LOOP = False
        elif (MONSTER_HEALTH <= 0):
            print(f"{CHARACTER_NAME} defeated the monster!\n")

            match HAS_TREASURE:
                case False:
                    print(f"The monster did not have the treasure. {CHARACTER_NAME} continues his journey.\n")
                case True:
                    print(f"{CHARACTER_NAME} found the hidden treasure! {CHARACTER_NAME} win!\n")
            LOOP = False
