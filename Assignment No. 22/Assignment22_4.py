""" 4. Write a program that calculates
1^5+2^5+3^5+.....+N^5
for multiple values of N simultaneously using Pool.
"""

import multiprocessing
import time

def Calculations(No):
    """Calculates 1^5 + 2^5 + ... + N^5 for a given N."""

    return sum(i**5 for i in range(1, No + 1))

def main():
    start_time = time.perf_counter()

    Numbers = [1000000, 2000000, 3000000, 4000000]

    print("Calculating the sum simultaneously using pool")

    with multiprocessing.Pool() as pool:
        Result = pool.map(Calculations, Numbers)

    end_time = time.perf_counter()

    for num, result in zip(Numbers, Result):
        print(f"Sum of N : {num} : {result}")

    print(f"Required time is : {end_time - start_time:.4f}")

if __name__ == "__main__":
    main()

"""
Input
[1000000,
2000000,
3000000,
4000000]
Measure total execution time.
"""