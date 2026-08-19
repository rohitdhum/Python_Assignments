""" 2. Using the same dataset from above question, calculate model performance.
Tasks
1. Predict all Y values using regression equation.
2. Calculate:
• Mean Squared Error (MSE)
• R2 Score
Show all intermediate calculations.
"""

import numpy as np

def main():
    # Dataset
    X = np.array([1, 2, 3, 4, 5])
    Y = np.array([3, 4, 2, 4, 5])

    # Calculate mean of X and Y
    mean_X = np.mean(X)
    mean_Y = np.mean(Y)

    # Calculate Slope (m)
    Numerator =  np.sum((X-mean_X) * (Y-mean_Y))
    Denominator = np.sum((X-mean_X)**2)

    # Formula of m
    m = Numerator / Denominator

    # Calculate Intercept (c)
    c = mean_Y - (m * mean_X)

    # Predict all Y values using regression equation
    Y_pred =(m * X) + c

    # Calculate Mean Squared Error (MSE)
    # Formula :-> sum of (Y_Actual - Y_Predicted)**2 divided by total number of points
    MSE = np.sum((Y-Y_pred)**2) / len(Y)

    # Calculate R2 Score
    # Formula :-> (Residual Sum of Squares / Total Sum of Squares)
    ss_res = np.sum((Y - Y_pred) ** 2)
    ss_tot = np.sum((Y - mean_Y) ** 2)
    R2_Score = 1 - (ss_res / ss_tot)

    print("--- Model Performance ---")
    print(f"Predicted Y values = {Y_pred}")
    print(f"Mean Squared Error (MSE) = {MSE:.2f}")
    print(f"R² Score = {R2_Score:.4f}")
    
if __name__ == "__main__":
    main()