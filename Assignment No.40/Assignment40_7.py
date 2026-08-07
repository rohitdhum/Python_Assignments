""" 7. Train model using:
• random_state = 0
• random_state = 10
• random_state = 42
Compare testing accuracy.
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

##############################################################
# random_state = 0
##############################################################

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=0,
    stratify=y
)

model0 = DecisionTreeClassifier(random_state=42)

model0.fit(X_train, y_train)

y_pred0 = model0.predict(X_test)

accuracy0 = accuracy_score(
    y_test,
    y_pred0
)

##############################################################
# random_state = 10
##############################################################

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=10,
    stratify=y
)

model10 = DecisionTreeClassifier(random_state=42)

model10.fit(X_train, y_train)

y_pred10 = model10.predict(X_test)

accuracy10 = accuracy_score(
    y_test,
    y_pred10
)

##############################################################
# random_state = 42
##############################################################

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

model42 = DecisionTreeClassifier(random_state=42)

model42.fit(X_train, y_train)

y_pred42 = model42.predict(X_test)

accuracy42 = accuracy_score(
    y_test,
    y_pred42
)

# Display Results
print("Testing Accuracy:")

print(f"random_state = 0 :{accuracy0 * 100:.2f}%")

print(f"random_state = 10 :{accuracy10 * 100:.2f}%")

print(f"random_state = 42 :{accuracy42 * 100:.2f}%")

"""
Does the result change?
-> No. For this dataset, all three random states give 100% testing accuracy.
"""