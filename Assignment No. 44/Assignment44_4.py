""" Q4: Display students who scored more than 85 in Science.
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

    # Q5. Display Student Scoring more than 85 in Science
    Science_Score = df[df['Science'] > 85]

    print("\nAbove 85 Marks obtained Students in science :","\n",Science_Score)

if __name__ == "__main__":
    main()