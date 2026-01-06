class GardenError(Exception):
    """
    Base class for all garden-related errors.
    Inherits from the built-in Exception class so it behaves like a real error.
    """
    pass

class PlantError(GardenError):
    """
    Specific error for plant-related issues.
    """
    pass

class WaterError(GardenError):
    """
    Specific error for water-related issues .
    """
    pass

def test_plant_error():
    """
    Simulates a plant problem by raising a PlantError.
    """
    raise PlantError("The tomato plant is wilting!")

def test_water_error():
    """
    Simulates a water problem by raising a WaterError.
    """
    raise WaterError("Not enough water in the tank!")

def test_custom_errors():
	print("=== Custom Garden Errors Demo ===")

	print("\nTesting PlantError...")
	try:
		test_plant_error()
	except PlantError as e:
		print(f"Caught PlantError: {e}")

	print("\nTesting WaterError...")
	try:
		test_water_error()
	except WaterError as e:
		print(f"Caught WaterError: {e}")

	print("\nTesting catching all garden errors...")
	try:
		test_plant_error()
	except GardenError as e:
	# I used subtype polymorphism where specific child classes
	# like PlantError are treated as their general parent class, GardenError.
		print(f"Caught a garden error: {e}")
	try:
		test_water_error()
	except GardenError as e:
		print(f"Caught a garden error: {e}")

	print("\nAll custom error types work correctly!")

test_custom_errors()