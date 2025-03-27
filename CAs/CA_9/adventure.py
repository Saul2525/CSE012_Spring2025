"""
    Saul Toribio
    3/27/25
    CSE012 Spring 2025: Week 9 Coding Assignment
    IDE: VSCode; Python: 3.12.7
"""

from abc import ABC, abstractmethod

class Character(ABC):
    """Base class for all characters in the game. Defines common attributes and methods."""
    @abstractmethod
    def __init__(self, name: str, health: int, attack_power: int):
        """Initialize character with name, health, and attack power."""
        self.name = name
        self.health = health
        self.attack_power = attack_power

    @abstractmethod
    def special_ability(self) -> str:
        """Returns a string describing the character's special ability."""

    @abstractmethod
    def take_damage(self, damage: int) -> int:
        """Reduces health by damage taken and returns remaining health."""

class Adventurer(Character):
    """Represents an Adventurer character."""
    def __init__(self, name="Adventurer", health=120, attack_power=20):
        """Initialize Adventurer with name, health, and attack power."""
        super().__init__(name, health, attack_power)
        self.inventory = {}

    def special_ability(self) -> str:
        """Returns the special ability of the Adventurer."""
        return "Adventurer's Courage: Increases attack power for a short duration."

    def take_damage(self, damage) -> int:
        """Reduces health by damage and returns remaining health."""
        self.health = max(self.health - damage, 0)
        return self.health

    def add_item_to_inventory(self, item_name: str, quantity=1):
        """Adds an item to the inventory, or increases its quantity if already exists."""
        self.inventory[item_name] = self.inventory.get(item_name, 0) + quantity

    def display_inventory(self):
        """Displays the inventory contents."""
        print("Adventurer Inventory:")
        for item, quantity in self.inventory.items():
            print(f"- {item}: {quantity}")

class Elf(Character):
    """Represents an Elf character."""
    def __init__(self, name="Elf", health=100, attack_power=25):
        """Initialize Elf with name, health, and attack power."""
        super().__init__(name, health, attack_power)

    def special_ability(self) -> str:
        """Returns the special ability of the Elf."""
        return "Elven Agility: Dodges the next attack completely."

    def take_damage(self, damage) -> int:
        """Reduces health by damage and returns remaining health."""
        self.health = max(self.health - damage, 0)
        return self.health

class Dragon(Character):
    """Represents a Dragon character."""

    breath_attack_damage = 50

    def __init__(self, name="Dragon", health=200, attack_power=30):
        """Initialize Dragon with name, health, and attack power."""
        super().__init__(name, health, attack_power)

    def special_ability(self) -> str:
        """Returns the special ability of the Dragon."""
        return "Dragon's Fire Breath: Deals massive fire damage to all enemies."

    def take_damage(self, damage) -> int:
        """Reduces health by damage and returns remaining health."""
        self.health = max(self.health - damage, 0)
        return self.health

    @classmethod
    def get_breath_attack_damage(cls) -> int:
        """Returns the breath attack damage for the Dragon."""
        return cls.breath_attack_damage

class EnchantedArtifact:
    """Represents an enchanted artifact with magic power."""
    def __init__(self, name: str, magic_power: int):
        """Initialize the artifact with name and magic power."""
        self.name = name
        self._magic_power = magic_power

    @property
    def magic_power(self):
        """Returns the current magic power."""
        return self._magic_power

    @magic_power.setter
    def magic_power(self, value: int):
        """Set magic power value, but it cannot be negative."""
        if value < 0:
            raise ValueError("Magic power cannot be negative!")
        self._magic_power = value

    @staticmethod
    def is_enchanted(power_level: int) -> bool:
        """Returns whether the artifact is enchanted based on its magic power."""
        return power_level > 75

def main():
    """Simulates the adventure with various characters."""
    heroine = Adventurer("героиня")
    legolas = Elf("Legolas")
    smaug = Dragon("Smaug")
    amulet = EnchantedArtifact("Amulet of Power", 100)

    characters = [heroine, legolas, smaug]
    for character in characters:
        print(f"{character.name}: {character.special_ability()}")

    print(Dragon.get_breath_attack_damage())

    is_enchanted = EnchantedArtifact.is_enchanted(amulet.magic_power)
    print(f"Is the 'Amulet of Power' highly enchanted? {'Yes' if is_enchanted else 'No'}")

    try:
        amulet.magic_power = -10
    except ValueError as verror:
        print(f"Error: {verror}")

if __name__ == "__main__":
    main()
