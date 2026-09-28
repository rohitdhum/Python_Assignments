# 2 : Create a neural network model to predict loan approval.

import numpy as np 
import tensorflow as tf

from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input

# Step 1 :- Create Dataset
X = np.array([
    [25000, 600, 200000, 10000, 0],
    [40000, 700, 300000, 8000, 1],
    [60000, 750, 500000, 12000, 1],
    [20000, 550, 150000, 15000, 0],
    [80000, 800, 700000, 10000, 1],
    [35000, 650, 250000, 9000, 1],
    [18000, 500, 100000, 12000, 0],
    [90000, 850, 800000, 15000, 1],
    [30000, 580, 200000, 14000, 0],
    [70000, 780, 600000, 10000, 1]    
],dtype=float)

Y = np.array([
    0, 1, 1, 0, 1,
    1, 0, 1, 0, 1
],dtype=float)

# Step 2 :- Preprocess categorical values.
# Employment Status:
# 0 = Not Stable
# 1 = Stable
print("Missing Values :", np.isnan(X).sum())

# Remove Duplicate Rows
X_unique, Indices = np.unique(X, axis=0, return_index=True)
Y_unique = Y[Indices]

X = X_unique
Y = Y_unique

print("Input Dataset Shape:", X.shape)
print("Target Shape :", Y.shape)

# Step 3 :- Apply Standard Scalar
scalar = StandardScaler()
X_scaled = scalar.fit_transform(X)

# Create And Train The FNN Model
tf.random.set_seed(42)
np.random.seed(42)

model = Sequential([
    Input(shape=(5,)),
    Dense(16, activation="relu"),
    Dense(8, activation="relu"),
    Dense(1, activation="sigmoid")
])

model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)

model.fit(
    X_scaled,
    Y,
    epochs=300,
    batch_size=2,
    verbose=0
)

# Step 5 :- Model Evaluation
loss, accuracy = model.evaluate(
    X_scaled, Y, verbose=0
)

print("Model Evaluation")
print("Loss :", round(loss, 4))
print("Accuracy :", round(accuracy * 100, 2), "%")

# Calculate Prediction on Dataset
Probabilities = model.predict(X_scaled, verbose=0)
Predictions = (Probabilities >= 0.5).astype(int).flatten()

print("Training Accuracy :", round(accuracy_score(Y, Predictions)*100, 2), "%")

# Step 6 :- Predict for new application
New_Applicant = np.array([
    [55000, 720, 400000, 10000, 1]
])

New_Applicant_Scalaed = scalar.fit_transform(New_Applicant)

Prediction = model.predict(New_Applicant_Scalaed, verbose=0)[0][0]

print("Prediction : Loan Approval")

if Prediction >= 0.5:
    print("Prediction : Loan Approved")
else:
    print("Prediction : Loan Rejected")