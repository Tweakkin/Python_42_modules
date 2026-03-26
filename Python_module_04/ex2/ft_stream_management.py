import sys


def main() -> None:
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")

    ID = input("Input Stream active. Enter archivist ID: ")
    sys.stdout.write("Input Stream active. Enter status report: ")
    sys.stdout.flush()
    status = sys.stdin.readline()

    print(f"\n[STANDARD] Archive status from {ID}: {status}", end="")
    print("[ALERT] System diagnostic: Communication channels verified",
          file=sys.stderr)
    print("[STANDARD] Data transmission complete")

    print("\nThree-channel communication test successful.")


main()
