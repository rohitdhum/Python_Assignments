""" 2. Remove the column SleepHours from the dataset.
• Train the model again.
• Compare new accuracy with previous accuracy.
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

# Create and Train Full Model
model_full = DecisionTreeClassifier(random_state=42)

model_full.fit(X_train_full, y_train)

# Predict
y_pred_full = model_full.predict(X_test_full)

# Calculate Accuracy
accuracy_full = accuracy_score(y_test, y_pred_full)

##############################################################
# Remove SleepHours
##############################################################

new_features = ["StudyHours","Attendance","PreviousScore","AssignmentsCompleted"]

X_new = df[new_features]

# Split Dataset
X_train_new, X_test_new, y_train_new, y_test_new = train_test_split(
    X_new,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

# Create and Train New Model
model_new = DecisionTreeClassifier(random_state=42)

model_new.fit(X_train_new, y_train_new)

# Predict
y_pred_new = model_new.predict(X_test_new)

# Calculate Accuracy
accuracy_new = accuracy_score(y_test_new, y_pred_new)

# Display Results
print(f"Previous Accuracy: {accuracy_full * 100:.2f}%")

print(f"New Accuracy after removing SleepHours: {accuracy_new * 100:.2f}%")

# Compare
if accuracy_new == accuracy_full:
    print("\nRemoving SleepHours did not affect performance.")
elif accuracy_new > accuracy_full:
    print("\nAccuracy improved after removing SleepHours.")
else:
    print("\nAccuracy decreased after removing SleepHours.")

"""
• Does removing this feature affect performance?
-> Removing SleepHours does not affect the model accuracy for this dataset and this train-test split.
"""
