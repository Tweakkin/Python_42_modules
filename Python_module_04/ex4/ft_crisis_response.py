def access_archive(filename: str) -> None:
    if filename.endswith("standard_archive.txt"):
        print("ROUTINE ACCESS: Attempting access to "
              "'standard_archive.txt'...")
    else:
        print(f"CRISIS ALERT: Attempting access to '{filename}'...")

    status = ""
    try:
        with open(filename, 'r') as f:
            content = f.read()
            print(f"SUCCESS: Archive recovered - ``{content}''")
            status = "Normal operations resumed"
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        status = "Crisis handled, system stable"
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        status = "Crisis handled, security maintained"
    except Exception as e:
        print(f"Something unexpected happened: {e}")
        status = "System checks required"
    finally:
        print(f"STATUS: {status}")


def main() -> None:
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")
    access_archive("lost_archive.txt")

    print()
    access_archive("classified_vault.txt")

    print()
    access_archive("../data_samples/standard_archive.txt")

    print("\nAll crisis scenarios handled successfully. Archives secure.")


main()
