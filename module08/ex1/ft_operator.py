import sys
import importlib


def main():
    """ Data analysis program"""
    if sys.prefix == sys.base_prefix:
        print("You are not in a VE")
    else:
        dependencies_dic = {"pandas": "Data manipulation",
                            "numpy": "for pandas",
                            "requests": "Network acess ready",
                            "matplotlib": "Visualisation ready"}
        try:
            for name, desc in dependencies_dic.items():
                depend = importlib.import_module(name)
                print(f"[OK] {depend.__name__} ({depend.__version__}) "
                      f"- {desc}")
        except ModuleNotFoundError:
            print(f"use either requirements or poetry to install {name}")
        else:
            import numpy as np
            import matplotlib.pyplot as plt
            print("\nAnalyzing Matrix data...\n"
                  "Processing 1000 data points...\n"
                  "Generating visualization...")
            data = np.random.randn(1000)
            plt.figure(figsize=(10, 6))
            plt.plot(data, color='green')
            plt.title("Matrix Data Stream Analysis")
            plt.xlabel("Random x values")
            plt.ylabel("Random y values")
            plt.savefig('analysis.png')
            print("\nAnalysis complete!")
            print("Results saved to: matrix/analysis.png")


if __name__ == "__main__":
    main()
