""" 5: Write a program that calculates factorials of multiple numbers
simultaneously using multiprocessing.Pool.
"""

import os
import math
from multiprocessing import Pool

def CalculateFactorial(No):
    FactResult = math.factorial(No)
    pid = os.getpid() 

    return f"Process ID : {pid} \n Input Number : {No} \n Factorial : {FactResult}"

def main():
    Data = [10, 15, 20, 25]

    with Pool() as pool:
        results = pool.map(CalculateFactorial, Data)

    for res in results:
        print(res)
        print("_" * 40)

if __name__ == "__main__":
    main()

"""
Input

Data = [10, 15, 20, 25]
Expected Task
For every N, calculate:

N!
Expected Output Format
Process ID : 1240
Input Number : 20
Factorial : 2432902008176640000
"""