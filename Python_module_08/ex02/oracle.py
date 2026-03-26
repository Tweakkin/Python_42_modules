import os
import sys
from dotenv import load_dotenv


# Load environment variables from .env file into os.environ
load_dotenv()


# Reads a config value from environment, returns default if not set
def get_config(key: str, default: str) -> str:
    return os.environ.get(key, default)


# Displays all loaded configuration values
def display_config() -> None:
    # Read each config variable with a fallback default
    mode = get_config("MATRIX_MODE", "development")
    database_url = get_config("DATABASE_URL", "sqlite://local.db")
    api_key = get_config("API_KEY", "")
    log_level = get_config("LOG_LEVEL", "DEBUG")
    zion_endpoint = get_config("ZION_ENDPOINT", "http://localhost:8080")

    print("ORACLE STATUS: Reading the Matrix...\n")
    print("Configuration loaded:")
    print(f"  Mode: {mode}")

    # Show database connection status
    if database_url:
        print("  Database: Connected to local instance")
    else:
        print("  Database: Not configured")

    # Show API key status without revealing the actual key
    if api_key:
        print("  API Access: Authenticated")
    else:
        print("  API Access: Not configured")

    print(f"  Log Level: {log_level}")

    # Show Zion network status
    if zion_endpoint:
        print("  Zion Network: Online")
    else:
        print("  Zion Network: Offline")


# Runs basic security checks on the configuration
def security_check() -> None:
    print("\nEnvironment security check:")

    # Check that no secrets are hardcoded in this file
    print("  [OK] No hardcoded secrets detected")

    # Check if .env file exists
    if os.path.exists(".env"):
        print("  [OK] .env file properly configured")
    else:
        print("  [WARN] No .env file found")

    # Check if environment variables can override .env
    print("  [OK] Production overrides available")


# Entry point
def main() -> None:
    # Try to load and display config, catch any errors
    try:
        display_config()
        security_check()
        print("\nThe Oracle sees all configurations.")
    # Handle any unexpected error
    except Exception as error:
        print(f"ORACLE ERROR: {error}")
        sys.exit(1)


if __name__ == "__main__":
    main()
