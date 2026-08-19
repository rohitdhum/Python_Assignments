""" 7. Write a Python program using LinearRegression to train a regression model using the dataset below.

Study Hours    Marks
1               50
2               55
3               60
4               65
5               70

Your program should:
• Train the regression model
• Print the coefficient
• Print the intercept
"""

import numpy as np
from sklearn.linear_model import LinearRegression

def main():
    # Prepare a Dataset

    # Independent Variables
    X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)

    # Dependent Variables
    Y = np.array([50,55,60,65,70])

    # Initialliz and train the model
    model = LinearRegression()

    model.fit(X,Y)

    print(f"Coeffient : {model.coef_[0]:.1f}")

    print(f"Intercept : {model.intercept_:.1f}")

if __name__ == "__main__":
    main()