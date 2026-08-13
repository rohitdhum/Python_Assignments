""" Q2: Create a gender column and perform one-hot encoding. 
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

    # Create column 'Gender' 
    df['Gender'] = ['Male', 'Male', 'Female']

    df_encoded = pd.get_dummies(df, columns=['Gender'], dtype = int)

    print(df_encoded)

if __name__ == "__main__":
    main()