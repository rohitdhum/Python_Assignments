""" 3: Write a Python program to calculate loss manually.
Tasks:
1. Implement Mean Squared Error.
2. Implement Binary Cross Entropy.
3. Take actual and predicted values.
4. Display the calculated loss.
5. Explain which loss function is used for regression and classification.
"""

import numpy as np

# Mean Squared Error
def MeanSquaredError(actual, predicted):
    return np.mean((actual-predicted)**2)

# Binary Cross Entropy
def BinaryCrossEntropy(actual, predicted):
    predicted = np.clip(predicted, 1e-15, 1 - 1e-15)
    return -np.mean(actual * np.log(predicted) + (1- actual) * np.log(1-predicted))

# Take Actual and Cross Entropy
actual_reg = np.array([2.5, 5.0, 4.2])
pred_reg = np.array([2.3,5.5,4.0])

actual_clf = np.array([1,0,1])
pred_clf = np.array([0.9,0.1,0.2])

# Calculated Loss
MSE_Loss = MeanSquaredError(actual_reg, pred_reg)
BCE_Loss = BinaryCrossEntropy(actual_clf, pred_clf)

print(f"Calculated Mean Squared Error (MSE) : {MSE_Loss:.4}")
print(f"Calculated Binary Cross Entropy (BCE) :{BCE_Loss:.4f}")
