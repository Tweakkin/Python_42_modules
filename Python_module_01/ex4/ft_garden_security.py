#!/usr/bin/env python3

class SecurePlant:
    """
    A Plant class that uses encapsulation to protect its data.
    Direct access to height and age is discouraged;
    setters are used for validation.
    """
    def __init__(self, name, height, age):
        self.name = name
        # We mark these as protected using the underscore convention
        self._height = height
        self._age = age

    # ---------------GETTERS------------------
    def get_height(self):
        """Returns the current height."""
        return self._height

    def get_age(self):
        """Returns the current age."""
        return self._age

    # ---------------SETTERS------------------
    def set_height(self, new_height):
        """
        Updates height only if the value is non-negative.
        """
        if new_height >= 0:
            self._height = new_height
        else:
            print("Security: Negative height rejected")

    def set_age(self, new_age):
        """
        Updates age only if the value is non-negative.
        """
        if new_age >= 0:
            self._age = new_age
        else:
            print("Security: Negative age rejected")


# === Main Execution ===

print("=== Garden Security System ===")

# We initialize with 0 to demonstrate the updates clearly
plant = SecurePlant("Rose", 0, 0)
print(f"Plant created: {plant.name}")

# 2. Valid data test
plant.set_height(25)
print(f"Height updated: {plant.get_height()}cm [OK]")
# =====================================
plant.set_age(30)
print(f"Age updated: {plant.get_age()} days [OK]")
print()

# 3. Corrupted data test
# We print the header, then try the bad operation to trigger the class error
print("Invalid operation attempted: height -5cm [REJECTED]")
plant.set_height(-5)
print()

# 4. Final Status
print(f"Current plant: {plant.name} "
      f"({plant.get_height()}cm, {plant.get_age()} days)")
