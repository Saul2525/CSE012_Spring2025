"""
    Saul Toribio
    3/20/25
    CSE012 Spring 2025: Week 8 Coding Assignment
    IDE: VSCode; Python: 3.12.7
"""

class Adventurer:
    """Represents an adventurer with a name, health, and an inventory."""
    def __init__(self, name, initial_health, inventory=None):
        """Initializes an adventurer with a name, health, and an empty inventory."""
        if inventory is None:
            inventory = {}
        self.name = name
        self.health = initial_health
        self.inventory = inventory

    def display_status(self):
        """Prints the adventurer's name, health, and inventory."""
        print("Adventurer Status:")
        print(f"Name:  {self.name}")
        print(f"Health: {self.health}")
        print(f"Inventory: {self.inventory}")

    def take_damage(self, damage):
        """Reduces the adventurer's health by the given damage amount."""
        self.health = max(self.health - damage, 0)
        return self.health

    def take_item(self, item_name, quantity=1):
        """Adds an item to the adventurer's inventory."""
        self.inventory[item_name] = self.inventory.get(item_name, 0) + quantity

class Goblin:
    """Represents a goblin enemy with a name, health, and attack power."""
    def __init__(self, name, initial_health, attack_power=20):
        """Initializes a goblin with a name, initial_health, and attack power."""
        self.name = name
        self.health = initial_health
        self.attack_power = attack_power

    def make_sound(self):
        """Returns the goblin's signature laughter."""
        return "Hehehe!"

    def take_damage(self, damage):
        """Reduces the goblin's health by the given damage amount."""
        self.health = max(self.health - damage, 0)
        return self.health

class TreasureChest:
    """Represents a treasure chest containing items that may be opened once."""
    def __init__(self, items, is_open=False):
        """Initializes a treasure chest with items and an open/closed state."""
        self.items = items
        self.is_open = is_open

    def open_chest(self, adventurer):
        """Opens the chest and gives the items to the adventurer if it hasn't been opened yet."""
        if not self.is_open:
            self.is_open = True
            if self.items:
                for item in self.items:
                    adventurer.take_item(item)
                return f"You open the chest and find: {', '.join(self.items)}."
            return "You open the chest, but it is empty."
        return "The chest is already open."

    def is_chest_open(self):
        """Returns whether the chest is open."""
        return self.is_open

def main():
    """Runs a demonstration of adventurers, goblins, and treasure chests interacting."""
    heroine = Adventurer("Heroine", 100)
    goblin = Goblin("Goblin", 50)
    chest = TreasureChest(["Magic Ring", "Arrows"])

    heroine.display_status()
    print(goblin.make_sound())

    heroine.take_damage(20)
    heroine.display_status()

    chest.open_chest(heroine)
    heroine.display_status()

if __name__ == "__main__":
    main()
