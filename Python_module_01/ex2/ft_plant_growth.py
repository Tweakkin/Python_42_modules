#!/usr/bin/env python3

"""
ft_plant_growth.py - Simulates the growth cycle of plants.

This module defines a Plant class with methods to modify
its state (age and growth)
and tracks these changes over a simulated period of time.
"""


class Plant:

    """
    Represents a plant in the garden that can age and grow.

    Attributes:
        name : The name of the plant.
        height : The current height of the plant in cm.
        days_old : The age of the plant in days.
    """

    def __init__(self, name, height, days_old):

        self.name = name
        self.height = height
        self.days_old = days_old

    def age(self):
        """
        Increments the plant's age by exactly one day.
        """
        self.days_old += 1

    def grow(self, increased):
        """
        Increases the plant's height by a specific amount.
        Args:
            increased : The amount of centimeters to add to the height.
        """
        self.height += increased

    def get_info(self):
        """
        Prints the current status of the plant to the console.
        """
        print(f"{self.name}: {self.height}cm, {self.days_old} days old")


# Creating plants instances
p1 = Plant("Rose", 25, 30)
p2 = Plant("Tulip", 80, 45)

# Stimulating the growth of the first plant
print("=== Day 1 ===")
p1.get_info()
p1_start_height = p1.height
for i in range(1, 7):
    p1.age()
    p1.grow(1)
p1_end_height = p1.height
print("=== Day 7 ===")
p1.get_info()
print(f"Growth this week: +{p1_end_height - p1_start_height}cm")

# Stimulating the growth of the second plant
# print("=== Day 1 ===")
# p2.get_info()
# p2_start_height = p2.height
# for i in range(1, 7):
# 	p2.age()
# 	p2.grow(1)
# print("=== Day 7 ===")
# p2_end_height = p2.height
# p2.get_info()
# print(f"Growth this week: +{p2_end_height - p2_start_height}cm")
