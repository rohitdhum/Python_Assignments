"""1. Write a program that accepts a list of integers and uses Pool.map()
to calculate the sum of squares from 1 to N for every element in the
list.
"""

from multiprocessing import Pool

def SumOfSquares(No):
    return No * (No+1) * (2 * No+1 ) // 6

def main():
    Numbers = [1000000,2000000,3000000,4000000]

    with Pool() as pool:
        Ret = pool.map(SumOfSquares, Numbers)
    
    print(Ret)

if __name__ == "__main__":
    main()

"""
Example Input
[1000000,2000000,3000000,4000000]
Expected Output
[333333833333500000,
2666668666667000000,
...
]
"""