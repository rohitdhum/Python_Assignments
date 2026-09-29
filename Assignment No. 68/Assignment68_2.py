# 2: Write a Python program to demonstrate ReLU and Max Pooling.

# Step 1 :- Create Input Feature Map
Feature_map = [
    [3,3,3],
    [0,0,0],
    [-3,-3,-3]
]

print("Input Featurte Map :")
for row in Feature_map:
    print(row)    

# Apply Relu Activation Function
Relu_Output = []

for row in Feature_map:
    new_row = []

    for value in row:
        if value < 0:
            new_row.append(0) 
        else:
            new_row.append(value)

    Relu_Output.append(new_row)

print("\nReLU Output:")
for row in Relu_Output:
    print(row)

# Step 3: Apply 2x2 Max Pooling
pool_size = 2
max_pooling_output = []

for i in range(0, len(Relu_Output) - pool_size + 1, pool_size):
    row = []

    for j in range(0, len(Relu_Output[0]) - pool_size + 1, pool_size):
        # Extract 2x2 Region
        region = [
            [Relu_Output[i + x][j + y] for y in range(pool_size)]
            for x in range(pool_size)
        ]

        print("\n2x2 Pooling Region:")
        for r in region:
            print(r)

        # Find Maximum Value
        maximum = max(max(r) for r in region)

        print("Maximum Value =", maximum)

        row.append(maximum)

    max_pooling_output.append(row)

print("\nMax Pooling Output:")
for row in max_pooling_output:
    print(row)