""" 3. Write a Python program using StandardScaler to perform feature scaling on the following dataset:
[[25,20000],
[30,40000],
[35,80000]]
Print the scaled dataset.
"""

import numpy as np
from sklearn.preprocessing import StandardScaler

def main():
    Data = np.array([
        [25,20000],
        [30,40000],
        [35,80000]
    ])

    Scalar = StandardScaler()

    Scaled_Data = Scalar.fit_transform(Data)

    print(f"Scaled Dataset : {Scaled_Data}")

if __name__ == "__main__":
    main()