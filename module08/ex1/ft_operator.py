import sys


def main():
    """ Data analysis program"""
    if sys.prefix == sys.base_prefix:
        print("You are not in a VE")
    else:
        try:
            import pandas
            import requests
            import matplotlib
            print(f"[OK] {pandas.__name__} ({pandas.__version__}) "
                  "- Data manipulation ready")
            print(f"[OK] {requests.__name__} ({requests.__version__})- "
                  "Data manipulation ready")
            print(f"[OK] {matplotlib.__name__} ({matplotlib.__version__})- "
                  "Data manipulation ready")
            print("\nAnalyzing Matrix data...\n"
                  "Processing 1000 data points...\n"
                  "Generating visualization...")

            print("\nAnalysis complete!")
            print("Results saved to: matrix/analysis.png")
        except ModuleNotFoundError:
            print("use either requirements or toml to install dependencies")


if __name__ == "__main__":
    main()
