""" 2: Write a Python program to demonstrate different activation functions.
Functions to implement:
1. Sigmoid
2. ReLU
3. Tanh
Tasks:
1. Accept input values from -10 to 10.
2. Plot all activation functions using Matplotlib.
3. Explain the use of each activation function.
"""

import numpy as np
import matplotlib.pyplot as plt

# Activation Function
def sigmoid(x):
    return 1/(1+np.exp(-x))

def relu(x):
    return np.maximum(0,x)

def tanh(x):
    return np.tanh(x)

# Accept input values from -10 to 10
values = np.linspace(-10, 10, 200)

# Calculate Outputs
sigmoid = sigmoid(values)
relu = relu(values)
tanh = tanh(values)

# plot all activation functions 
plt.figure(figsize=(10,6))

plt.plot(values, sigmoid, label="Sigmoid", color="blue", lw=2)
plt.plot(values, tanh, label="Tanh", color="orange", lw=2)
plt.plot(values, relu, label="Relu", color="green", lw=2)

plt.title("Comparision of Activation Function", fontsize=14)
plt.xlabel("Input Value (x)", fontsize=12)
plt.ylabel("Output Value", fontsize=12)
plt.axhline(0, color='black', linewidth=0.5, linestyle="--")
plt.axvline(0, color='black', linewidth=0.5, linestyle="--")
plt.grid(True, which='both', linestyle=':', alpha=0.6)
plt.legend(fontsize=12)
plt.ylim(-1.5, 5)       # Restricting ylim to show details without squishing shapes

plt.show()

"""
Explain the use of each activation function.
1. Sigmoid -> (0,1) -> Primarily used in the output layer of binary classification models 
                       to interpret outputs as final class probabilities.

2. Tanh -> (-1,1) -> Zero-centered function often used in hidden layers of shallow networks.
                     Negative inputs are mapped to strongly negative outputs, 
                     helping center training data distribution.

3. ReLU -> \([0, \infty)\) -> Default standard for hidden layers in Deep Neural Networks (DNNs/CNNs).
                        It avoids vanishing gradient issues for positive values and is computationally highly efficient.
"""