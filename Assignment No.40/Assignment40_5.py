""" 5. Without using accuracy_score, manually calculate accuracy:
Verify whether it matches sklearn accuracy.
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

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

##############################################################
# Manual Accuracy Calculation
##############################################################

correct_predictions = 0

for actual, predicted in zip(y_test, y_pred):

    if actual == predicted:
        correct_predictions += 1

total_predictions = len(y_test)

manual_accuracy = (correct_predictions / total_predictions) * 100

##############################################################
# Sklearn Accuracy
##############################################################

sklearn_accuracy = accuracy_score(y_test, y_pred) * 100

# Display Results
print("Total Test Students:",total_predictions)

print("Correct Predictions:",correct_predictions)

print("Manual Accuracy:",manual_accuracy, "%")

print("Sklearn Accuracy:",sklearn_accuracy, "%")


# Verify
if manual_accuracy == sklearn_accuracy:
    print("\nManual accuracy matches sklearn accuracy.")
else:
    print("\nManual accuracy does not match sklearn accuracy.")