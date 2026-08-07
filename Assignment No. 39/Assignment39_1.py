""" 1. Import DecisionTreeClassifier from sklearn.
Create a model object and train it using fit().
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# Load Dataset
print("Load the data :")

DataPath = "student_performance_ml.csv"
df = pd.read_csv(DataPath)

print("\nData loaded successfully")

# Separate input feature and target/label 
# X : Independent Variable(Features)
# Y : Depenedent Variables(Labels)
print("\nDecide Independent and Dependent Variables")

feature_cols = ["StudyHours", "Attendance", "PreviousScore", "AssignmentsCompleted", "SleepHours"]

X = df[feature_cols]
y = df["FinalResult"]

# Split Dataset into training and testing data
print("\nSplit the dataset for traning and testing")

X_train, X_test, y_train, y_test = train_test_split(
    X,y,
    test_size=0.20,
    random_state=43,
    stratify=y)

# Create Decision tree model
model = DecisionTreeClassifier(random_state=42)

# train the model
model.fit(X_train, y_train)

print("\nDecision tree model trained successfully")

print("X shape :", X.shape)
print("y shape :", y.shape)

print("X_train :", X_train.shape)
print("X_test :", X_test.shape)

print("y_train :", y_train.shape)
print("y_test :", y_test.shape)