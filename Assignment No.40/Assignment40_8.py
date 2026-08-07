""" 8. Decision Tree Visualization
Use:
from sklearn.tree import plot_tree
Visualize the trained decision tree.
"""

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import plot_tree

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

# Create Decision Tree Model
model = DecisionTreeClassifier(random_state=42)

# Train Model
model.fit(X_train, y_train)

##############################################################
# Visualize Decision Tree
##############################################################

plt.figure(figsize=(5, 5))

plot_tree(
    model,
    feature_names=feature_cols,
    class_names=["Fail", "Pass"],
    filled=True
)

plt.title("Decision Tree Visualization")
plt.show()

##############################################################
# Find Root Feature
##############################################################

root_feature_index = model.tree_.feature[0]

root_feature = feature_cols[root_feature_index]

print("Root Node Feature:",root_feature)

"""
• Which feature appears at the root node?
-> Root Node Feature = Attendance

• Why do you think that feature was selected first?
-> The Decision Tree selects a feature that provides the best split of the training data 
   according to its splitting criterion.
   In this dataset, Attendance provides the strongest separation between Pass and Fail students,
   so it appears at the root node.
"""