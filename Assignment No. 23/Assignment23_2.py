""" 2: Write a Python program using multiprocessing.Pool to calculate the
sum of all odd numbers from 1 to N.
"""

import os
from multiprocessing import Pool

def OddNumber(No):
    k = No // 2
    OddSum = k * k
    pid = os.getpid() 

    return f"Process ID : {pid} \n Input Number : {No} \n Sum of Odd Numbers : {OddSum}"

def main():
    Data = [1000000, 2000000, 3000000, 4000000]

    with Pool() as pool:
        results = [pool.apply_async(OddNumber, (No,)) for No in Data]

        for res in results:
            print(res.get())
            print("_" * 40)
            
if __name__ == "__main__":
    main()

"""
Input
Data = [1000000, 2000000, 3000000, 4000000]
Expected Task
For each number N, calculate:

1 + 3 + 5 + ... + N
Expected Output Format

Process ID : 1235
Input Number : 1000000
Sum of Odd Numbers : 250000000000
"""