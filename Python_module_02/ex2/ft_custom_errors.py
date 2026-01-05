class GardenError(Exception):
    pass

class PlantError(GardenError):
    pass

class WaterError(GardenError):
    pass

def test_plant_error():
    raise PlantError("the tomato plant is wilting!")

def test_water_error():
    raise WaterError("Not enough water in the tank!")

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
    print(f"Caught a garden error: {e}")
try:
    test_water_error()
except GardenError as e:
    print(f"Caught a garden error: {e}")
