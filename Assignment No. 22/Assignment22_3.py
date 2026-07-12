""" 3. For every number in the given list, count how many prime numbers
exist between 1 and N using multiprocessing Pool.
"""

import multiprocessing
import math
import time

def PrimeNumber(No):
    if No < 2:
        return False
    
    for i in range(2, int(No ** 0.5)+1):
        if No % i == 0:
            return False
    return True

def PrimeCount(N):
    # Counts primes between 1 and N.
    return sum(1 for i in range(1, N+1) if PrimeNumber(i))

def main():
    Numbers = [10000, 20000, 30000, 40000]

    with multiprocessing.Pool() as pool:
        Results = pool.map(PrimeCount, Numbers)

    for No, count in zip(Numbers, Results):
        print(f"Total prime numbers between 1 amd {No} : {count}")

if __name__ == "__main__":
    main()

"""
Example
10000
20000
30000
40000
Display total prime count for each number.
"""