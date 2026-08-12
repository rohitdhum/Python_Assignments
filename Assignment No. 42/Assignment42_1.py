"""
1. Write a Python program that classifies a new data point using the K-Nearest Neighbors algorithm.
The algorithm should be implemented manually without using any machine learning library.
The program should:
• Calculate Euclidean distance
• Sort distances
• Select K nearest neighbors
• Predict the class based on majority voting

Dataset :->
Point X   Y   Label
A     1   2   Red
B     2   3   Red
C     3   1   Blue
D     6   5   Blue

Tasks :->
1. Accept X and Y coordinates of a new point from the user.
2. Compute Euclidean distance from all dataset points.
3. Sort the distances.
4. Select K = 3 nearest neighbors.
5. Predict the class label.

Input Format :->
Enter X coordinate: 2
Enter Y coordinate: 2

Expected Output :->
Nearest Neighbors:
A - Distance: 1.0
B - Distance: 1.0
C - Distance: 1.41
Predicted Class: Red
"""

import math

def CalculateEuclideanDistance(x1, y1, x2, y2):
    # Calculate standard Euclidean distance formula
    distance = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    return distance

def  PredictClass(K=3):
    # Create Dataset
    Data = [
        ("A",1,2,"Red"),
        ("B",2,3,"Red"),
        ("C",3,1,"Blue"),
        ("D",6,5,"Blue")
    ]

    # Accept the input
    X = float(input("Enter X coordinate :"))
    Y = float(input("Enter Y coordinate :"))

    Distances = []

    # Calculate distance to all points
    for point, px, py, label in Data:
        distance = CalculateEuclideanDistance(X,Y,px,py)
        Distances.append(
            (point, distance, label)
        )

    # Sort distances 
    Distances.sort(key = lambda item : item[1])

    # Select K nearest neighbors
    nearest = Distances[:K]

    print("\nNearest Neighbors :")

    for point, distance, label in nearest:
        print(f"{point} - Distance: {round(distance, 2)}")

    # Majority Voting    
    red_count = 0
    blue_count = 0

    for point, distance, label in nearest:
        if label == "Red":
            red_count = red_count + 1 
        else:
            blue_count = blue_count + 1

    if red_count > blue_count:
        result = "Red"
    else:
        result = "Blue"

    print("Predicted class :", result)

    return result

def main():
    PredictClass()

if __name__ == "__main__":
    main()