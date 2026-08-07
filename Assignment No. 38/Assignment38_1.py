""" 1. Write a Python program to load the file student_performance_ml.csv using pandas.
Display:
• First 5 records
• Last 5 records
• Total number of rows and columns
• List of column names
• Data types of each column
"""

import pandas as pd

df = pd.read_csv("student_performance_ml.csv")

# First 5 records
print("\nFirst five records :")
print(df.head())

# Last 5 records
print("\nLast five records :")
print(df.tail())

# Total number of rows and columns
print("\nTotal number of rows and columns :")
print(df.shape)

# List of column names
print("\nList of column names")
print(df.columns.tolist())

# Data types of each column
print("\nData types of each column :")
print(df.dtypes)