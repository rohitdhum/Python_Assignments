"""
2. The value of K plays an important role in the KNN algorithm.
Write a Python program that demonstrates how prediction changes when K changes.
Dataset
Use the same dataset as Assignment 1.
Tasks :->
Predict the class of the same new point using:
• K = 1
• K = 3
• K = 5

Expected Output :->
Prediction Results
K = 1 → Red
K = 3 → Red
K = 5 → Blue
Explain why the prediction changes when K increases.
"""

import math

def  PredictClass():
    # Create Dataset
    Data = [
        ("A",1,2,"Red"),
        ("B",2,3,"Red"),
        ("C",3,1,"Blue"),
        ("D",6,5,"Blue")
    ]

    # Accept the input
    x = float(input("Enter X coordinate :"))
    y = float(input("Enter Y coordinate :"))

    Distances = []

    # Calculate distance to all points
    for point, px, py, label in Data:
        # Calculate standard Euclidean distance formula
        distance =math.sqrt((x-px)**2 + (y-py)**2)

        Distances.append(
            (point, distance, label)
        )

    # Sort Distances
    Distances.sort(key = lambda item : item[1])

    print("\nPrediction Results")
    #############################################
    # K = 1
    #############################################

    k = 1

    nearest = Distances[:k]

    red_count = 0
    blue_count = 0

    for point, distance, label in nearest:
        if label == "Red":
            red_count = red_count + 1
        else:
            blue_count = blue_count + 1

    result = "Red" if red_count > blue_count else "Blue"
    print("k = 1 ->",result)

    #############################################
    # K = 3
    #############################################

    k = 3

    nearest = Distances[:k]

    red_count = 0
    blue_count = 0

    for point, distance, label in nearest:
        if label == "Red":
            red_count = red_count + 1
        else:
            blue_count = blue_count + 1

    result = "Red" if red_count > blue_count else "Blue"
    print("k = 3 ->", result)

    #############################################
    # K = 5
    #############################################

    k = 5

    nearest = Distances[:k]

    red_count = 0
    blue_count = 0

    for point, distance, label in nearest:
        if label == "Red":
            red_count = red_count + 1
        else:
            blue_count = blue_count + 1

    result = "Red" if red_count > blue_count else "Blue"
    print("k = 5 ->", result)

def main():
    PredictClass()

if __name__ == "__main__":
    main()

"""
    Explain why the prediction changes when K increases ?
 -> 1. Small K (K=1, K=3): The model captures highly localized data structures.
    The point (2,2) is physically closest to the 'Red' cluster (Points A and B),
    meaning the closest neighborhood has a strict Red majority.
    2. Large K (K=5): As K scales up, the boundaries become smooth and look at a
    broader window. Because there are only 4 points, K=5 captures the entire
    dataset. Since there is a tie (2 Red, 2 Blue), the fallback logic selects
    'Blue', proving that a high K makes the model less sensitive to the immediate
    closest points and more dependent on the overall background balance.
"""