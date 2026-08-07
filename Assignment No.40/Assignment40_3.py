""" 3. Train the model using only:
• StudyHours
• Attendance
Compare the accuracy with the full-feature model.
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Load Dataset
DataPath = "student_performance_ml.csv"
df = pd.read_csv(DataPath)

##############################################################
# Full Feature Model
##############################################################

full_features = ["StudyHours","Attendance","PreviousScore","AssignmentsCompleted","SleepHours"]

X_full = df[full_features]
y = df["FinalResult"]

# Split Dataset
X_train_full, X_test_full, y_train, y_test = train_test_split(
    X_full,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

# Train Full Model
model_full = DecisionTreeClassifier(random_state=42)

model_full.fit(X_train_full, y_train)

# Predict
y_pred_full = model_full.predict(X_test_full)

# Accuracy
accuracy_full = accuracy_score(y_test, y_pred_full)

##############################################################
# Model using only StudyHours and Attendance
##############################################################

selected_features = ["StudyHours","Attendance"]

X_selected = df[selected_features]

# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X_selected,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

# Train Model
model = DecisionTreeClassifier(random_state=42)

model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)

# Display Results
print(f"Full Feature Model Accuracy :{accuracy_full * 100:.2f}%")

print(f"StudyHours + Attendance Accuracy :{accuracy * 100:.2f}%")

if accuracy >= 0.80:
    print("\nThe model is still performing well.")
else:
    print("\nThe model performance is low.")

"""
Is the model still performing well?
-> Yes. The model is still performing very well using only StudyHours and Attendance.
"""