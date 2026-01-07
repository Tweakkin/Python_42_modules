class GardenError(Exception):
    """Custom exception base class for Garden errors."""
    pass


class PlantError(GardenError):
    """Exception for plant-specific issues."""
    pass


class WaterError(GardenError):
    """
    Specific error for water-related issues .
    """
    pass


class SunError(GardenError):
    """
    Specific error for sun-related issues .
    """
    pass


class GardenManager:
    """
    Manages a collection of plants and garden resources.

    Attributes:
        plants : A list of dictionaries representing the garden's plants.
        water_tank : The current water level in the tank.
    """

    def __init__(self):
        """
        Initialize the garden with an empty
        plant list and a full water tank.
        """
        self.plants = []
        self.water_tank = 500

    def add_plants(self, plant_name, water, sun):
        """
        Adds a new plant to the garden after validating inputs.

        Checks if the name is not empty and if water/sun levels are valid
        positive numbers. If validation fails, it catches the error internally
        and prints a message.

        Args:
            plant_name : The name of the plant.
            water : The water level required.
            sun : The sunlight hours required.
        """
        try:
            if not plant_name:
                raise PlantError("Plant name cannot be empty!")
            try:
                if water < 0 or sun < 0:
                    raise PlantError("Water and Sun numbers, "
                                     "cannot be negative!")
            except Exception:
                raise PlantError("Water and Sun need to be actual numbers!")
        except Exception as e:
            print(f"Error adding plant : {e}")
        else:
            self.plants.append(
                {'name': plant_name, 'water': water, 'sun': sun}
                )
            print(f"Added {plant_name} successfully")

    def water_plants(self):
        """
        Simulates watering all plants in the garden.

        Checks if the water tank has enough water before proceeding.

        Raises:
            GardenError: If the water tank is empty or <= 0.
        """
        try:
            print("Opening watering system")
            for plant in self.plants:
                if self.water_tank <= 0:
                    raise GardenError("Not enough water in tank!")
                self.water_tank -= 10
                print(f"Watering {plant['name']} - success")
        except GardenError as e:
            print(f"Caught GardenError: {e}")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self):
        """
        Checks the health status of every plant in the garden.

        Iterates through the plant list and
        validates their water and sun levels.
        Uses a try/except block *inside* the loop to ensure
        that one unhealthy plant does not stop the check for the others.

        Raises:
            WaterError: If water is > 10 or < 1.
            SunError: If sun is > 12 or < 2.
        """
        for plant in self.plants:
            try:
                if plant['water'] > 10:
                    raise WaterError(f"{plant['name']}: Water level "
                                     f"{plant['water']} is too high (max 10)")
                elif plant['water'] < 1:
                    raise WaterError(f"{plant['name']}: water level "
                                     f"{plant['water']} is too low (min 1)")
                if plant['sun'] < 2:
                    raise SunError(f"{plant['name']}: Sunlight hours "
                                   f"{plant['sun']} is too low (min 2)")
                elif plant['sun'] > 12:
                    raise SunError(f"{plant['name']}: "
                                   f"Sunlight hours {plant['sun']} "
                                   "is too high (max 12)")
                print(f"{plant['name']}: healthy (water: {plant['water']}"
                      f", sun: {plant['sun']})")
            except GardenError as e:
                print(f"Error checking {e}")


def test_garden_management():
    """
    Main execution function to test the GardenManager class.

    Demonstrates:
    1. Adding valid and invalid plants.
    2. Watering plants correctly.
    3. Checking plant health with mixed results.
    4. Simulating a system failure (empty tank) and recovering from it.
    """
    print("=== Garden Management System ===\n")

    yahya = GardenManager()
    print("Adding plants to garden...")
    yahya.add_plants("tomato", 5, 8)
    yahya.add_plants("lettuce", 15, 8)
    yahya.add_plants("", 10, 10)

    print("\nWatering plants...")
    yahya.water_plants()

    print("\nChecking plant health...")
    yahya.check_plant_health()

    print("\nTesting error recovery...")
    yahya.water_tank = 0
    yahya.water_plants()

    print("\nRetrying operation after recovery...")
    yahya.water_tank = 100
    yahya.water_plants()
    print("System recovered and continuing...\n")

    print("Garden management system test complete!")


test_garden_management()
