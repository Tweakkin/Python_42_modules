import sys


def main() -> None:
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")

    print("Initiating secure vault access...")
    try:
        with open("../data_samples/classified_data.txt", 'r') as file:
            print("Vault connection established with failsafe protocols\n")
            print("SECURE EXTRACTION:")
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("ERROR: Storage vault not found")
        sys.exit(1)
    except PermissionError:
        print("ERROR: Storage vault access denied.")
        sys.exit(1)

    try:
        print("\nSECURE PRESERVATION:")
        with open("../data_samples/classified_data.txt", 'w') as file:
            file.write("[CLASSIFIED] New security protocols archived")
            print("[CLASSIFIED] New security protocols archived")
        if file.closed:
            print("Vault automatically sealed upon completion")
    except FileNotFoundError:
        print("ERROR: Storage vault not found")
        sys.exit(1)
    except PermissionError:
        print("ERROR: Storage vault access denied.")
        sys.exit(1)

    print("\nAll vault operations completed with maximum security.")


main()
