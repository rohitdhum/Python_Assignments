""" 1. Implement Simple Linear Regression manually without using any ML library.
Dataset
X = [1,2,3,4,5]
Y = [3,4,2,4,5]

Tasks
Calculate:
1. Mean of X (X̄ )
2. Mean of Y (Ȳ)
3. Slope (m)
4. Intercept (c)
"""

import numpy as np

def main():
    # Dataset
    X = np.array([1,2,3,4,5])

    Y = np.array([3,4,2,4,5])

    # Calculate mean of X and Y
    Mean_X = np.mean(X)
    Mean_Y = np.mean(Y)

    # Calculate Slop(m)
    # Formula :-> m = sum((X-Mean_X) * (Y-Mean_Y) / Sum(X-Mean_X)**2)
    Numerator = np.sum((X - Mean_X) * (Y - Mean_Y))
    Denominator = np.sum((X-Mean_X) ** 2)

    m = Numerator / Denominator

    # Calculate Intercept
    # Formula :-> c = (m * Mean_Y) - Mean_Y 
    c = Mean_Y - (m * Mean_X) 

    # Predict Y for X = 6
    X_pred = 6
    Y_pred = (m * X_pred) + c

    print(f"Mean of X = {Mean_X:.0f}")
    print(f"Mean of Y = {Mean_Y:.1f}")
    print(f"Slope (m) = {m:.1f}")
    print(f"Intercept (c) = {c:.1f}")
    print(f"Regression Equation:\nY = {m:.1f}X + {c:.1f}")
    print(f"Predicted Y for X = 6 : {Y_pred:.1f}")
    
if __name__ == "__main__":
    main()

"""
Expected Output Example
Mean of X = 3
Mean of Y = 3.6
Slope (m) = 0.4
Intercept (c) = 2.4
Regression Equation:
Y = 0.4X + 2.4
Predicted Y for X = 6 : 4.8
"""