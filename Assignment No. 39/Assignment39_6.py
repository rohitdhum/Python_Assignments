""" 6. Train three Decision Tree models with:
• max_depth = 1
• max_depth = 3
• max_depth = None
Compare their testing accuracies and write your observations.
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

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

# Q.6) Model with max_depth = 1
model1 = DecisionTreeClassifier(max_depth=1,random_state=42)
model1.fit(X_train, y_train)
print("\nDecision tree model-1 trained successfully")

# Model with max_depth = 3
model3 = DecisionTreeClassifier(max_depth=3,random_state=42)
model3.fit(X_train, y_train)
print("\nDecision tree model-3 trained successfully")

# Model with max_depth = None
model_None = DecisionTreeClassifier(max_depth=None,random_state=42)
model_None.fit(X_train, y_train)
print("\nDecision tree model-None trained successfully\n")

# Calculate testing accuracy
accuracy1 = accuracy_score(y_test, model1.predict(X_test))
accuracy3 = accuracy_score(y_test, model3.predict(X_test))
accuracy_None = accuracy_score(y_test, model_None.predict(X_test))

print(f"max_depth = 1: {accuracy1 * 100}%")
print(f"max_depth = 3: {accuracy3 * 100}%")
print(f"max_depth = None: {accuracy_None * 100}%")

"""
Observation : All three Decision Tree models achieved 100% testing accuracy on this particular dataset split.
| max_depth | Testing Accuracy |
| --------- | ---------------: |
| 1         |             100% |
| 3         |             100% |
| None      |             100% |

The depth of the tree did not affect the testing accuracy for this particular split.
"""