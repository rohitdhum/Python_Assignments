""" Q2: Use the DataFrame from Q1 and print descriptive statistics using .describe().
"""

import pandas as pd

def main():
    data = {
        'Name' : ['Amit', 'Sagar', 'Pooja'],
        'Math' : [85, 90, 78],
        'Science' : [92, 88, 80],
        'English' : [75, 85, 82]
        }

    # Create Dataframe
    df = pd.DataFrame(data)

    print("\nDataFrame Shape :", df.shape)

    print("\nDataFrame Columns :", df.columns.to_list())

    print("\nData Types :", df.dtypes)

    # Q2. Print Descriptive Statistics
    print("\n",df.describe())

if __name__ == "__main__":
    main()