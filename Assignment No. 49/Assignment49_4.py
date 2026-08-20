""" 4. Write a Python program to calculate the Euclidean distance between two points before and after applying
feature scaling, and explain the difference in results.
"""

import numpy as np
from sklearn.preprocessing import StandardScaler

def main():
    P1 = np.array([25,20000])
    P2 = np.array([30,40000])
    Data = np.array([P1, P2, [35,80000]])

    # Calculate Distance before scaling
    Dist_Before = np.linalg.norm(P1 - P2)

    # Scale Dataset
    Scalar = StandardScaler()
    Scaled_Data = Scalar.fit_transform(Data)

    P1_Scaled = Scaled_Data[0]
    P2_Scaled = Scaled_Data[1]

    # Calculate Distance after scaling
    Dist_After = np.linalg.norm(P1_Scaled - P2_Scaled)

    print(f"Euclidean Distance before scaling : {Dist_Before:.4f}")
    print(f"Euclidean Distance after scaling : {Dist_After:.4f}")

    print("\n-----------------------------------------------")
    print("\n-------------Result Before Scaling-------------")

    print("\nBefore Scaling: Feature 2 (income/money values up to 80,000) completely dominates the distance calculation."
          "\nThe tiny difference in Feature 1 (Age: (30 - 25 = 5)) becomes numerically irrelevant compared to" 
          "\nthe massive scale of Feature 2 ((40,000 - 20,000 = 20,000)).") 

    print("\n-----------------------------------------------")

    print("\n-------------Result After Scaling-------------")

    print("\nStandardScaler shifts data to center around a mean of 0 with a standard deviation of 1."
          "\nBoth features now sit on an equal playing field."
          "\nThe resulting distance treats both attributes with equal importance, preventing feature scale bias.")

    print("\n-----------------------------------------------")

if __name__ == "__main__":
    main()