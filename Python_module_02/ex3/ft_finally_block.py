# CONFLICT :
# The subject text says test_watering_system() should
# demonstrate try/except,
# BUT the Example Output shows the Error
# printing BEFORE "Closing watering system".
# ============================================================
# If we put try/except in test_watering_system(),
# the 'finally' block here would
# run BEFORE the error is printed, which contradicts the output.
# Therefore, the try/except MUST live here inside water_plants()
# to match the output.
# ============================================================
# Or maybe there is no CONFLICT?
# Because we demonstrate try/except in test_watering_system()
# by calling water_plants in it


def water_plants(plant_list):

    """
    Waters a list of plants.
    It catches errors if a plant is invalid and always runs the cleanup code.
    """
    try:
        print("Opening watering system")
        for plant in plant_list:
            try:
                print("Watering " + plant)
            except TypeError:
                print(f"Error: Cannot water {plant} - invalid plant!")
    except TypeError:
        print("Error: The plant list itself is invalid!")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system():

    """
    Runs tests to show that the system cleans
    up correctly after success or failure.
    """

    print("=== Garden Watering System ===\n")
    print("Testing normal watering...")

    plant_list_1 = ["tomato", "lettuce", "carrots"]
    water_plants(plant_list_1)
    print("Watering completed successfully!")

    print("\nTesting with error...")
    plant_list_2 = ["tomato", None]
    water_plants(plant_list_2)
    print("\nCleanup always happens, even with errors!")


test_watering_system()
