""" 1: Design a Python application that creates two threads named Prime and NonPrime.
• Both threads should accept a list of integers.
• The Prime thread should display all prime numbers from the list.
• The NonPrime thread should display all non-prime numbers from the list.
"""

import threading
import time

printLock = threading.Lock()

def Prime(List):
    ThreadName = threading.current_thread().name
    
    with printLock:
        print(f"{ThreadName} is started")
        print(f"{ThreadName} found Prime number")

        for No in List:
            if No <= 1:
                continue

            PrimeNumber = True
    
            for i in range(2, int(No ** 0.5) + 1):
                if No % i == 0:
                    PrimeNumber = False
                    break

            if PrimeNumber:
                print(No)
    
def NonPrime(List):
    ThreadName = threading.current_thread().name
    
    with printLock:
        print(f"{ThreadName} is started")
        print(f"{ThreadName} : found NonPrime number")

        for No in List:
            if No <= 1:
                print(No)
                continue

            PrimeNumber = True

            for i in range(2, int(No ** 0.5) + 1):
                if No % i == 0:
                    PrimeNumber = False
                    break

            if not PrimeNumber:
                print(No)

def main():
    start_time = time.perf_counter()

    Data = [2, 3, 4, 7, 10, 11, 15, 19, 20, 23, 24, 1, 0, 17]
    print("Input Data list :", Data)
    
    PrimeThread = threading.Thread(target = Prime, name = "Prime Thread", args = (Data,))
    NonPrimeThread = threading.Thread(target = NonPrime, name = "NonPrime Thread", args = (Data,))

    PrimeThread.start()
    NonPrimeThread.start()

    PrimeThread.join()
    NonPrimeThread.join()

    end_time = time.perf_counter()

    print("Exit from the main")

    print(f"Time requird is :{end_time - start_time:.4f}")


if __name__ == "__main__":
    main()