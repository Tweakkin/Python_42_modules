import sys

print("=== Command Quest ===")

total_args = len(sys.argv)

if (total_args < 2):
	print("No arguments provided!")
print(f"Program name: {sys.argv[0]}")
for i in range(total_args):
	print(i)

