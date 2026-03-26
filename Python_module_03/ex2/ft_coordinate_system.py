import math


def calc_distance(p: tuple, p2: tuple) -> float:
    res = math.sqrt(
        (p[0] - p2[0]) ** 2 +
        (p[1] - p2[1]) ** 2 +
        (p[2] - p2[2]) ** 2
    )
    return res


def str_into_tupple(pos_str: str) -> tuple:
    temp_list = []
    pos_list = pos_str.split(",")
    for num in pos_list:
        temp_list.append(int(num))
    return tuple(temp_list)


print("=== Game Coordinate System ===\n")

p1 = (10, 20, 5)
p2 = (0, 0, 0)
print(f"Position created: {p1}")
print(f"Distance between {p2} and {p1}: {calc_distance(p1, p2):.2f}")

print('\nParsing coordinates: "3,4,0"')
pos_str = "3,4,0"
temp_list = []
try:
    pos_tuple = str_into_tupple(pos_str)
    print(f"Parsed position: {pos_tuple}")
    print(f"Distance between {p2} and {pos_tuple}: "
          f"{calc_distance(pos_tuple, p2):.1f}")
except ValueError as e:
    print(f"Error parsing coordinates: {e}")
    print(f"Error details - Type: ValueError, Args: {e.args}")

print('\nParsing invalid coordinates: "abc,def,ghi"')
pos_str_2 = "abc,def,ghi"
try:
    pos_tuple = str_into_tupple(pos_str_2)
    print(f"Parsed position: {pos_tuple}")
except ValueError as e:
    print(f"Error parsing coordinates: {e}")
    print(f"Error details - Type: ValueError, Args: {e.args}")

print("\nUnpacking demonstration:")
x, y, z = pos_tuple
print(f"Player at x={x}, y={y}, z={z}")
print(f"Coordinates: X={x}, Y={y}, Z={z}")
