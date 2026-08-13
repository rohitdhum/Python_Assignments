""" Q1: Normalize the 'Math' scores using Min-Max scaling.
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

    # Formula (X-min) / (max-min)
    df['Math'] = (df['Math'] - df['Math'].min()) / (df['Math'].max() - df['Math'].min())

    print(df[['Name', 'Math']])

if __name__ == "__main__":
    main()