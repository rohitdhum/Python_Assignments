""" 2. Write a program to:
• Display total number of students in the dataset
• Count how many students Passed (FinalResult = 1)
• Count how many students Failed (FinalResult = 0)
"""

import pandas as pd

df = pd.read_csv("student_performance_ml.csv")

# Display total number of students in the dataset
print("Total number of students :")
print(len(df))

# Count how many students Passed (FinalResult = 1)
print("Count how many students Passed :")
print((df["FinalResult"] == 1).sum())

# Count how many students Failed (FinalResult = 0)
print("Count how many students Failed :")
print((df["FinalResult"] == 0).sum())