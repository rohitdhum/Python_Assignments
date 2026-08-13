""" Q7: Export the final DataFrame to a CSV file.
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

    # Export to the working directory without the pandas index row
    df.to_csv('final_student.csv', index = False)

    print("File Exported Successfully")

if __name__ == "__main__":
    main()