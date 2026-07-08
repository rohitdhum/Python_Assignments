""" 2: Design a Python application that creates two threads named EvenFactor and
OddFactor.
• Both threads should accept one integer number as a parameter.
• The EvenFactor thread should:
◦ Identify all even factors of the given number.
◦ Calculate and display the sum of even factors.
• The OddFactor thread should:
◦ Identify all odd factors of the given number.
◦ Calculate and display the sum of odd factors.
• After both threads complete execution, the main thread should display the message:
“Exit from main”
"""

import threading
import time

def EvenFactor(No):
    Even = []

    for i in range(1, No + 1):
        if No % i == 0:
            if i % i % 2 == 0:
                pass
            if i % 2 == 0:
                Even.append(i)

    SumOfEven = sum(Even)

    print(f"Even Factors : {Even}")
    print(f"Sum of Even Factor : {SumOfEven}")

def OddFactor(No):
    Odd = []

    for i in range(1, No + 1):
        if No % i == 0:
            if i % 2 != 0:
                Odd.append(i)

    SumOfOdd = sum(Odd)

    print(f"Odd Factors : {Odd}")
    print(f"Sum of Odd Factors : {SumOfOdd}")

def main():
    start_time = time.perf_counter()

    InputNumber = int(input("Enter Input :"))

    EvenThread = threading.Thread(target = EvenFactor, args = (InputNumber,) )

    OddThread = threading.Thread(target = OddFactor, args = (InputNumber,) )

    EvenThread.start()
    OddThread.start()

    EvenThread.join()
    OddThread.join()

    end_time = time.perf_counter()

    print("Exit from the main")

    print(f"Time required is : {end_time - start_time:.4f}seconds")

if __name__ == "__main__":
    main()