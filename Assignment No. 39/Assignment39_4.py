""" 4. Generate confusion matrix using sklearn.
Display it using ConfusionMatrixDisplay.
Explain clearly:
• True Positive
• True Negative
• False Positive
• False Negative
"""

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

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

# train the model
model.fit(X_train, y_train)

print("\nDecision tree model trained successfully")

# Predict the results
y_pred = model.predict(X_test)

# Q.4) Generate the confusion matrix
CM = confusion_matrix(y_test, y_pred)

print("Confusion Matrix :")
print(CM)

# Display the confusion matrix
Display = ConfusionMatrixDisplay(confusion_matrix=CM, display_labels=["Fail", "Pass"])

Display.plot()
plt.title("Confusion Matrix")
plt.show()

""" Explaination :
              Predicted Fail	Predicted Pass
Actual Fail	         2	           0
Actual Pass	         0	           4

True Negative (TN) = 2
2 students actually failed and the model correctly predicted Fail.
True Positive (TP) = 4
4 students actually passed and the model correctly predicted Pass.
False Positive (FP) = 0
No failed student was incorrectly predicted as Pass.
False Negative (FN) = 0
No passed student was incorrectly predicted as Fail.
"""