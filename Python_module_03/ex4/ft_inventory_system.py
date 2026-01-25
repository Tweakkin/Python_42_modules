import sys

inventory = {}

args = sys.argv[1:]

for arg in args:
	data = arg.split(':')
	if len(data) == 2:
		key = data[0]
		try:
			value = int(data[1])
			inventory.update({key: value})
		except ValueError:
			continue


print("=== Inventory System Analysis ===")

inventory_values_total = sum(inventory.values())
num_unique_keys = len(inventory.keys())
print(f"Total items in inventory: {inventory_values_total}")
print(f"Unique item types: {num_unique_keys}")