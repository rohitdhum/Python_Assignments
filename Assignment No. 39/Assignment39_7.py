""" 7. Use the trained model to predict result for a student with:
• StudyHours = 6
• Attendance = 85
• PreviousScore = 66
• AssignmentsCompleted = 7
• SleepHours = 7
Will the student Pass or Fail?
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# Load Dataset
print("Load the data :")

DataPath = "student_performance_ml.csv"
df = pd.read_csv(DataPath)

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

# train the model
model.fit(X_train, y_train)
print("\nDecision tree model trained successfully")

# Create a new stdent data
New_Student = pd.DataFrame({
  "StudyHours": [6],
  "Attendance": [85],
  "PreviousScore": [66],
  "AssignmentsCompleted": [7],
  "SleepHours": [7]
})

print("New student data created successfully")

# Predict the result
Prediction = model.predict(New_Student)

if Prediction[0] == 1:
    print("Student will pass")
else:
    print("Student will fail")