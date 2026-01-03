
def check_temperature(temp_str):
	try:
		temp = int(temp_str)
	except:
		print(f"Error: '{temp_str}' is not a valid number")
		return
	if temp >= 0 and temp <= 40:
		print(f"Temperature {temp}°C is perfect for plants!")
		return temp
	elif temp > 40:
		print(f"Error: {temp}°C is too hot for plants (max 40°C)")
	elif temp < 0:
		print(f"Error: {temp}°C is too cold for plants (min 0°C)")

def test_temperature_input():
	print("=== Garden Temperature Checker ===\n")

	print("Testing temperature: 25")
	check_temperature("25")
	print()

	print("Testing temperature: abc")
	check_temperature("abc")
	print()

	print("Testing temperature: 100")
	check_temperature("100")
	print()

	print("Testing temperature: -50")
	check_temperature("-50")

	print("\nAll tests completed - program didn't crash!")

test_temperature_input()