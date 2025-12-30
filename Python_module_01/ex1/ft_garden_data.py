#!/usr/bin/env python3

"""
ft_garden_data.py - A program to manage community garden plant data.

This module defines a Plant class to represent individual plants and
a main execution block to demonstrate the creation and display of
several plant instances.
"""


class Plant:

    """
    A class used to represent a Plant in the community garden.

    Attributes:
        name : The common name of the plant (e.g., 'Rose').
        height : The height of the plant in centimeters.
        age : The age of the plant in days.
    """

    def __init__(self, name, height, age):
        """
        Initializes a new instance of the Plant class.
        Args(Same args):
            name : The name of the plant.
            height : The height of the plant in cm.
            age : The age of the plant in days.
        """
        self.name = name
        self.height = height
        self.age = age


# Creating Plant instances
p1 = Plant("Rose", 25, 30)
p2 = Plant("Tulip", 80, 45)
p3 = Plant("Cactus", 15, 120)

# Demonstrate the plants after using the Plant class to Create them
print("=== Garden Plant Registry ===")
print(f"{p1.name}: {p1.height}cm, {p1.age} days old")
print(f"{p2.name}: {p2.height}cm, {p2.age} days old")
print(f"{p3.name}: {p3.height}cm, {p3.age} days old")
