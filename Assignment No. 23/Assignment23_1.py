""" 1: Write a Python program using multiprocessing.Pool to calculate the
sum of all even numbers from 1 to N for every number from the given
list.
"""

import os
from multiprocessing import Pool

def EvenNumber(No):
    k = No // 2
    EvenSum = k * (k + 1)
    pid = os.getpid() 

    return f"Process ID : {pid} \n Input Number : {No} \n Sum of even Numbers : {EvenSum}"

def main():
    Data = [1000000, 2000000, 3000000, 4000000]

    with Pool() as pool:
        results = [pool.apply_async(EvenNumber, (No,)) for No in Data]

        for res in results:
            print(res.get())
            print("_" * 50)

if __name__ == "__main__":
    main()


"""
Input
Data = [1000000, 2000000, 3000000, 4000000]
Expected Task
For each number N, calculate:
2 + 4 + 6 + ... + N
Expected Output Format
Process ID : 1234
Input Number : 1000000
Sum of Even Numbers : 250000500000
"""