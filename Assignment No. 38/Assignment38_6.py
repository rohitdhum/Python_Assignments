""" 6. Plot a histogram of StudyHours.
Explain what the distribution tells you.
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("student_performance_ml.csv")

plt.hist(df["StudyHours"], bins=8, edgecolor="black")

plt.xlabel("Study Hours")

plt.ylabel("Number of students")

plt.title("Distribution of study hours")

plt.show()

""" 
The histogram shows that students' study hours range from approximately 1 to 8.5 hours per day.
Most students are concentrated around the 2-8 hour range.
The dataset contains both low-study-hour and high-study-hour students.
From the data, higher study hours are generally associated with passing.
"""