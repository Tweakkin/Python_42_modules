def check_plant_health(plant_name, water_level, sunlight_hours):

    """
    Validates plant conditions and raises errors if limits are exceeded.

    Args:
        plant_name : The name of the plant.
        water_level : Water level (must be between 1 and 10).
        sunlight_hours : Sunlight hours (must be between 2 and 12).

    Raises:
        ValueError: If plant_name is empty.
        ValueError: If water_level is outside range [1, 10].
        ValueError: If sunlight_hours is outside range [2, 12].

    Returns:
        str: A success message if all checks pass.
    """

    if not plant_name:
        raise ValueError("Plant name cannot be empty!")
    if water_level > 10:
        raise ValueError(f"Water level {water_level} is too high (max 10)")
    elif water_level < 1:
        raise ValueError(f"Water level {water_level} is too low (min 1)")
    if sunlight_hours < 2:
        raise ValueError(f"Sunlight hours {sunlight_hours} is too low (min 2)")
    elif sunlight_hours > 12:
        raise ValueError(f"Sunlight hours {sunlight_hours} is too high (max 12)")
    return f"Plant '{plant_name}' is healthy!"

def test_plant_checks():

    """
    Runs a series of tests to verify that check_plant_health 
    raises the correct errors for invalid inputs.
    """

    print("=== Garden Plant Health Checker ===\n")

    print("Testing good values...")
    try:
        print(check_plant_health("tomato", 10, 6))
    except ValueError as e:
        print(f"Error : {e}")
    
    print("\nTesting empty plant name...")
    try:
        print(check_plant_health("", 2, 10))
    except ValueError as e:
        print(f"Error : {e}")
    
    print("\nTesting bad water level...")
    try:
        print(check_plant_health("Rose", 15, 6))
    except ValueError as e:
        print(f"Error : {e}")
    
    print("\nTesting bad sunlight hours...")
    try:
        print(check_plant_health("Rose", 6, 0))
    except ValueError as e:
        print(f"Error : {e}")
    
    print("\nAll error raising tests completed!")

test_plant_checks()