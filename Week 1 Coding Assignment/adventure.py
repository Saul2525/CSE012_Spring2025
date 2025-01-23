""""
    Saul Toribio
    1/22/25
    CSE012 Spring 2024: Week 1 Coding Assignment
    IDE: VSCode; Python: 3.12.7

    Week 1 Coding Assignment: Homie's Adventure
    This module simulates a simple text-based adventure game where the
    character encounters monsters, finds potions, and navigates
    based on user input.
"""

# Declaring Variables
# Used to store important information.
# The name of our character, their initial and current health, if they have a sword, etc.
INITIAL_HEALTH = 100
HEALTH = INITIAL_HEALTH
STRENGTH = 75.5
CHARACTER_NAME = "Homie"
HAS_SWORD = True
STRENGTH_MULTIPLIER = .5
STRENGTH_BOOST = 15.5
HEALTH_DECREASE = 20

# Introduction
# The "story," if you're being generous. I used a couple of f-strings because
# it's easier to type out, especially when using variables.
INTRO = (
    f"{CHARACTER_NAME}, after having one of the most vivid nightmares of his life, "
    f"awoke in a cold sweat. Rather than awakening in his bed, he found himself in a crop circle,\n"
    f"surrounded by towering walls of wheat, with no earthly idea of how he had gotten there. "
    f"Despite feeling disoriented and nauseated, he noticed a path forward—his \"way out.\""
)
print(INTRO + "\n")

# Arithmetic Operations
# Using the variables declared earlier, I changed the values of base HEALTH
# and STRENGTH by subtracting and adding it with HEALTH_DECREASE and STRENGTH_BOOST respectively.
# I also printed messages explaining what happened with Homie's HEALTH and STRENGTH.
HEALTH -= HEALTH_DECREASE
STRENGTH += STRENGTH_BOOST
print(f"Health decreased to {HEALTH} because {CHARACTER_NAME} encountered a monster.\n")
print(
    f"Strength increased to {STRENGTH} because {CHARACTER_NAME}"
    f"found and drank a magical potion.\n"
)

# Input and Output
# Rather than use if-elif-else statements, I decided to use a match-case statement,
# which is just a switch-case statement in Java.
# Also, I was just thinking about something fun to write about here.
if __name__ == "__main__":
    print(f"{CHARACTER_NAME} walks until he runs into a four-way intersection.\n")
    user_input = input("Which direction would you like to go?")

    print("")
    match user_input:
        case "left":
            print(
                f"{CHARACTER_NAME} chose to go left. "
                f"After some time walking down the path, he came across something of note: "
                f"a hill. From the hill's vantage point, he could now see a forest looming in the "
                f"distance to the North."
            )
        case "right":
            print(
                f"{CHARACTER_NAME} chose to go right. After some time walking down the path, "
                f"he heard the distant hum of an engine. "
                f"Eager to find the source, he ran faster and faster,\n"
                f"only to crash face-first into a wall of wheat. "
                f"A dead end. {CHARACTER_NAME} paused, contemplating life for a moment."
            )
        case "forward":
            print(
                f"{CHARACTER_NAME} chose to go forward. The path, normally straight, "
                f"twisted left and right, winding unpredictably until he found himself near the "
                f"entrance of a forest that stretched for miles as far as he could see.\n"
                f"With the only path leading forward and the day slowly turning to night, "
                f"{CHARACTER_NAME} sighed and stepped into the forest."
            )
        case "backward":
            print(
                f"Despite having been there just moments ago, "
                f"{CHARACTER_NAME} walked back to the crop circle. "
                f"Perhaps he wanted to take in his surroundings and admire how uniform the circle "
                f"was."
            )
        case _:
            print(
                f"{CHARACTER_NAME} couldn't decide where to go "
                f"and remained standing at the intersection."
            )