""" 3: Write a program that counts how many even numbers exist
between 1 and N using Pool.map().
"""

import os
from multiprocessing import Pool

def CountEvenNumber(No):
    EvenCount = No // 2
    pid = os.getpid() 

    return f"Process ID : {pid} \n Input Numbers : {No} \n Even Number Count : {EvenCount}"

def main():
    Data = [1000000, 2000000, 3000000, 4000000]

    with Pool() as pool:
        results = pool.map(CountEvenNumber, Data)

    for res in results:
        print(res)
        print("_" * 40)

if __name__ == "__main__":
    main()

"""
Input
Data = [1000000, 2000000, 3000000, 4000000]
Expected Output Format
Process ID : 1236
Input Number : 1000000
Even Number Count : 500000
"""