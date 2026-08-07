""" 8. Write a single structured Python program that performs:
1. Dataset loading
2. Data analysis
3. Visualization
4. Train-test split
5. Model training
6. Prediction
7. Accuracy calculation
8. Confusion matrix generation
9. Final conclusion
Your code should include proper comments explaining each step.
"""

################################################
# import required liabraries
################################################

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

################################################
# 1. Dataset loading
################################################

# Load Dataset
print("----------Load the data----------")

DataPath = "student_performance_ml.csv"
df = pd.read_csv(DataPath)

print("\nData loaded successfully")
print("\nFirst 5 records :")
print(df.head())

################################################
# 1. Data analysis
################################################

# Data Analysis
print("\n----------Data Analysis----------")

# Display daaset information
print("\nTotal number of students :",len(df))

print("\nTotal number of columns :",len(df.columns))

print("\nColumn Names :",df.columns.tolist())

# Count pass and fail students
Passed = (df["FinalResult"] == 1).sum()
Failed = (df["FinalResult"] == 0).sum()

print("\nTotal Passed Students :",Passed)
print("\nTotal Failed Students :", Failed)

# Calculate basic statistics
print("\nAverage study hours :",df["StudyHours"].mean())
print("\nAverage Attendance :",df["Attendance"].mean())
print("\nMaximum previous score :",df["PreviousScore"].max())
print("\nMinimum Sleep hours :",df["SleepHours"].min())

################################################
# 3. Visualization
################################################

# Visualization
print("\n----------Visualization----------")

# Histogram of StudyHours
plt.hist(df["StudyHours"],bins=8,edgecolor="black")

plt.xlabel("Study Hours")
plt.ylabel("Number of Students")
plt.title("Distribution of Study Hours")
plt.show()

################################################
# 4. Separate Features and Target
################################################

print("\n----------Separate Features and Target----------")

# Separate input feature and target/label 
# X : Independent Variable(Features)
# Y : Depenedent Variables(Labels)
feature_cols = ["StudyHours", "Attendance", "PreviousScore", "AssignmentsCompleted", "SleepHours"]

# Independent variables
X = df[feature_cols]

# Dependent variables
y = df["FinalResult"]

print("Features selected successfully.")
print("Target variable : FinalResult")

################################################
# 5. Train-Test Split
################################################

print("\n----------Train-Test Split----------")
# Split Dataset into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X,y,
    test_size=0.20,
    random_state=43,
    stratify=y)

print("Training samples:", len(X_train))
print("Testing samples:", len(X_test))

################################################
# 6. Model Training
################################################

print("\n----------Model Traning----------")

# Create Decision tree model
model = DecisionTreeClassifier(random_state=42)

# train the model
model.fit(X_train, y_train)

print("\nDecision tree model trained successfully")

################################################
# 7. Prediction
################################################

print("\n----------Prediction----------")

# Predict test data
y_pred = model.predict(X_test)

print("Predicted values :")
print(y_pred)

print("Actual values :")
print(y_test.values)

################################################
# 8. Accuracy Calculation
################################################

print("\n----------Accuracy Prediction----------")

# Accuracy Calculation
Accuracy = accuracy_score(y_test, y_pred)
print(f"Testing Accuracy is :{Accuracy * 100:.2f}%")

################################################
# 9. Confusion Matrix
################################################

print("\n----------Confusion Matrix----------")

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)

print("Confusion Matrix :")
print(cm)

# Display Confusion Matrix
Disp = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=["Fail", "Pass"]
)

Disp.plot()
plt.title("Decision Tree Confusion Matrix")
plt.show()

################################################
# 10. Final Conclusion
################################################

print("\n----------Final Conclusion----------")

print("Total Students", len(df))
print("Total Passed Stdents :", Passed)
print("Total Failed Students :", Failed)
print(f"Testing Accuracy :{Accuracy * 100:.2f}%")
print("\nThe Decision Tree model was successfully")
print("trained and evaluated on the Student Performance dataset.")

if Accuracy >= 0.80:
    print("The model shows good performance")
else:
    print("The model need improvement")

print("\nFinal Conclusion:")
print("The model predicts whether a student will")
print("Pass or Fail based on academic and behavioral features.")