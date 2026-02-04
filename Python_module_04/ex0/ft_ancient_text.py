import sys


def main() -> None:
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    print("Accessing Storage Vault: ancient_fragment.txt")
    f = None
    try:
        f = open("../data_samples/ancient_fragment.txt", "r")
        print("Connection established...\n")
        data = f.read()
        print("RECOVERED DATA:")
        print(data, end="")
        print("\n\nData recovery complete. Storage unit disconnected.")
    except FileNotFoundError:
        print("ERROR: Storage vault not found")
        sys.exit(1)
    except PermissionError:
        print("ERROR: Storage vault access denied.")
        sys.exit(1)
    finally:
        if f is not None:
            f.close()


main()
