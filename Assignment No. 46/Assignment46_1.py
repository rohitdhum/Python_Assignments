import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

def LinearRegressionPredictor():
    Border = "_" * 40

    # Load the Dataset
    print(Border)
    print("Step 1 : Load the Dataset")
    print(Border)

    df = pd.read_csv("Advertising.csv")

    print(df.head())

    # Clean Prepare and Manipulate the Data
    print(Border)
    print("Step 2 : Clean Prepare and Manipulate the Data")
    print(Border)

    # Remove unwanted column
    print(Border)
    print("Remove unwanted column")
    print(Border)

    if "Unnamed: 0" in df.columns:
        df = df.drop(columns=["Unnamed: 0"])

    print(df.head())

    # Check Missing values
    print(Border)
    print("Check Missing Values")
    print(Border)

    print("Total Missing Values :")
    print(Border)
    print(df.isnull().sum())
    print(Border)

    # Statistical Summary
    print(Border)
    print("Step 4 : Statistical Summary")
    print(Border) 

    print(df.describe())

    # Correlation
    print(Border)
    print("Step 5 : Correlation")
    print(Border) 

    print(df.corr())

    # Separate Independent and Dependent Variables
    print(Border)
    print("Separate Independent and Dependent Variables :")
    print(Border)

    X = df[['TV', 'radio', 'newspaper']]
    Y = df['sales']

    print("Independent Variables :")
    print(X.head())

    print("Dependent Variables")
    print(Y.head())

    # Split the Data (As per the Assignment 1st half is for training and 2nd half is for testing)
    total_records = len(df)
    half_index = total_records // 2

    X_train = X.iloc[:half_index] 
    X_test = X.iloc[half_index:]
    Y_train = Y.iloc[:half_index]
    Y_test = Y.iloc[half_index:]

    print("Training Data :", X_train.shape)
    print("Testing Data :", X_test.shape)

    # Create and Train the Data
    print(Border)
    print("Step 3 : Create and Train the Data")
    print(Border)

    model = LinearRegression()

    model.fit(X_train, Y_train)

    print("Model Trained Succussfully")

    # Predict the Data
    Y_pred = model.predict(X_test)

    print("Expected Answer :")
    print(Y_test[:3])

    print("Actual Answer :")
    print(Y_pred[:3])

    # Evaluate the model
    print(Border)
    print("Evaluate the model")
    print(Border)

    MSE = mean_squared_error(Y_test, Y_pred)

    RMSE = np.sqrt(MSE)

    R2 = r2_score(Y_test, Y_pred)

    print("MSE :", MSE)
    print("RMSE :", RMSE)
    print("R2 :", R2)

    # Step 4 : Display Coefficient
    print(Border)
    print("Step 4 : Display Coefficient")
    print(Border)

    print("TV Coefficient :", model.coef_[0])
    print("Radio Coefficient :", model.coef_[1])
    print("NewsPaper Coefficient :", model.coef_[2])

    print(Border)

    print("Intercepts :", model.intercept_)

    # Display your visualization graph
    plt.plot(range(len(Y_test)), Y_pred, color='g', label='Regression Line')
    plt.scatter(range(len(Y_test)), Y_test, color='r', label='Scatter Plot')
    plt.xlabel("Tested Record Index Offset")
    plt.ylabel("Sales Units")
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    LinearRegressionPredictor()

if __name__ == "__main__":
    main()