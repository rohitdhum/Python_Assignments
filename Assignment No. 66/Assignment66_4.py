""" 4: Write a Python program to show how weights are updated in ANN.
Tasks:
1. Take input, weight, bias, target output, and learning rate.
2. Calculate prediction.
3. Calculate error.
4. Update weight using gradient descent logic.
5. Display old weight and updated weight.
"""

X = 2.0               # Input
W_old = 0.8           # Old Weight
Bias = 0.3            # Bias
Target = 1.0          # Output
Learning_rate = 0.1   # Optimization step scale

# Task 2: Calculate prediction
Z = (X * W_old) + Bias
prediction = Z 

# Calculate Error
Error = prediction - Target

# Updated Weight using gradient descent logic
gradient_W = Error * X
W_new = W_old - (Learning_rate * gradient_W) 

# Display old weight and updated weight.
print("Initaial Prediction", prediction)
print("Calculated Error", Error)
print("Old Weight", W_old)
print("Updated Weight", W_new)