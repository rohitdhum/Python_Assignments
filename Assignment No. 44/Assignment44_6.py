""" Q6: Sort the DataFrame by 'Total' marks in descending order.
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

    # Calculate and add "Total" column to the Dataframe
    df['Total'] = df['Math'] + df['Science'] + df['English']

    print("\n", df)   

    # Display Student Scoring more than 85 in Science
    Science_Score = df[df['Science'] > 85]

    print("\nAbove 85 Marks obtained Students in science :","\n",Science_Score)

    # Replace 'Pooja' with 'Puja'
    df['Name'] = df['Name'].replace('Pooja', 'Puja')

    print("\nReplace Pooja Name with Puja :", "\n", df)

    # Q6. Sort by 'Total' marks in descending order
    df_Sorted = df.sort_values(by = 'Total', ascending = False)

    print("\nSort by 'Total' marks in descending order :\n", df_Sorted)

if __name__ == "__main__":
    main()