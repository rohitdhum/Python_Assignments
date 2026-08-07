""" 10. Plot SleepHours against FinalResult.
Does sleeping more guarantee success? Explain.
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("student_performance_ml.csv")

plt.scatter(df["SleepHours"],
            df["FinalResult"])

plt.xlabel("Sleep Hours")

plt.ylabel("Final Result")

plt.title("Sleep Hours Vs Final Result")

plt.yticks([0,1], ["Fail", "Pass"])

plt.show()

"""
Explaination :
More sleep is associated with better results in this dataset, but sleeping more alone doesn't guarantee success.
A student needs a combination of good study habits, attendance, previous performance, assignment completion, 
and adequate sleep.
"""