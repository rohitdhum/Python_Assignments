""" 4. Create a new DataFrame with details of 5 new students.
Use the trained model to predict their results.
Display predictions clearly.
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# Load Dataset
DataPath = "student_performance_ml.csv"
df = pd.read_csv(DataPath)

# Select Features and Target
feature_cols = ["StudyHours","Attendance","PreviousScore","AssignmentsCompleted","SleepHours"]

X = df[feature_cols]
y = df["FinalResult"]

# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

# Create and Train Model
model = DecisionTreeClassifier(random_state=42)

model.fit(X_train, y_train)

##############################################################
# Create DataFrame for 5 New Students
##############################################################

new_students = pd.DataFrame({
    "StudyHours": [2, 4, 6, 7, 8],
    "Attendance": [65, 75, 85, 90, 95],
    "PreviousScore": [45, 55, 66, 72, 78],
    "AssignmentsCompleted": [3, 5, 7, 8, 9],
    "SleepHours": [5, 6, 7, 8, 8]
})

# Predict Results
predictions = model.predict(new_students)

# Add Prediction Column
new_students["PredictedResult"] = predictions

# Convert 0 and 1 to Fail and Pass
new_students["Result"] = new_students["PredictedResult"].map({
    0: "Fail",
    1: "Pass"
})

# Display Results
print("Predictions for 5 New Students:")
print(new_students)