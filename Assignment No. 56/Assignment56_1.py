# Fraudulent Transaction Detection

import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeClassifier

from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import VotingClassifier

from sklearn.linear_model import LogisticRegression

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

Border = "-" * 50

##########################################################
# Step 1 : Load the data
##########################################################
print(Border)
print("Step 1 : Load the Data")
print(Border)

df = pd.read_csv("Fraudulent_Transaction_Detection.csv")

print("Shape of Dataset :", df.shape)

print("First few records :")
print(df.head())

##########################################################
# Step 2 : Separate features and labels
##########################################################
print(Border)
print("Step 2 : Separate features labels")
print(Border)

X = df.drop("Fraud", axis=1)
Y = df["Fraud"]

print("Independent Features :", X.columns)

##########################################################
# Step 3 : Splitting the data
##########################################################
print(Border)
print("Step 3 : Splitting the data")
print(Border)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

print("Training Data :", X_train.shape)
print("Testing Data :", X_test.shape)

##########################################################
# Step 4 : Create Decision tree model
##########################################################
print(Border)
print("Step 4 : Create Decision tree model")
print(Border)

DT_model = DecisionTreeClassifier(random_state=42)

DT_model.fit(X_train, Y_train)

Y_pred_DT = DT_model.predict(X_test)

print("Accuracy :", accuracy_score(Y_test, Y_pred_DT))
print("Precision :", precision_score(Y_test, Y_pred_DT))
print("Recall :", recall_score(Y_test, Y_pred_DT))
print("f1 score :", f1_score(Y_test, Y_pred_DT))

print("Confusion Matrix :", confusion_matrix(Y_test, Y_pred_DT))

##########################################################
# Step 5 : Create Bagging Classifier
##########################################################
print(Border)
print("Step 5 : Create Bagging Classifier")
print(Border)

Bg_model = BaggingClassifier(
    estimator=DecisionTreeClassifier(random_state=42),
    n_estimators=50,
    random_state=42
) 

Bg_model.fit(X_train, Y_train)

Y_pred_Bg = Bg_model.predict(X_test)

print("Accuracy :", accuracy_score(Y_test, Y_pred_Bg))
print("Precision :", precision_score(Y_test, Y_pred_Bg))
print("Recall :", recall_score(Y_test, Y_pred_Bg))
print("f1 score :", f1_score(Y_test, Y_pred_Bg))

print("Confusion Matrix :", confusion_matrix(Y_test, Y_pred_Bg))

##########################################################
# Step 6 : Create Random Forest Classifier
##########################################################
print(Border)
print("Step 6 : Create Random Forest Classifier")
print(Border)

Rf_model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

Rf_model.fit(X_train, Y_train)

Y_pred_Rf = Rf_model.predict(X_test)

print("Accuracy :", accuracy_score(Y_test, Y_pred_Rf))
print("Precision :", precision_score(Y_test, Y_pred_Rf))
print("Recall :", recall_score(Y_test, Y_pred_Rf))
print("f1 score :", f1_score(Y_test, Y_pred_Rf))

print("Confusion Matrix :", confusion_matrix(Y_test, Y_pred_Rf))

##########################################################
# Step 7 : Create AdaBoost Classifier
##########################################################
print(Border)
print("Step 7 : Create AdaBoost Classifier")
print(Border)

AB_model = AdaBoostClassifier(
    n_estimators=50,
    random_state=42
)

AB_model.fit(X_train, Y_train)

Y_pred_AB = AB_model.predict(X_test)

print("Accuracy :", accuracy_score(Y_test, Y_pred_AB))
print("Precision :", precision_score(Y_test, Y_pred_AB))
print("Recall :", recall_score(Y_test, Y_pred_AB))
print("f1 score :", f1_score(Y_test, Y_pred_AB))

print("Confusion Matrix :", confusion_matrix(Y_test, Y_pred_AB))

##########################################################
# Step 8 : Create Voting Classifier
##########################################################
print(Border)
print("Step 8 : Create Voting Classifier")
print(Border)

LG_model = LogisticRegression(max_iter=1000)

DT1_model = DecisionTreeClassifier(random_state=42)

RF1_model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

VC_model = VotingClassifier(
    estimators=[
        ("LG_model", LG_model),
        ("DT_model", DT1_model),
        ("RF_model", RF1_model)
    ],
    voting="hard"
)

VC_model.fit(X_train, Y_train)

Y_pred_vc = VC_model.predict(X_test)

print("Accuracy :", accuracy_score(Y_test, Y_pred_vc))
print("Precision :", precision_score(Y_test, Y_pred_vc))
print("Recall :", recall_score(Y_test, Y_pred_vc))
print("f1 score:", f1_score(Y_test, Y_pred_vc))

print("Confusion Matrix :", confusion_matrix(Y_test, Y_pred_vc))

##########################################################
# Step 9 : Final Comparison
##########################################################
print(Border)
print("Step 9 : Final Comparison")
print(Border)

result = pd.DataFrame({
    "Algorithm" :[
        "Decision Tree",
        "Bagging",
        "Random Forest",
        "AdaBoost",
        "Voting"
    ],

    "Accuracy" :[
        accuracy_score(Y_test,Y_pred_DT),
        accuracy_score(Y_test,Y_pred_Bg),
        accuracy_score(Y_test,Y_pred_Rf),
        accuracy_score(Y_test,Y_pred_AB),
        accuracy_score(Y_test,Y_pred_vc)
    ],

    "Precision" :[
        precision_score(Y_test,Y_pred_DT),
        precision_score(Y_test,Y_pred_Bg),      
        precision_score(Y_test,Y_pred_Rf),
        precision_score(Y_test,Y_pred_AB),
        precision_score(Y_test,Y_pred_vc)
    ],

    "Recall" :[
        recall_score(Y_test,Y_pred_DT),
        recall_score(Y_test,Y_pred_Bg),
        recall_score(Y_test,Y_pred_Rf),
        recall_score(Y_test,Y_pred_AB),
        recall_score(Y_test,Y_pred_vc)
    ],

    "f1 score":[
        f1_score(Y_test,Y_pred_DT),
        f1_score(Y_test,Y_pred_Bg),
        f1_score(Y_test,Y_pred_Rf),
        f1_score(Y_test,Y_pred_AB),
        f1_score(Y_test,Y_pred_vc)
    ]
})

print(result)