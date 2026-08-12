"""
3. Use KNN to predict whether a student passes or fails based on study hours and attendance.
Dataset :->
Study Hours   Attendance   Result
2               60          Fail
5               80          Pass
6               85          Pass
1               50          Fail

Tasks :->
1. Accept input from user:
◦ Study hours
◦ Attendance percentage
2. Apply KNN algorithm
3. Predict whether the student Passes or Fails
Input Example :->
Enter Study Hours: 4
Enter Attendance: 70
Expected Output
Predicted Result: Pass
"""

import math

def StudentResult():
    #Create Dataset
    Data = [
        (2, 60, "Fail"),
        (5, 80, "Pass"),
        (6, 85, "Pass"),
        (1, 50, "Fail")
    ]

    # Accept the input
    Study_Hours = float(input("Enter Study Hours :"))
    Attendance = float(input("Enter Attendance :"))

    # Calculate Eclidean distance
    Distances = []

    for hours, attend, result in Data:
        distance = math.sqrt((Study_Hours - hours)**2 + (Attendance - attend)**2)

        Distances.append(
            (distance, result)
        )

    # Sort Distance
    Distances.sort(key = lambda item : item[0])

    # Select K = 3  
    k = 3

    nearest = Distances[:k]

    print("\nNearest Neighbor :")

    for distance, result in nearest:
        print(f"Distance :{distance :2f} - {result}")

    # Majority Voting
    pass_count = 0
    fail_count = 0

    for distance, result in nearest:
        if result == "Pass":
            pass_count = pass_count + 1
        else:
            fail_count = fail_count + 1

    # Prediction
    if pass_count > fail_count:
        prediction = "Pass"
    else:
        prediction = "Fail"

    print("\nPredicted Result :", prediction)

def main():
    StudentResult()

if __name__ == "__main__":
    main()