""" 1. After training the Decision Tree model, use:
model.feature_importances_
• Display importance score of each feature.
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

# Create Decision Tree Model
model = DecisionTreeClassifier(random_state=42)

# Train Model
model.fit(X_train, y_train)

# Get Feature Importance
importance = model.feature_importances_

# Display Feature Importance
print("Feature Importance :")

for feature, score in zip(feature_cols, importance):
    print(feature, ":", score)

# Find Most Important Feature
max_index = importance.argmax()

print("\nMost Important Feature:",
      feature_cols[max_index])

print("Importance Score:",
      importance[max_index])

# Find Least Important Features
min_score = importance.min()

least_features = [
    feature_cols[i]
    for i, score in enumerate(importance)
    if score == min_score
]

print("\nLeast Important Features :",least_features)

print("Least Importance Score:",min_score)

"""
• Which feature contributes the most in predicting FinalResult?
-> Most important feature: Attendance
   Importance score: 1.0

• Which feature contributes the least?
-> Least important features: StudyHours, PreviousScore, AssignmentsCompleted, SleepHours
   Least importance score: 0.0
"""