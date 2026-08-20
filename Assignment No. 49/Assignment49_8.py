""" 8. Write a Python program that calculates TP, TN, FP, FN for the following arrays:
actual = [1,1,1,1,0,0,0,0]
predicted = [1,1,0,1,0,1,0,0]
Display all four values.
"""

def ConfusionMatrics(Actual, Predicted):
    # Initialize counts to zero
    TP = TN = FP = FN = 0

    for act, pred in zip(Actual, Predicted):
        if act == 1 and pred == 1:
            TP += 1
        elif act == 0 and pred == 0:
            TN += 1
        elif act == 1 and pred == 0:
            FN += 1
        elif act == 0 and pred == 1:
            FP += 1

    return TP, TN, FP, FN

def main():
    Actual = [1,1,1,1,0,0,0,0]
    Predicted = [1,1,0,1,0,1,0,0]

    TP, TN, FP, FN = ConfusionMatrics(Actual, Predicted)

    print("--- Confusion Matrix Breakdown ---")
    print(f"True Positives (TP)  : {TP}")
    print(f"True Negatives (TN)  : {TN}")
    print(f"False Positives (FP) : {FP}")
    print(f"False Negatives (FN) : {FN}")

if __name__ == "__main__":
    main()
