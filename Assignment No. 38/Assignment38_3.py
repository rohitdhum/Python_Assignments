""" 3. Using pandas functions, calculate and display:
• Average StudyHours
• Average Attendance
• Maximum PreviousScore
• Minimum SleepHours
"""

import pandas as pd

df = pd.read_csv("student_performance_ml.csv")

# Average StudyHours
print("Average StudyHours :", df["StudyHours"].mean())

# Average Attendance
print("Average Attendance :", df["Attendance"].mean())

# Maximum PreviousScore
print("Maximum PreviousScore :", df["PreviousScore"].max())

# Minimum SleepHours
print("Minimum SleepHours :", df["SleepHours"].min())
