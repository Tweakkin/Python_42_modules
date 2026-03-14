import sys
import os
import site

def is_virtual_env() -> bool:
    try:
        return sys.prefix != sys.base_prefix
    except AttrributeError:
        # sys.base_prefix was added in python 3.3
        # older versions would cause error
        return os.environ.get("VIRTUAL_ENV") is not None

def get_venv_name() -> str:
    try:
        venv_path = os.environ.get("VIRTUAL_ENV", "")
        if venv_path:
            return	os.path.basename(venv_path)
        return os.path.basename(sys.prefix)
    except Exception as e:
        return f"Unknown error {e}"

def get_package_installation_path() -> str:
    try:
        paths = site.getsitepackages()
        return paths[0] if paths else "No site-packages path found"
    except Exception as error:
        return f"Could not determine package path: {error}"

def display_outside_matrix() -> None:
    print("\nMATRIX STATUS: You're still plugged in\n")
    print(f"Current Python: {sys.executable}")
    print("Virtual Environment: None detected")

    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.")
    print("")
    print("To enter the construct, run:")
    print("python3 -m venv matrix_env")
    print("source matrix_env/bin/activate # On Unix")
    print("matrix_env")
    print("Scripts")
    print("activate # On Windows\n")
    print("Then run this program again.")

def display_inside_matrix() -> None:
    venv_name = get_venv_name()
    venv_path = os.environ.get("VIRTUAL_ENV", sys.prefix)
    package_path = get_package_installation_path()

    print("\nMATRIX STATUS: Welcome to the construct\n")
    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment: {venv_name}")
    print(f"Environment Path: {venv_path}")
    print("")
    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting the global system.")
    print("")
    print("Package installation path:")
    print(f"{package_path}")

def main() -> None:
    """
    Entry point of the program.
    Determines context (inside or outside venv) and calls the right display function.
    """
    try:
        if is_virtual_env():
            display_inside_matrix()
        else:
            display_outside_matrix()
    except Exception as error:
        print(f"MATRIX ERROR: An unexpected error occurred: {error}")
        print("Please check your Python installation.")


if __name__ == "__main__":
    main()
