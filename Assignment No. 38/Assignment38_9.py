""" 9. Create a plot showing relationship between AssignmentsCompleted and FinalResult.
Explain your observation.
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("student_performance_ml.csv")

plt.scatter(df["AssignmentsCompleted"],
            df["FinalResult"],)

plt.xlabel("Assignment Completed")

plt.ylabel("Final Result")

plt.title("Assignment Completed Vs Final Result")

plt.yticks([0,1], ["Fail", "Pass"])

plt.show()

"""
Observation :
Students who complete more assignments are much more likely to pass the course.
On the other hand, students who complete fewer assignments are more likely to fail.
This shows that doing homework has a strong, positive connection to passing.
"""