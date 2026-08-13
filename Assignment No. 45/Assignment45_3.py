""" Q3: Group students by gender and calculate average marks.
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
    
    avg_marks = df.groupby('Gender')[['Math', 'Science', 'English']].mean()

    print("\nAverage Marks :\n", avg_marks)

if __name__ == "__main__":
    main()