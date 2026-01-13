import sys

print("=== Command Quest ===")

total_args = len(sys.argv)

if total_args == 1:
	print("No arguments provided!")
	print(f"Program name: {sys.argv[0]}")
	print(f"Total arguments: {total_args}")

elif total_args > 1:
	print(f"Program name: {sys.argv[0]}")
	print(f"Arguments received: {total_args - 1}")
	for i in range(1, total_args):
		print(f"Argument {i}: {sys.argv[i]}")
	print(f"Total arguments: {total_args}")
