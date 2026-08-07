""" 6. Identify students where:
y_test != y_pred
• Display those rows.
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

# Predict
y_pred = model.predict(X_test)

# Find misclassified rows
misclassified = X_test[y_test != y_pred].copy()

# Add actual result
misclassified["ActualResult"] = y_test[y_test != y_pred]

# Add predicted result
misclassified["PredictedResult"] = y_pred[y_test != y_pred]

# Display misclassified students
print("Misclassified Students:")

print(misclassified)

# Count misclassified students
count = len(misclassified)

print("\nNumber of Misclassified Students:",count)

# Observation
if count == 0:
    print("\nNo students were misclassified.")
    print("All test students were predicted correctly.")

else:
    print("\nSome students were misclassified.")
    print("Observe their feature values for common patterns.")

"""
• How many students were misclassified?
-> Misclassified students = 0
   Incorrect predictions = 0

• What common pattern do you observe?
-> Common pattern: There is no misclassification in this particular test set.
"""