import sys


def get_quantity(inventory_tuple):
    return inventory_tuple[1]


inventory = {}

args = sys.argv[1:]

for arg in args:
    data = arg.split(":")
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


print("\n=== Current Inventory ===")
sorted_inventory = sorted(inventory.items(), key=get_quantity, reverse=True)
for key, val in sorted_inventory:
    print(f"{key}: {val} units ({((val/inventory_values_total)*100):.1f}%)")

print("\n=== Inventory Statistics ===")

max_item = max(inventory.items(), key=get_quantity)
min_item = min(inventory.items(), key=get_quantity)
print(f"Most abundant: {max_item[0]} ({max_item[1]} units)")
print(f"Least abundant: {min_item[0]} ({min_item[1]} unit)")

print("\n=== Item Categories ===")
item_categories = {"moderate": {}, "scarce": {}}
for name, qty in inventory.items():
    if qty >= 5:
        item_categories["moderate"].update({name: qty})
    else:
        item_categories["scarce"].update({name: qty})
print(f"Moderate = {item_categories['moderate']}")
print(f"Scarce = {item_categories['scarce']}")

print("\n=== Management Suggestions ===")
item_categories.update({"restock": []})
for name, qty in inventory.items():
    if qty <= 1:
        item_categories["restock"].append(name)
print(f"Restock needed: {item_categories['restock']}")

print("\n=== Dictionary Properties Demo ===")
print(f"Dictionary keys: {list(inventory.keys())}")
print(f"Dictionary values: {list(inventory.values())}")
check_item = "sword"
print(f"Sample lookup - '{check_item}' "
      f"in inventory: {check_item in inventory}")
