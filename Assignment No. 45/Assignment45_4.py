""" Q4: Plot a pie chart of subject marks for 'Sagar'.
"""

import matplotlib.pyplot as plt
import pandas as pd

def main():
    Data = {
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [85, 90, 78],
        'Science': [92, 88, 80],
        'English': [75, 85, 82]
    }

    df = pd.DataFrame(Data)

    # Extract Sagar's row data into series
    Sagar_Marks = df[df['Name'] == 'Sagar'][['Math', 'Science', 'English']].squeeze()

    # Plot the pie chart
    plt.figure
    Sagar_Marks.plot(kind='pie', autopct ='%1.1f%%', startangle = 90, color = ['#ff9999','#66b3ff','#99ff99'])
    plt.title("Sagara's marks Distribustion")
    plt.ylabel('') # Hides the default vertical axis label
    plt.show()

if __name__ == "__main__":
    main()