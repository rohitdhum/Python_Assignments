""" 9. Create a new column:
PerformanceIndex = (StudyHours * 2) + Attendance
Train the model including this new feature.
"""

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Load Dataset
DataPath = "student_performance_ml.csv"
df = pd.read_csv(DataPath)

##############################################################
# Create PerformanceIndex
##############################################################

df["PerformanceIndex"] = (df["StudyHours"] * 2) + df["Attendance"]

print("PerformanceIndex column created successfully.")

# Display first 5 records
print("\nFirst 5 Records:")
print(df.head())

##############################################################
# Select Features and Target
##############################################################

feature_cols = ["StudyHours","Attendance","PreviousScore","AssignmentsCompleted","SleepHours","PerformanceIndex"]

X = df[feature_cols]
y = df["FinalResult"]

print(X.shape)
print(y.shape)

##############################################################
# Split Dataset
##############################################################

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

##############################################################
# Train Model
##############################################################

model = DecisionTreeClassifier(random_state=42)

model.fit(X_train, y_train)

##############################################################
# Prediction
##############################################################

y_pred = model.predict(X_test)

##############################################################
# Calculate Accuracy
##############################################################

accuracy = accuracy_score(y_test, y_pred)

# Display Result
print(f"\nTesting Accuracy : {accuracy * 100:.2f}%")

if accuracy > 1.0:
    print("Accuracy improved.")
else:
    print("Accuracy did not improve.")

"""
Does accuracy improve?
-> Therefore, accuracy does not improve. It remains 100%.
"""