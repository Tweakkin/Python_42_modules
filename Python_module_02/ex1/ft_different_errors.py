def garden_operations(task):
	"""
    Simulates errors based on the specified garden task.

    This function is designed to intentionally raise specific exceptions 
    to facilitate the testing of error handling logic.

    Args:
        task : The operation to perform. specific triggers include:
            - "bad_data": Triggers a ValueError.
            - "zero_division": Triggers a ZeroDivisionError.
            - "file_not_found": Triggers a FileNotFoundError.
            - "key_error": Triggers a KeyError.

    Raises:
        ValueError: When attempting to convert a non-numeric string to an int.
        ZeroDivisionError: When attempting to divide a number by zero.
        FileNotFoundError: When attempting to open a file that does not exist.
        KeyError: When accessing a dictionary key that does not exist.
    """
	if task == "bad_data":
		int("abc")
	elif task == "zero_division":
		x = 5 / 0
	elif task == "file_not_found":
		open("missing.txt")
	elif task == "key_error":
		plants = {"tomato": 10, "potato": 5}
		x = plants["rose"]

def test_error_types():
	"""
    Demonstrates and validates the handling of specific Python exception types.

    This function runs a sequence of tests against garden_operations().
    It uses try-except blocks to catch expected errors individually and 
    prints hardcoded messages to verify that the correct exception was caught.
    
    It tests the following scenarios:
    1. ValueError handling.
    2. ZeroDivisionError handling.
    3. FileNotFoundError handling.
    4. KeyError handling.
    5. Grouped exception handling (catching multiple errors in one block).
    """
	print("=== Garden Error Types Demo ===\n")

	print("Testing ValueError...")
	try:
		garden_operations("bad_data")
	except ValueError:
		print("Caught ValueError: invalid literal for int()")
	
	print("\nTesting ZeroDivisionError...")
	try:
		garden_operations("zero_division")
	except ZeroDivisionError:
		print("Caught ZeroDivisionError: division by zero")
	
	print("\nTesting FileNotFoundError...")
	try:
		garden_operations("file_not_found")
	except FileNotFoundError:
		print("Caught FileNotFoundError: No such file 'missing.txt'")
	
	print("\nTesting KeyError...")
	try:
		garden_operations("key_error")
	except KeyError:
		print("Caught KeyError: 'missing\\_plant'")
	
	print("\nTesting multiple errors together...")
	try:
		garden_operations("key_error")
	except (KeyError, FileNotFoundError, ZeroDivisionError, ValueError):
		print("Caught an error, but program continues!")
	
	print("\nAll error types tested successfully!")

#test_error_types()