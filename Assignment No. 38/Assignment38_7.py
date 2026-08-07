"""
7. Create a scatter plot of:
StudyHours vs PreviousScore
Use different colors for Pass and Fail students.
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("student_performance_ml.csv")

Passed = df[df["FinalResult"] == 1]

Failed = df[df["FinalResult"] == 0]

plt.scatter(Failed["StudyHours"],
            Failed["PreviousScore"],
            label = "Fail")

plt.scatter(Passed["StudyHours"],
            Passed["PreviousScore"],
            label = "Pass")

plt.xlabel("Study Hours")

plt.ylabel("Previous Score")

plt.title("Study Hours Vs Previous Score")

plt.legend()

plt.show()
