""" Q6: Count how many students passed.
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

    pass_count = (df['Status'] == 'Pass').sum()

    # Count Passed students
    print(f"Number of students who passed : {pass_count}")

if __name__ == "__main__":
    main()