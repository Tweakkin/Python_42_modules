#!/usr/bin/env python3

"""
ft_plant_creation.py - Streamlined creation of Plant objects.

This script demonstrates how to efficiently initialize multiple Plant instances
using a list of data tuples and a list comprehension, rather than creating
variables manually one by one.
"""


class Plant:

    """
    Represents a plant in the garden with basic biological attributes.

    Attributes:
        name : The common name of the plant.
        height : The current height of the plant in centimeters.
        age : The age of the plant in days.
    """

    def __init__(self, name, height, age):
        """
        Initializes a new Plant instance.

        Args:
            name : The name of the plant (e.g., 'Rose').
            height : The starting height in cm.
            age : The starting age in days.
        """
        self.name = name
        self.height = height
        self.age = age


# === Main Execution ===

# List of tuples containing data for plant creation
plants_data = [
    ("Rose", 25, 30),
    ("Oak", 200, 265),
    ("Cactus", 5, 90),
    ("Sunflower", 80, 45),
    ("Fern", 15, 120)
]

# Create Plant objects efficiently using a List Comprehension
garden = [Plant(name, h, a) for name, h, a in plants_data]

plants_created = 0

# Demonstrating results
print("=== Plant Factory Output ===")
for plant in garden:
    plants_created += 1
    print(f"Created: {plant.name} ({plant.height}cm, {plant.age} days)")
print()
print("Total plants created:", plants_created)
