""" Q10: Plot a boxplot for English marks to check distribution and outliers.
"""

import pandas as pd
import matplotlib.pyplot as plt

def main():
    Data = {
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [85, 90, 78],
        'Science': [92, 88, 80],
        'English': [75, 85, 82]
    }

    df = pd.DataFrame(Data)
 
    # Plot a boxplot for English marks
    plt.figure()
    df['English'].plot(kind='box')
    plt.title("Boxplt of English Marks")
    plt.ylabel("Marks")
    plt.show()
    
if __name__ == "__main__":
    main()