""" 5. Calculate:
• Training accuracy
• Testing accuracy
Compare both and comment whether the model is overfitting or underfitting.
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

# Create Decision tree model
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

# Q.5) Predict the training and testing data
train_pred = model.predict(X_train)
test_pred = model.predict(X_test)

# Calculate traing accuracy
train_accuracy = accuracy_score(y_train, train_pred)
print(f"Training Accuracy is :{train_accuracy * 100:.2f}%")

# Calculate Testing Accuracy
test_accuracy = accuracy_score(y_test, test_pred)

print(f"Testing Accuracy is : {test_accuracy * 100:.2f}%")

# Compare accuracies
if train_accuracy > test_accuracy:
    print("The model may be overfitting.")

elif train_accuracy < test_accuracy:
    print("The model may be underfitting.")

else:
    print("Training and testing accuracy are equal.")

"""
Output -> Training Accuracy is :100.00%
          Testing Accuracy is : 100.00%
          Training and testing accuracy are equal.

Observation :
Both training and testing accuracy are 100%.
here is no accuracy gap in this particular train-test split, 
so there is no clear evidence of overfitting or underfitting.
"""