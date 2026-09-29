# 1: Write a Python program to manually perform convolution.

# Step 1 :- Input Image Matrix
Image = [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [1,1,1,1,1],
    [0,0,0,0,0],
    [0,0,0,0,0]
]

# Step 2 :- Karnel Matrix (3D)
Kernel = [
    [-1,-1,-1],
    [1,1,1],
    [0,0,0]
]

# Step 3 :- Initialize Feature Map
Feature_Map = []

# Move Kernel Over the Image
for i in range (len(Image) - len(Kernel) + 1):
    Row = []

    for j in range(len(Image[0]) - len(Kernel[0]) + 1):
        # Extract 3x3 region
        Region = [
            [Image[i + x][j + y] for y in range(3)]
            for x in range(3)
        ]

        print("Region :")
        for R in Region:
            print(R)

        print("Kernel :")
        for K in Kernel:
            print(K)

        # Step 5 :- Multiplcation And Activation
        Total = 0

        print("Calculations :")

        for x in range(3):
            for y in range(3):

                Value = Region[x][y] * Kernel[x][y]

                Total += Value

                print(f"{Region[x][y]} * {Kernel[x][y]}", 
                      end="+" if not (x == 2 and y == 2) else "\n"
                    )

            print("Output :", Total)

            # Store Result in Feature Map
            Row.append(Total)

        Feature_Map.append(Row)

    print("Expected Feature Map :")

    for Row in Feature_Map:
        print(Row)