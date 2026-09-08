#########################################################
# Employee Attrition Prediction using Deep Learning
#########################################################
# 1. Load the dataset using Pandas.
# 2. Display the shape, columns and first five records.
# 3. Check for missing values.
# 4. Identify numerical and categorical features.
# 5. Convert categorical features such as OverTime into numerical representation.
# 6. Convert the target Attrition into 0 and 1.
# 7. Separate independent and dependent variables.
# 8. Divide the dataset into training and testing data.
# 9. Apply appropriate feature scaling.
# 10. Design an MLP with at least two hidden layers.
# 11. Train the network.
# 12. Display the number of iterations required for training.
# 13. Calculate training accuracy.
# 14. Calculate testing accuracy.
# 15. Generate a confusion matrix.
# 16. Plot the loss curve.
# 17. Create a function: PredictAttrition(employee_data)
# 18. Test the system using at least five new employee records.
#########################################################

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

Border = "-" * 50
#########################################################
# 1. Load the Data
#########################################################

print(Border)
print("1. Load the Data")
print(Border)

data = pd.read_csv("Employee_Attrition.csv")

print("Data loaded Successfully")

#########################################################
# 2. Display shape of columns and few records
#########################################################

print(Border)
print("2. Display shape of columns and few records")
print(Border)

print("Shape of Dataset :", data.shape)

print("Columns :", data.columns)

print("Few Records :") 
print(data.head()) 

#########################################################
# 3. Check Missing values
#########################################################

print(Border)
print("3. Check Missing values")
print(Border)

print("Missing Values :")
print(data.isnull().sum())

#########################################################
# 4. Identify Numerical and Categorical Features
#########################################################

print(Border)
print("4. Identify Numerical and Categorical Features")
print(Border)

Numerical_Features = [
    'Age',
    'MonthlyIncome',
    'YearsAtCompany',
    'TotalWorkingYears',
    'DistanceFromHome', 
    'JobSatisfaction', 
    'WorkLifeBalance', 
    'NumCompaniesWorked', 
    'TrainingTimesLastYear'
]

Categorical_Features = [
    'OverTime'
]

print("Numerical Features :")
print(Numerical_Features)

print("Categorical Features :")
print(Categorical_Features)

#########################################################
# 5. Convert categorical features such as OverTime into numerical representation.
#########################################################

print(Border)
print("5. Convert categorical features such as OverTime into numerical representation.")
print(Border)

data['OverTime'] = data['OverTime'].map({
    "Yes": 1,
    "No" : 0
})

print(data)

#########################################################
# 6. Convert the target Attrition into 0 and 1.
#########################################################

print(Border)
print("6. Convert the target Attrition into 0 and 1.")
print(Border)

data['Attrition'] = data['Attrition'].map({
    "Yes" : 1,
    "No" : 0
})

print(data)

#########################################################
# 7. Separate independent and dependent variables.
#########################################################

print(Border)
print("7. Separate independent and dependent variables.")
print(Border)

X = data.drop('Attrition', axis=1)
Y = data['Attrition']

print("(Independent) Input Features :")
print(X.head())

print("Target :")
print(Y.head())

#########################################################
# 8. Training, testing and Spliting the data.
#########################################################

print(Border)
print("8. Training, testing and Spliting the data.")
print(Border)

X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.2, random_state=42)

print("Training Input Shape :", X_train.shape)
print("Testing Input Shape :", X_test.shape)
print("Training Output Shape :", Y_train.shape)
print("Testing Output Shape :", Y_test.shape)

#########################################################
# 9. feature scaling.
#########################################################

print(Border)
print("9. feature scaling.")
print(Border)

scalar = StandardScaler()

X_train_scaled = scalar.fit_transform(X_train)

X_test_scaled = scalar.fit_transform(X_test)

print("Scaled Training Data :")
print(X_train_scaled[:5])

#########################################################
# 10. Create MLP Classifier
#########################################################

print(Border)
print("10. Create MLP Classifier")
print(Border)

model = MLPClassifier(
    hidden_layer_sizes=(16,8),
    activation='relu',
    solver='adam',
    max_iter=1000,
    random_state=42
)

print("MLP model created")

print(model)

#########################################################
# 11. Train the model.
#########################################################

print(Border)
print("11. Train the model.")
print(Border)

model.fit(X_train_scaled, Y_train)
print("Model Training Completed")


#########################################################
# 12. Number of iterations required for training.
#########################################################

print(Border)
print("12. Number of iterations required for training.")
print(Border)

print(model.n_iter_)

#########################################################
# 13. Training accuracy.
#########################################################

print(Border)
print("13. Training accuracy.")
print(Border)

Y_train_pred = model.predict(X_train_scaled)

Accuracy_train = accuracy_score(Y_train, Y_train_pred)

print(f"{Accuracy_train * 100:.2f}%")

#########################################################
# 14. Testing accuracy.
#########################################################

print(Border)
print("14. Testing accuracy.")
print(Border)

Y_test_pred = model.predict(X_test_scaled)

Accuracy_test = accuracy_score(Y_test, Y_test_pred)

print(F"{Accuracy_test * 100:.2f}%")

#########################################################
# 15. Confusion matrix.
#########################################################

print(Border)
print("15. Confusion matrix.")
print(Border)

cm = confusion_matrix(Y_test, Y_test_pred)

print(cm)

#########################################################
# 16. Plot the loss curve.
#########################################################

print(Border)
print("16. Plot the loss curve.")
print(Border)

model.loss_curve_

plt.figure(figsize=(8,5))
plt.plot(model.loss_curve_)
plt.title("MLP Training Loss Curve")
plt.xlabel("Iterations")
plt.ylabel("Loss")
plt.grid(True)
plt.show()

#########################################################
# 17. Create a function: PredictAttrition(employee_data)
#########################################################

print(Border)
print("17. Create a function: PredictAttrition(employee_data)")
print(Border)

def PredictAttrition(employee_data):

    # Convert input into Dataframe
    employee_df = pd.DataFrame([employee_data])

    # Convert OverTime
    employee_df['OverTime'] = employee_df['OverTime'].map({
        "Yes" : 1,
        "No" : 0
    })

    # Applying scaler during training
    employee_scaled = scalar.fit_transform(employee_df)

    # Prediction
    prediction = model.predict(employee_scaled)

    if prediction[0] == 1:
        print("Employee is likely to leave")
    else:
        print("Employee is likely to stay")

#########################################################
# 18. Test the system using new employee records.
#########################################################

print(Border)
print("18. Test the system using new employee records.")
print(Border)

employee1 = {
    "Age" : 25,
    "MonthlyIncome" : 25000,
    "YearsAtCompany" : 1,
    "TotalWorkingYears" : 2,
    "DistanceFromHome" : 25,
    "JobSatisfaction" : 2,
    "WorkLifeBalance" : 2,
    "OverTime" : "Yes",
    "NumCompaniesWorked" : 3, 
    "TrainingTimesLastYear" : 2
}

employee2 = {
    "Age" : 45,
    "MonthlyIncome" : 120000,
    "YearsAtCompany" : 12,
    "TotalWorkingYears" : 20,
    "DistanceFromHome" : 5,
    "JobSatisfaction" : 4,
    "WorkLifeBalance" : 4,
    "OverTime" : "No",
    "NumCompaniesWorked" : 2, 
    "TrainingTimesLastYear" : 5
}

employee3 = {
    "Age" : 28,
    "MonthlyIncome" : 35000,
    "YearsAtCompany" : 2,
    "TotalWorkingYears" : 5,
    "DistanceFromHome" : 35,
    "JobSatisfaction" : 1,
    "WorkLifeBalance" : 2,
    "OverTime" : "Yes",
    "NumCompaniesWorked" : 6, 
    "TrainingTimesLastYear" : 1
}

employee4 = {
    "Age" : 50,
    "MonthlyIncome" : 100000,
    "YearsAtCompany" : 15,
    "TotalWorkingYears" : 25,
    "DistanceFromHome" : 8,
    "JobSatisfaction" : 4,
    "WorkLifeBalance" : 4,
    "OverTime" : "No",
    "NumCompaniesWorked" : 2, 
    "TrainingTimesLastYear" : 4
}

employee5 = {
    "Age" : 32,
    "MonthlyIncome" : 50000,
    "YearsAtCompany" : 3,
    "TotalWorkingYears" : 8,
    "DistanceFromHome" : 40,
    "JobSatisfaction" : 2,
    "WorkLifeBalance" : 2,
    "OverTime" : "Yes",
    "NumCompaniesWorked" : 5, 
    "TrainingTimesLastYear" : 2
}

print("Employee 1 :")
print(PredictAttrition(employee1))

print("Employee 2 :")
print(PredictAttrition(employee2))

print("Employee 3 :")
print(PredictAttrition(employee3))

print("Employee 4 :")
print(PredictAttrition(employee4))

print("Employee 5 :")
print(PredictAttrition(employee5))