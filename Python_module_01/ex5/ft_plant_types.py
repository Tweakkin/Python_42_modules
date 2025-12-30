#!/usr/bin/env python3

class Plant:
    """
    A base class representing a plant in the garden.

    Attributes:
        name : The common name of the plant.
        height : The height of the plant in cm.
        age : The age of the plant in days.
    """
    def __init__(self, name, height, age):
        """Initializes the common attributes for any plant."""
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    """
    A specialized class for Flowers, inheriting from Plant.
    Adds specific attributes for color and blooming behavior.
    """
    def __init__(self, name, height, age, color):
        """
        Initializes a Flower instance.
        Args:
            color : The color of the flower petals.
        """
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        """Simulates the flower blooming by printing a message."""
        print(f"{self.name} is blooming beautifully!")

    def get_info(self):
        """Prints the specific details of the flower including its color."""
        print(f"{self.name} (Flower): {self.height}cm, "
              f"{self.age} days, {self.color} color")


class Vegetable(Plant):
    """
    A specialized class for Vegetables, inheriting from Plant.
    Adds specific attributes for harvest season and nutrition.
    """
    def __init__(self, name, height, age, harvest_season, nutritional_value):
        """
        Initializes a Vegetable instance.
        Args:
            harvest_season : The time of year best for harvesting.
            nutritional_value : Key vitamin or nutrient information.
        """
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def get_nutrition(self):
        """Prints the nutritional value of the vegetable."""
        print(f"{self.name} is rich in {self.nutritional_value}")

    def get_info(self):
        """
        Prints the specific details of the vegetable
        including harvest season.
        """
        print(f"{self.name} (Vegetable): {self.height}cm, "
              f"{self.age} days, {self.harvest_season} harvest")


class Tree(Plant):
    """
    A specialized class for Trees, inheriting from Plant.
    Adds specific attributes for trunk size and shade calculation.
    """
    def __init__(self, name, height, age, trunk_diameter):
        """
        Initializes a Tree instance.
        Args:
            trunk_diameter : The diameter of the tree trunk in cm.
        """
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        """
        Calculates and prints the shade area based on trunk diameter.
        Formula: trunk_diameter * 1.56
        (took it from the example in the subject)
        """
        shade_area = int(self.trunk_diameter * 1.56)
        print(f"{self.name} provides {shade_area} square meters of shade")

    def get_info(self):
        """Prints the specific details of the tree including trunk diameter."""
        print(f"{self.name} (Tree): {self.height}cm, "
              f"{self.age} days, {self.trunk_diameter}cm diameter")


# ============MAIN EXECUTION=================

print("=== Garden Plant Types ===\n")

# Creating two instances of Flower
rose = Flower("Rose", 25, 30, "red")
tulip = Flower("Tulip", 20, 25, "pink")

# Creating two instances of Tree
oak = Tree("Oak", 500, 1825, 50)
pine = Tree("Pine", 800, 3000, 70)

# Creating two instances of vegetables
tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
carrot = Vegetable("Carrot", 20, 60, "winter", "vitamin A")

# Demonstration
rose.get_info()
rose.bloom()

print()
oak.get_info()
oak.produce_shade()

print()
tomato.get_info()
tomato.get_nutrition()
