""" Q5: Add a new column 'Status' where students with total >= 250 are 'Pass', else 'Fail'.
"""

import pandas as pd

def main():
    Data = {
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [85, 90, 78],
        'Science': [92, 88, 80],
        'English': [75, 85, 82]
    }

    df = pd.DataFrame(Data)

    # Calculate Total Column
    df['Total'] = df['Math'] + df['Science'] + df['English']

    # Apply the condition
    df['Status'] = df['Total'].apply(lambda x : 'Pass' if x >= 250 else 'Fail')

    print(df[['Name', 'Total', 'Status']])

if __name__ == "__main__":
    main()