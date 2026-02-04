import sys


def main() -> None:
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
    f = None
    try:
        print("Initializing new storage unit: new_discovery.txt")
        f = open("new_discovery.txt", "w")
        print("Storage unit created successfully...\n")
        print("Inscribing preservation data...")
        f.write("[ENTRY 001] New quantum algorithm discovered\n")
        print("[ENTRY 001] New quantum algorithm discovered")
        f.write("[ENTRY 002] Efficiency increased by 347%\n")
        print("[ENTRY 002] Efficiency increased by 347%")
        f.write("[ENTRY 003] Archived by Data Archivist trainee\n")
        print("[ENTRY 003] Archived by Data Archivist trainee")
        print("\nData inscription complete. Storage unit sealed.")
        print("Archive 'new_discovery.txt' ready for long-term preservation.")
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
