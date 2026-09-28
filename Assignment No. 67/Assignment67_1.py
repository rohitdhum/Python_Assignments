# 1 : Create a neural network model to predict whether a customer will leave a service.

import numpy as np
import tensorflow as tf

from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input

# Step 1 :- Create Dataset
X = np.array([
    [25, 500, 12, 1, 2],
    [30, 700, 24, 0, 1],
    [45, 1200, 6, 5, 8],
    [50, 1500, 5, 6, 10],
    [28, 600, 18, 1, 1],
    [35, 800, 30, 0, 0],
    [48, 1400, 4, 7, 9],
    [52, 1600, 3, 8, 12],
    [27, 550, 20, 0, 1],
    [42, 1300, 8, 4, 7]
], dtype=float)

Y = np.array([
    0, 0, 1, 1, 0,
    0, 1, 1, 0, 1
], dtype=float)

# Step 2 :- Clean The Dataset
print("Missing Values :", np.isnan(X).sum())

# Remove Dublicate rows 
X_unique, Indices = np.unique(X, axis=0, return_index=True)

Y_unique = Y[Indices]

X = X_unique
Y = Y_unique

print("Inp[ut Data Shape :", X.shape)
print("Target Data :", Y.shape)

# Step 3 :- Apply StandardScalar
scalar = StandardScaler()
X_scaled = scalar.fit_transform(X)

# Step 4 :- Create and Train FNN Model
tf.random.set_seed(42)
np.random.seed(42)

model = Sequential([
    Input(shape=(5,)),
    Dense(16, activation='relu'),
    Dense(8, activation='relu'),
    Dense(1, activation='sigmoid')
])

model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

model.fit(X_scaled, 
          Y, 
          epochs=300,
          batch_size=2,
          verbose=0
)

# Step 5 :- Evaluate Model
loss, accuracy = model.evaluate (X_scaled, Y, verbose=0)

print("Model Evaluation")
print("Loss", round(loss,4))
print("Accuracy :", round(accuracy * 100, 2), "%")

# Calculate predictions on Dataset
Probabilities = model.predict(X_scaled, verbose=0)

Predictions = (Probabilities >= 0.5).astype(int).flatten()

print("Training Accuracy :", 
      round(accuracy_score(Y, Predictions) * 100, 2), "%")

# Predict for new customer
New_Customer = np.array([[46, 1450, 5, 6, 9]])

New_Customer_Scaled = scalar.transform(New_Customer)

Prediction = model.predict(
    New_Customer_Scaled, verbose=0
)[0][0]

print("New Customer Prediction")

if Prediction >= 0.5:
    print("Prediction : Customer may leave")

else:
    print("Prediction : Customer will leave")

print("Probability of leaving", 
      round(float(Prediction) * 100, 2), "%")