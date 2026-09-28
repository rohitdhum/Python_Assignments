""" 1: Write a Python program to simulate a single artificial neuron.
Input:
x1 = 2
x2 = 3
w1 = 0.4
w2 = 0.6
bias = 0.5

Tasks:
1. Calculate weighted sum.
2. Apply sigmoid activation function.
3. Display final output.
4. Explain whether output is close to 0 or 1.
"""

import numpy as np

# Inputs
x1, x2 = 2, 3
w1, w2 = 0.4, 0.6
bias = 0.5

# weighted sum  (z = (x1*w1) + (x2*w2) + bias)
weighted_sum = (x1*w1) + (x2*w2) + bias

# sigmoid activation function (1/(1 + e^-z))
def sigmoid(z):
    return 1/(1+np.exp(-z))

final_output = sigmoid(weighted_sum)

# Display the Outputs
print(f"Weigjted Sum :{weighted_sum}")
print(f"Final Output :{final_output:.4f}")

"""
Explanation of Output Value :
Analysis: The weighted sum \[z\] calculates to \((2 \times 0.4) + (3 \times 0.6) + 0.5 = 3.1\).
Conclusion: The final output is approximately 0.9568, which is close to 1.
Reasoning: The Sigmoid function compresses any input into a range between 0 and 1.
           Positive values greater than 0 shift the output toward 1.
           Since \[3.1\] is significantly larger than 0, the neuron yields a strong probability 
           indicating a positive or highly activated state.
"""