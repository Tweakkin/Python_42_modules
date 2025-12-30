#!/usr/bin/env python3

"""
Garden Analytics Platform
-------------------------
A system to manage gardens, track plant growth, and calculate statistics
using Object-Oriented Programming patterns (Inheritance, Nested Classes,
Static/Class Methods).
"""


class Plant:
    """
    The base class representing a  plant.
    Tracks name, height, and growth history.
    """
    def __init__(self, name, height):
        self.name = name
        self.height = height
        self.growth_tracker = 0

    def grow(self, cm):
        """Increases plant height and updates the growth tracker."""
        self.height += cm
        self.growth_tracker += cm
        print(f"{self.name} grew {cm}cm")

    def get_details(self):
        """Returns a string summary of the plant."""
        return f"{self.name}: {self.height}cm"


class FloweringPlant(Plant):
    """
    A child class representing plants that have flowers.
    Inherits from Plant and adds color and blooming status.
    """
    def __init__(self, name, height, color):
        # super() calls the Parent (Plant)
        # __init__ method to handle basic setup
        super().__init__(name, height)
        self.color = color
        self.is_blooming = True

    def get_details(self):
        """Extend the parent's details string with specific flower info"""
        base_details = super().get_details()
        bloom_status = "(blooming)" if self.is_blooming else "(dormant)"
        return f"{base_details}, {self.color} flowers {bloom_status}"


class PrizeFlower(FloweringPlant):
    """
    A grandchild class representing special flowers.
    Inherits from FloweringPlant and adds prize points.
    """
    def __init__(self, name, height, color, prize_points):
        super().__init__(name, height, color)
        self.prize_points = prize_points

    def get_details(self):
        """Extend the parent's details string with specific flower info"""
        base_details = super().get_details()
        return f"{base_details}, Prize points: {self.prize_points}"


class GardenManager:
    """
    The main controller class. Manages a collection
    of plants for a specific owner.
    Contains nested helper tools for statistics.
    """

    # Class Variable: Shared by ALL instances of GardenManager
    total_gardens = 0

    # --- Nested Helper Class ---
    class GardenStats:
        """
        A nested helper class for performing calculations.
        Hidden inside GardenManager to keep logic encapsulated.
        """

        @staticmethod
        def calculate_total_growth(plants):
            """Sums the 'growth_tracker' attribute of all plants."""
            return sum(p.growth_tracker for p in plants)

        @staticmethod
        def calculate_plant_type(plants):
            """Counts how many plants of each specific type exist."""
            regular = sum(1 for p in plants if type(p) is Plant)
            flowering = sum(1 for p in plants if type(p) is FloweringPlant)
            prize = sum(1 for p in plants if type(p) is PrizeFlower)
            return regular, flowering, prize

        @staticmethod
        def calculate_score(plants):
            """
            Calculates a custom score:
            Total Height + Bonus for PrizeFlowers.
            """
            total = sum(p.height for p in plants)
            for p in plants:
                if isinstance(p, PrizeFlower):
                    # Logic: Prize points are weighted heavily
                    # (*4 following the example in the subject)
                    total += p.prize_points * 4
            return total

    def __init__(self, owner_name):
        self.owner_name = owner_name
        self.plants = []
        GardenManager.total_gardens += 1

    def add_plant(self, plant):
        """Adds a plant object to the garden's list."""
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.owner_name}'s garden")

    def generate_report(self):
        """Prints a full summary of the garden using the Nested Stats class."""
        print(f"=== {self.owner_name}'s Garden Report ===")
        print("Plants in garden:")
        for p in self.plants:
            print(f"- {p.get_details()}")

        # Calling the nested static methods to get the math
        total_growth = self.GardenStats.calculate_total_growth(self.plants)
        reg, flw, prize = self.GardenStats.calculate_plant_type(self.plants)
        print(f"\nPlants added: {len(self.plants)}, "
              f"Total growth: {total_growth}cm")
        print(f"Plant types: {reg} regular, "
              f"{flw} flowering, {prize} prize flowers")

    def validate_height(self):
        """Checks if a number is physically possible for a plant."""
        print("\nHeight validation test: ", end='')
        for p in self.plants:
            if p.height < 0 or p.height > 3000:
                return False
        return True

    @classmethod
    def create_garden_network(cls, owner_names):
        """
        method to create multiple GardenManagers at once.
        'cls' refers to the GardenManager class itself.
        """
        print("\n=== Garden Management System Demo ===\n")
        network = []
        for name in owner_names:
            network.append(cls(name))
        return network

    def help_plants_grow(self, cm):
        """implies "grow()" to every plant in the list."""
        print(f"\n{self.owner_name} is helping all plants grow...")
        for p in self.plants:
            p.grow(cm)


# ============MAIN EXECUTION=================

# 1. Use Class Method to managers
alice_m, bob_m = GardenManager.create_garden_network(["Alice", "Bob"])

# 2. Setup Alice's Garden
p1 = Plant("Oak Tree", 100)
p2 = FloweringPlant("Rose", 25, "red")
p3 = PrizeFlower("Sunflower", 50, "yellow", 10)

alice_m.add_plant(p1)
alice_m.add_plant(p2)
alice_m.add_plant(p3)

# 3. Setup Bob's Garden
bob_m.add_plant(Plant("Bush", 40))
bob_m.add_plant(FloweringPlant("Daisy", 52, "white"))

# 4. Action: Grow plants
alice_m.help_plants_grow(1)

print()  # Empty line for formatting

# 5. Generate Report (Uses Nested Classes)
alice_m.generate_report()

# 6. Validate if every height is valid in Alice's Garden
print(alice_m.validate_height())

# 7. Scoring Logic
alice_score = alice_m.GardenStats.calculate_score(alice_m.plants)
bob_score = bob_m.GardenStats.calculate_score(bob_m.plants)
print(f"Garden scores - Alice: {alice_score}, Bob: {bob_score}")

# 8. Print Number of gardens managed (Class variable check)
print(f"Total gardens managed: {alice_m.total_gardens}")
