
def check_temperature(temp_str):

	"""
    Validates a temperature reading for agricultural safety.

    Attempts to convert the input string to an integer and checks if it falls
    within the safe range for plants (0°C to 40°C). Handles invalid numbers.

    Args:
        temp_str : The temperature input to validate.

    Returns:
        int: The valid temperature if it is between 0 and 40.
        None: If the input is not a number or is out of the safe range.
    """

	try:
		temp = int(temp_str)
	except ValueError:
		print(f"Error: '{temp_str}' is not a valid number")
		return
	if temp > 40:
		raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")
	elif temp < 0:
		raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")

	print(f"Temperature {temp}°C is perfect for plants!")
	return temp

def test_temperature_input():

	"""
    Executes a set of tests to verify the check_temperature function.

    Tests include:
    - Valid input ("25")
    - Invalid syntax ("abc")
    - Out of bounds high ("100")
    - Out of bounds low ("-50")
    
    Demonstrates that the program continues running even after encountering errors.
    """

	print("=== Garden Temperature Checker ===\n")

	print("Testing temperature: 25")
	try:
		check_temperature("25")
	except ValueError as e:
		print(f"Error: {e}")

	print()

	print("Testing temperature: abc")
	try:
		check_temperature("abc")
	except ValueError as e:
		print(f"Error: {e}")
	print()

	print("Testing temperature: 100")
	try:
		check_temperature("100")
	except ValueError as e:
		print(f"Error: {e}")
	print()

	print("Testing temperature: -50")
	try:
		check_temperature("-50")
	except ValueError as e:
		print(f"Error: {e}")

	print("\nAll tests completed - program didn't crash!")

test_temperature_input()