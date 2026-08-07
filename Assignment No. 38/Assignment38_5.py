""" 5. Based on the dataset values, analyze whether:
• Higher StudyHours increase the chance of passing.
• Higher Attendance improves FinalResult.
Write your observations in 4-5 lines.
"""

import pandas as pd

df = pd.read_csv("student_performance_ml.csv")

print(df.groupby("FinalResult")[["StudyHours", "Attendance"]].mean())

"""
Output ->       
              StudyHours  Attendance
FinalResult
0              2.550000   67.750000
1              6.372222   86.611111

Observation :
Students who study for more hours generally have a higher chance of passing.
Passed students studied an average of about 6.37 hours, while failed students studied only 2.55 hours.
Higher attendance is also associated with better results.
Passed students had an average attendance of about 86.61%, compared with 67.75% for failed students.
Therefore, both study hours and attendance show a strong positive relationship with FinalResult in this dataset.
"""
