import sys

def main() -> None:
	print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===")

	ID = input("Input Stream active. Enter archivist ID: ")
	sys.stdout.write("Input Stream active. Enter status report: ")
	sys.stdout.flush()
	status = sys.stdin.readline().rstrip("\n")

	print("\n--- TRANSMISSION RECEIVED ---")
	print(f"Archivist ID: {ID}")
	print(f"Status report: {status}")

main()
