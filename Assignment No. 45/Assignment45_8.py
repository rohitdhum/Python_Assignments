""" Q8: Plot a histogram of math marks.
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

    # Plot a histogram of math marks
    plt.figure()
    df['Math'].plot(
        kind = 'hist',
        bins = 3,
        edgecolor = 'black',
        color = 'skyblue'
    )

    plt.title("Histogram of Math Marks")
    plt.xlabel("Marks Range")
    plt.ylabel("Frequency")
    plt.show()

if __name__ == "__main__":
    main()