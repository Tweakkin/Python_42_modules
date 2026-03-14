import importlib
import importlib.util

PACKAGES = ["pandas", "numpy", "matplotlib", "requests"]

def check_dependencies() -> bool:
    print("\nLOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")

    all_ok = True

    for name in PACKAGES:
        try:
            spec = importlib.util.find_spec(name)
            if spec is None:
                print(f"[MISS] {name} - not installed")
                all_ok = False
            else:
                module = importlib.import_module(name)
                version = getattr(module, "__version__", "unknown")
                print(f"[OK] {name} ({version})")
        except Exception as error:
            print(f"[ERROR] {name} - {error}")
            all_ok = False

    return all_ok


def show_install_instructions() -> None:
    print("\nMissing dependencies. Install them:\n")
    print("  pip:    pip install -r requirements.txt")
    print("  Poetry: poetry install")

def run_analysis() -> None:
    try:
        import numpy as np
        import pandas as pd
        import matplotlib.pyplot as plt

        print("\nAnalyzing Matrix data...")
        print("Processing 1000 data points...")

        # creates 1000 evenly spaced numbers between 0 and 10.
        # Like range() but for floats.
        data_points = np.random.randint(0, 100, size=1000)

        # pandas put in a table
        data = pd.DataFrame({"values": data_points})

        # matplotlib — draw and save
        print("Generating visualization...")
        data.plot()
        plt.savefig("matrix_analysis.png")
        plt.close()

        print("\nAnalysis complete!")
        print("Results saved to: matrix_analysis.png")

    except ImportError as error:
        print(f"Import failed: {error}")
    except Exception as error:
        print(f"Analysis failed: {error}")


def main() -> None:
    all_ok = check_dependencies()

    if all_ok:
        run_analysis()
    else:
        show_install_instructions()

if __name__ == "__main__":
    main()