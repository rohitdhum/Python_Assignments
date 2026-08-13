""" Q3: Add a new column 'Total' to the DataFrame as the sum of all subject marks.
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

    # Print Descriptive Statistics
    print("\n",df.describe())

    # Q3. Calculate and add "Total" column to the Dataframe
    df['Total'] = df['Math'] + df['Science'] + df['English']

    print("\n", df)   

if __name__ == "__main__":
    main()