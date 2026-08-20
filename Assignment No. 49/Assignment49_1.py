""" 1. Write a Python program that calculates the mean of a dataset using NumPy for the following values:
[6, 7, 8, 9, 10, 11, 12]
"""

import numpy as np

def main():
    Data = np.array([6,7,8,9,10,11,12])

    Mean_Data = np.mean(Data)

    print(f"The mean of Dataset : {Mean_Data}")

if __name__ == "__main__":
    main()