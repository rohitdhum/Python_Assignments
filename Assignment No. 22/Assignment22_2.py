""" 2. Write a program that calculates factorials of multiple numbers
simultaneously using Pool.map().
"""

import math
import os
from multiprocessing import Pool

def Factorials(No):
    ProcessID = os.getpid()
    Result = math.factorial(No)
    return ProcessID, No, Result

def main():
    Numbers = [10, 15, 20, 25]

    with Pool() as pool:
        Ret = pool.map(Factorials, Numbers)

    print(f"{"Process ID" :<12} {"Input Number" :<12} {"Factorial"}")

    print("-" * 50)

    for pid, num, result in Ret:
        print(f"{pid:<12} {num:<12} {result}")
 
if __name__ == "__main__":
    main()

"""
Input
[10,15,20,25]
Display
• Process ID
• Input Number
• Factorial
"""