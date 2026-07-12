""" 4: Write a program that counts how many odd numbers exist between
1 and N.
"""

import os
from multiprocessing import Pool

def CountOddNumber(No):
    OddCount = (No + 1) // 2
    pid = os.getpid() 

    return f"Process ID : {pid} \n Input Number : {No} \n Odd Count Number : {OddCount}"

def main():
    Data = [1000000, 2000000, 3000000, 4000000]

    with Pool() as pool:
        results = pool.map(CountOddNumber, Data)

    for res in results:
        print(res)
        print("_" * 40)

if __name__ == "__main__":
    main()

"""
Input
Data = [1000000, 2000000, 3000000, 4000000]
Expected Output Format
Process ID : 1237
Input Number : 1000000
Odd Count Number : 500000
"""
