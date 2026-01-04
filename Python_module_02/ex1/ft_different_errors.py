def garden_operations(task):
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


test_error_types()