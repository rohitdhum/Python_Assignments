""" 2. Write a Python program that calculates the variance and standard deviation of the dataset:
[6, 7, 8, 9, 10, 11, 12]
Display both results.
"""

import numpy as np

def main():
    Data = np.array([6,7,8,9,10,11,12])

    Variance = np.var(Data)

    Standard_Deviation = np.std(Data)

    print(f"Variance of Dataset : {Variance}")

    print(f"Standard Deviation of Dataset : {Standard_Deviation}")

if __name__ == "__main__":
    main()