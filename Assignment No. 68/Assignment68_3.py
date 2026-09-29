# 3: Write a Python program to show flattening.

# Step 1: Create a 2D Matrix
matrix = [
    [6, 4],
    [8, 6]
]

print("Input Matrix:")
for row in matrix:
    print(row)


# Step 2: Convert 2D Matrix into 1D Vector
flatten_output = []

for row in matrix:
    for value in row:
        flatten_output.append(value)

print("\nFlatten Output:")
print(flatten_output)


# Step 3: Define Fully Connected Layer Weights and Bias
weights = [0.5, 0.2, 0.3, 0.4]
bias = 1

# Step 4: Calculate Final Output Manually
output = 0

for i in range(len(flatten_output)):
    output += flatten_output[i] * weights[i]

output += bias

print("\nWeights:", weights)
print("Bias:", bias)

print("\nCalculation:")
print("(6 * 0.5) + (4 * 0.2) + (8 * 0.3) + (6 * 0.4) + 1")

print("Final Output =", output)