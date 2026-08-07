""" 8. Draw a boxplot for Attendance.
Identify if any outliers are present.
"""
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("student_performance_ml.csv")

plt.boxplot(df["Attendance"], patch_artist=True)

plt.ylabel("Attendance (%)")

plt.title("Boxplot for Attendance")

plt.show()