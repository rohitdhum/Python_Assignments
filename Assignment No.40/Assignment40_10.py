""" 10. Train model with:
• max_depth = None
Calculate:
• Training accuracy
• Testing accuracy
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

# Create Decision Tree with max_depth=None
model = DecisionTreeClassifier(
    max_depth=None,
    random_state=42
)

# Train Model
model.fit(X_train, y_train)

##############################################################
# Training Prediction
##############################################################

train_pred = model.predict(X_train)

##############################################################
# Testing Prediction
##############################################################

test_pred = model.predict(X_test)

##############################################################
# Calculate Training Accuracy
##############################################################

training_accuracy = accuracy_score(y_train, train_pred)

##############################################################
# Calculate Testing Accuracy
##############################################################

testing_accuracy = accuracy_score(y_test, test_pred)

# Display Results
print(f"Training Accuracy:{training_accuracy * 100:.2f}%")

print(f"Testing Accuracy:{testing_accuracy * 100:.2f}%")

# Compare Results
if training_accuracy == 1.0 and testing_accuracy < 1.0:
    print("\nThe model may be overfitting.")

elif training_accuracy < 0.80 and testing_accuracy < 0.80:
    print("\nThe model may be underfitting.")

else:
    print("\nNo clear evidence of overfitting or underfitting.")

"""
If training accuracy is 100% but testing accuracy is lower, explain why this happens.
-> If a Decision Tree has: Training Accuracy = 100%
                           Testing Accuracy < 100%
   it can indicate overfitting.
   This happens because the tree may become too complex and learn the training data very closely, 
   including patterns that do not generalize to unseen data.
   As a result, it performs perfectly on training data but makes mistakes on testing data.

   However, for your actual dataset, both accuracies are:
   Training Accuracy = 100%
   Testing Accuracy  = 100%
   So there is no observed overfitting based on this train-test split.
"""