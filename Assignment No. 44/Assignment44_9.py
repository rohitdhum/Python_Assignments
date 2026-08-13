""" Q9: Create a DataFrame with missing values and fill them with column mean.
data2 = {
'Name': ['Amit', 'Sagar', 'Pooja'],
'Math': [np.nan, 76, 88],
'Science': [91, np.nan, 85]
}
"""

import numpy as np
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

    # Calculate and add "Total" column to the Dataframe
    df['Total'] = df['Math'] + df['Science'] + df['English']

    print("\n", df)   

    # Display Student Scoring more than 85 in Science
    Science_Score = df[df['Science'] > 85]

    print("\nAbove 85 Marks obtained Students in science :","\n",Science_Score)

    # Replace 'Pooja' with 'Puja'
    df['Name'] = df['Name'].replace('Pooja', 'Puja')

    print("\nReplace Pooja Name with Puja :", "\n", df)

    # Sort by 'Total' marks in descending order
    df_Sorted = df.sort_values(by = 'Total', ascending = False)

    print("\nSort by 'Total' marks in descending order :\n", df_Sorted)

    # Q9. Create a DataFrame with missing values
    data2 = {
        'Name' : ['Amit', 'Sagar', 'Pooja'],
        'Math' : [np.nan, 76, 88],
        'Science' : [91, np.nan, 85]
        }

    # Create DataFrame
    df2 = pd.DataFrame(data2)

    # Fill missing values with column mean
    df2['Math'] = df2['Math'].fillna(df2['Math'].mean())
    df2['Science'] = df2['Science'].fillna(df2['Science'].mean())

    print("\nFilled Missing Values with Mean\n", df2)
if __name__ == "__main__":
    main()