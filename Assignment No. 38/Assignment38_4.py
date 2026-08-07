""" 4. Use value_counts() to analyze the distribution of FinalResult.
Calculate the percentage of Pass and Fail students.
Is the dataset balanced? Justify your answer.
"""

import pandas as pd

df = pd.read_csv("student_performance_ml.csv")

print(df["FinalResult"].value_counts())

percentage = df["FinalResult"].value_counts(normalize=True) * 100

print("\npercentage :")
print(percentage)

""" 
Answer : ->
Pass = 18 students = 60%
Fail = 12 students = 40%

Is the dataset balanced? 
-> The dataset is reasonably balanced but not perfectly balanced.
   There is a 60:40 distribution between Pass and Fail students, so there is no severe class imbalance.
"""