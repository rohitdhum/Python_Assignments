################################################################
# Loan Default Prediction using Multi-Layer Perceptron
################################################################

# Tasks :
# 1. Load and understand the dataset.
# 2. Perform exploratory analysis.
# 3. Find missing values.
# 4. Check whether the target classes are balanced.
# 5. Encode categorical variables.
# 6. Separate X and y.
# 7. Split the dataset into training and testing data.
# 8. Explain whether stratified splitting should be used.
# 9. Scale the features.
# 10. Create an MLPClassifier.
"""
Start with:
MLPClassifier(
   hidden_layer_sizes=(32, 16),
   activation='relu',
   solver='adam',
   max_iter=1000,
   random_state=42
)
"""
# 11. Train the model.
# 12. Calculate accuracy.
# 13. Generate the confusion matrix.
# 14. Generate the classification report.
# 15. Calculate precision, recall and F1-score.
# 16. Plot training loss.
# 17. Test the model on new loan applicants.
################################################################
# Hyperparameter Experiment
# Change one parameter at a time.

# Experiment 1 — Activation
# identity
# logistic
# tanh
# relu

# Experiment 2 — Hidden Layers
# (10,)
# (20,10)
# (50,25)
# (100,50,25)

# Experiment 3 — Learning Rate
# Try different values for learning_rate_init.
################################################################

################################################################
# Import Required Liabraries
################################################################
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, precision_score, recall_score, f1_score

################################################################
# 1. Load the dataset
################################################################

Border = "-" * 60
print(Border)
print("1. Load the dataset")
print(Border)

data = pd.read_csv("Loan_Default.csv")

print("Complete Dataset :")
print(data)

print("Dataset Information :")
print(Border)
data.info()

print("Statistical Summary :")
print(Border)
print(data.describe())

################################################################
# 2. Exploratory Data Analysis (EDA)
################################################################

Border = "-" * 60
print(Border)
print("2. Exploratory Data Analysis")
print(Border)

print("Previous Default :")
print(data['PreviousDefault'].value_counts())

print("Home Ownership :")
print(data["HomeOwnership"].value_counts())

################################################################
# 3. Missing values.
################################################################

Border = "-" * 60
print(Border)
print("3. Missing values.")
print(Border)

print("Missing Values are :")
print(data.isnull().sum())

################################################################
# 4. Target class Balanced.
################################################################

Border = "-" * 60
print(Border)
print("4. Target class Balanced.")
print(Border)

print("Target Distribustion :")
print(data['Default'].value_counts())

print("Target Percentage :")
print(data['Default'].value_counts(normalize=True)*100)

plt.figure(figsize=(6,4))

data['Default'].value_counts().plot(kind='bar')

plt.title("Default Class Distribution")
plt.xlabel("Default")
plt.ylabel("Count")
plt.xticks(rotation = 0)
plt.show()

################################################################
# 5. Encode categorical variables.
################################################################

Border = "-" * 60
print(Border)
print("5. Encode categorical variables.")
print(Border)

data['PreviousDefault'] = data['PreviousDefault'].map({
    "Yes" : 1,
    "No" : 0
})

data = pd.get_dummies(
    data,
    columns=['HomeOwnership'],
    dtype=int
)

print("Dataset After Encoding :", data.head())

################################################################
# 6. Separate Features.
################################################################

Border = "-" * 60
print(Border)
print("6. Separate Features.")
print(Border)

X = data.drop("Default", axis=1)
Y = data["Default"]

print("X Shape :",X.shape)
print("Y Shape", Y.shape)

################################################################
# 7. Split the dataset into training and testing data.
################################################################

Border = "-" * 60
print(Border)
print("7. Split the dataset into training and testing data.")
print(Border)

X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.2, random_state=42, stratify=Y)

print("Training Input Shape :", X_train.shape)
print("Testing Input Shape :", X_test.shape)
print("Training Output Shape :", Y_train.shape)
print("Testing Output Shape :", Y_test.shape)

################################################################
# 8. Explain whether stratified splitting should be used.
################################################################

Border = "-" * 60
print(Border)
print("8. Explain whether stratified splitting should be used.")
print(Border)

print("""
Yes, stratified splitting should be used.

The target variable 'Default' contains two classes:
0 -> Low default risk
1 -> High default risk

The classes are not equally distributed in the dataset.
Therefore, stratified splitting is used to maintain approximately
the same proportion of both classes in the training and testing
datasets.

We use stratify=y in train_test_split().
""")

################################################################
# 9. Scale the features.
################################################################

Border = "-" * 60
print(Border)
print("9. Scale the features.")
print(Border)

scalar = StandardScaler()

X_train_scaled = scalar.fit_transform(X_train)
X_test_scaled = scalar.fit_transform(X_test)

print("Scaled Training Data :")
print(X_test_scaled[:10])

################################################################
# 10. Create an MLPClassifier.
################################################################

Border = "-" * 60
print(Border)
print("10. Create an MLPClassifier.")
print(Border)

model = MLPClassifier(
   hidden_layer_sizes=(32,16),
   activation="relu",
   solver='adam',
   max_iter=1000,
   random_state=42
)

print(model)

################################################################
# 11. Train the model.
################################################################

Border = "-" * 60
print(Border)
print("11. Train the model.")
print(Border)

model.fit(X_train_scaled, Y_train)

print("Model training completed")

################################################################
# 12. Calculate accuracy.
################################################################

Border = "-" * 60
print(Border)
print("12. Calculate accuracy.")
print(Border)

# Prediction
Y_pred = model.predict(X_test_scaled)

Accuracy = accuracy_score(Y_test, Y_pred)
print(f"Accuracy is : {Accuracy*100:.2f}%")

################################################################
# 13. Confusion Matrix.
################################################################

Border = "-" * 60
print(Border)
print("13. Confusion Matrix.")
print(Border)

cm = confusion_matrix(Y_test, Y_pred)
print(cm)

################################################################
# 14. Classification Report.
################################################################

Border = "-" * 60
print(Border)
print("14. Classification Report.")
print(Border)

Classification_Report = classification_report(Y_test, Y_pred)
print(Classification_Report)

################################################################
# 15. Calculate precision, recall and F1-score.
################################################################

Border = "-" * 60
print(Border)
print("15. Calculate precision, recall and F1-score.")
print(Border)

Precision = precision_score(Y_test, Y_pred)
print(f"Presion Score : {Precision * 100:.2f}%")

Recall = recall_score(Y_test, Y_pred)
print(f"Recall Score : {Recall * 100:.2f}%")

F1 = f1_score(Y_test, Y_pred)
print(f"F1 Score : {F1 * 100:.2f}%")

################################################################
# 16. Plot training loss.
################################################################

Border = "-" * 60
print(Border)
print("16. Plot training loss.")
print(Border)

Loss_Curve = model.loss_curve_

print("Training Loss values :")
print(Loss_Curve)

plt.figure(figsize=(8,5))

plt.plot(range(1, len(Loss_Curve) + 1), Loss_Curve)

plt.title("Training loss curve")
plt.xlabel("Iterations")
plt.ylabel("Loss")
plt.grid(True)
plt.show()

################################################################
# 17. Test the model on new loan applicants.
################################################################

Border = "-" * 60
print(Border)
print("17. Test the model on new loan applicants.")
print(Border)

New_Application = pd.DataFrame({
    "Age": [30],
    "Income": [60000],
    "LoanAmount": [20000],
    "CreditScore": [720],
    "PreviousDefault": [0],
    "HomeOwnership_Own": [1],
    "HomeOwnership_Rent": [0],
    "HomeOwnership_Mortgage": [0],
    "EmploymentYears": [5],
    "ExistingLoans": [1],
    "LoanTerm": [60],
    "MonthlyDebt": [10000]
})

New_Application = New_Application[X.columns]

print("Fetures used for training :")
print(X.columns.tolist())

New_Application_scaled = scalar.transform(New_Application)

New_pred = model.predict(New_Application_scaled) 

New_probability = model.predict_proba(New_Application_scaled)

print("New Application Data :")
print(New_Application)

print("Prediction Probability :", New_probability)

if New_pred[0] == 0:
    print("Prediction : Loan Will Not Default")
else:
    print("Prediction : Loan May Default")

################################################################
# Experiment 1 — Activation
################################################################

Border = "-" * 60
print(Border)
print("Experiment 1 — Activation")
print(Border)

Activations = [
    "identity",
    "logistic",
    "tanh",
    "relu"
]

Activation_Results = []

for Activation in Activations:
    print("Testing Activation",Activation)

    Experiment_model1 = MLPClassifier(
        hidden_layer_sizes=(32,16),
        activation=Activation,
        solver='adam',
        max_iter=1000,
        random_state=42
    )

    Experiment_model1.fit(X_train_scaled,Y_train)

    prediction = Experiment_model1.predict(X_test_scaled)

    Accuracy = accuracy_score(Y_test, prediction)

    Activation_Results.append({
        "Activation" : Activation,
        "Accuracy" : (f"{Accuracy * 100:.2f}%")
    })

    print(f"Accuracy : {Accuracy*100:.2f}%")

################################################################
# Convert result into DataFrame
################################################################

    Activation_Results_df = pd.DataFrame(Activation_Results)

    print("Activation Experiment Result :")
    print(Activation_Results_df)

################################################################
# Experiment 2 — Hidden Layers
################################################################

Border = "-" * 60
print(Border)
print("Experiment 2 — Hidden Layers")
print(Border)

Hidden_Layers = [
    (10,),
    (20,10),
    (50,25),
    (100,50,25)
]

Hidden_Results = []

for layers in Hidden_Layers:
    print("Testing Hidden Layer :", layers)

    Experiment_model2 = MLPClassifier(
        hidden_layer_sizes=layers,
        activation='relu',
        solver='adam',
        max_iter=1000,
        random_state=42
    )

    Experiment_model2.fit(X_train_scaled, Y_train)

    prediction = Experiment_model2.predict(X_test_scaled)

    Accuracy = accuracy_score(Y_test, prediction)

    Hidden_Results.append({
        "Hidden Layer" : str(layers),
        "Accuracy" : (f"{Accuracy * 100:.2f}%")
    })

    print(f"Accuracy : {Accuracy * 100:2f}%")

    Hidden_Results_df = pd.DataFrame(Hidden_Results)

    print("Hidden Layer Experiment Result :")
    print(Hidden_Results_df)

################################################################
# Experiment 3 — Learning Rate
################################################################

Border = "-" * 60
print(Border)
print("Experiment 3 — Learning Rate")
print(Border)

Learning_Rates = [
    0.0001,
    0.001,
    0.01,
    0.1
]

Learning_Rate_Results = []

for Learning_Rate in Learning_Rates:
    print("Testing Learning Rate :",Learning_Rate)

    Experiment_model3 = MLPClassifier(
        hidden_layer_sizes=(32,16),
        activation='relu',
        solver='adam',
        max_iter=1000,
        random_state=42
    )

    Experiment_model3.fit(X_train_scaled, Y_train)

    prediction = Experiment_model3.predict(X_test_scaled)

    Accuracy = accuracy_score(Y_test, prediction)

    Learning_Rate_Results.append({
        "Learning Rate" : Learning_Rate,
        "Accuracy" : (f"{Accuracy*100:.2f}%")
    })

    print(f"Accuracy : {Accuracy*100:.2f}%")

    Learning_Rate_Results_df = pd.DataFrame(Learning_Rate_Results)

    print(Learning_Rate_Results_df)

################################################################
# Final Comparison
################################################################

Border = "-" * 60
print(Border)
print("FINAL HYPERPARAMETER EXPERIMENT RESULTS")
print(Border)

print("Experiment 1 - Actication :")
print(Activation_Results_df)

print("Experiment 2 -  Hidden Layer :")
print(Activation_Results_df)

print("Experiment 3 - Learning Rate :")
print(Activation_Results_df)

################################################################
# Find the Best Activation, Hidden Layer, Learning Rate
################################################################

Border = "-" * 60
print(Border)
print("Find the Best Activation, Hidden Layer, Learning Rate")
print(Border)

Best_Activation = Activation_Results_df.loc[Activation_Results_df["Accuracy"].idxmax()]

Best_Hidden_Layer = Hidden_Results_df.loc[Hidden_Results_df["Accuracy"].idxmax()]

Best_Learning_Rate = Learning_Rate_Results_df.loc[Learning_Rate_Results_df["Accuracy"].idxmax()]

print("Best Activation :")
print(Best_Activation)
print(Border)

print("Best Hidden Layer :")
print(Best_Hidden_Layer)
print(Border)

print("Best Learning Rate :")
print(Best_Learning_Rate)
print(Border)

#####################################################################
# End Of Program
#####################################################################

Border = "-" * 60
print(Border)
print("-----------------------End Of Program-----------------------")
print(Border)