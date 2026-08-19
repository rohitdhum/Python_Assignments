""" 3. Consider below task
1. Train linear regression model.
2. Predict salary for 6 years of experience.
3. Plot regression line using matplotlib.

Dataset :->
Experience     Salary
1               20000
2               25000
3               30000
4               35000
5               40000
"""

import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

def main():
    # Load Dataset
    X = np.array([1,2,3,4,5]).reshape(-1, 1)
    Y = np.array([20000, 25000, 30000, 35000, 40000])

    # Create Linear Regression model
    model = LinearRegression()
    model.fit(X,Y)

    Predicted_Salary = model.predict([[6]])
    print(f" Predict salary for 6 years of experience : {Predicted_Salary[0]:.0f}")

    # Plot Histogram
    plt.scatter(X,
                Y,
                color='blue',
                label='Data Points' 
    )

    plt.plot(X,
             model.predict(X),
             color='Red',
             label='Regression Line'
    )

    plt.xlabel("Experience (Years)")
    plt.ylabel("Salary")
    plt.title("Experience Vs Salary")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()

"""
Expected Output
Predicted Salary for 6 Years Experience: ₹45000
Graph should display:
• Data points
• Regression line
"""