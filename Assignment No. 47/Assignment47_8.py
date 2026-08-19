""" 8. Using the regression model created in the previous question, write a Python program to predict marks for 6
study hours and display the predicted value.
"""

import numpy as np
from sklearn.linear_model import LinearRegression

def main():
    # Independent Variables
    X = np.array([1,2,3,4,5]).reshape(-1,1)

    # Dependendent Variables
    Y = np.array([50,55,60,65,70])

    # Initialize and train the model
    model = LinearRegression()
    model.fit(X,Y)

    # Define the input hours to predict (6 hours)
    # We pass it as a 2D array [[6]] so scikit-learn accepts its shape
    Predicted_Hours = np.array([[6]])

    Predicted_Marks = model.predict(Predicted_Hours)

    print(f"Predicted marks for 6 study hours : {Predicted_Marks[0]:.1f}")

if __name__ == "__main__":
    main()