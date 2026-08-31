# Customer Loan Approval Using Voting Classification

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.metrics import accuracy_score

Border = "-" * 50
##########################################################
# Step 1 : Load the data
##########################################################

print(Border)
print("Step 1 : Load the data")
print(Border)

df = pd.read_csv("Customer_Loan_Approval.csv")

print("Shape of Dataset :", df.shape)

print("First few records :")
print(df.head())

##########################################################
# Step 2 : Check Missing Values
##########################################################

print(Border)
print("Step 2 : Check Missing Values")
print(Border)

print("Missing Values are :")
print(df.isnull().sum())

##########################################################
# Step 3 : Separate Input Output variables
##########################################################

print(Border)
print("Step 3 : Separate Input Output Variables")
print(Border)

X = df.drop("LoanApproved", axis = 1)
Y = df["LoanApproved"]

print("Input Variables :")
print(X.head())

print("Output Variables :")
print(Y.head())

##########################################################
# Step 4 : Split the dataset into training and testing 
##########################################################

print(Border)
print("Step 4 : Split the dataset into training and testing")
print(Border)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

print("training Data :", X_train.shape)
print("Testing Data :", X_test.shape)

##########################################################
# Step 5 : Train the data using Logistic Regression
##########################################################

print(Border)
print("Step 5 : Train the data using Logistic Regression")
print(Border)

log_model = LogisticRegression(random_state=42, max_iter=1000)

log_model = log_model.fit(X_train, Y_train)

print("Data training (Logistic Regression) is successfully completed")

Y_pred = log_model.predict(X_test)

log_accuracy = accuracy_score(Y_test, Y_pred)

print("Logistic Regression Accuracy :", log_accuracy * 100,"%")

##########################################################
# Step 6 : Train the data using Decision Tree
##########################################################

print(Border)
print("Step 6 : Train the data using Decision Tree")
print(Border)

dec_tree_model = DecisionTreeClassifier(random_state=42)

dec_tree_model = dec_tree_model.fit(X_train, Y_train)

print("Data training (Decision Tree) is successfully completed")

Y_pred = dec_tree_model.predict(X_test)

dec_tree_accuracy = accuracy_score(Y_test, Y_pred)

print("Decision Tree Accuracy :", dec_tree_accuracy * 100,"%")

##########################################################
# Step 7 : Train the data using K-Nearest Neighbors
##########################################################

print(Border)
print("Step 7 : Train the data using K-Nearest Neighbors")
print(Border)

KNN_model = KNeighborsClassifier(n_neighbors=5)

KNN_model = KNN_model.fit(X_train, Y_train)

print("Data training of (K-Nearest Kneigbours) is successfully completed")

Y_pred = KNN_model.predict(X_test)

KNN_accuracy = accuracy_score(Y_test, Y_pred)

print("K-Nearest Neighbours Accuracy :", KNN_accuracy * 100, "%")

##########################################################
# Step 8 : Create a Hard Voting Classifier
##########################################################

print(Border)
print("Step 8 : Create a Hard Voting Classifier")
print(Border)

hard_voting = VotingClassifier(
    estimators=[
        ("logistic", log_model),
        ("decision_tree", dec_tree_model),
        ("knn", KNN_model)
    ],
    voting='hard'
)

hard_voting_model = hard_voting.fit(X_train, Y_train)

Y_pred_hard = hard_voting_model.predict(X_test)

hard_voting_accuracy = accuracy_score(Y_test, Y_pred_hard)

print("Hard Voting Accuracy is :", hard_voting_accuracy * 100,"%")

##########################################################
# Step 9 : Create a Soft Voting Classifier
##########################################################

print(Border)
print("Step 9 : Create a Soft Voting Classifier")
print(Border)

soft_voting = VotingClassifier(
    estimators=[
        ("logistic", log_model),
        ("decision_tree", dec_tree_model),
        ("knn", KNN_model)
    ],
    voting='soft'
)

soft_voting_model = soft_voting.fit(X_train, Y_train)

Y_pred_soft = soft_voting_model.predict(X_test)

soft_voting_accuracy = accuracy_score(Y_test, Y_pred_soft)

print("Soft Voting Accuracy is :", soft_voting_accuracy * 100,"%")

##########################################################
# Step 10 : Model Accuracy Comparison
##########################################################

print(Border)
print("Step 10 : Model Accuracy Comparison")
print(Border)

print("Logistic Regression :", log_accuracy * 100,"%")
print("Decision Tree Classifier :", dec_tree_accuracy * 100,"%")
print("K-Nearest Neighbours  :", KNN_accuracy * 100,"%")
print("Hard Voting :", hard_voting_accuracy * 100,"%")
print("Soft Voting :", soft_voting_accuracy * 100,"%")