""" 3: Design a Python application that creates two threads named EvenList and OddList.
• Both threads should accept a list of integers as input.
• The EvenList thread should:
◦ Extract all even elements from the list.
◦ Calculate and display their sum.
• The OddList thread should:
◦ Extract all odd elements from the list.
◦ Calculate and display their sum.
• Threads should run concurrently.
"""

import threading
import time

def EvenList(No):
    Even = []

    for i in No:
        if i % 2 == 0:
            Even.append(i)
    
    SumOfEven = sum(Even)

    print(f"Even Element : {Even}")
    print(f"Sum of all even elements : {SumOfEven}")

def OddList(No):
    Odd = []

    for i in No:
        if i % 2 != 0:
            Odd.append(i)

    SumOfOdd = sum(Odd)

    print(f"Odd Elements :{Odd}")
    print(f"Sum of all odd elements : {SumOfOdd}")


def main():
    start_time = time.perf_counter()

    Data = [11, 22 ,33, 44, 55, 66, 77, 88, 99, 110]
    print(f"Main Thread of processing List :{Data}")
    
    EvenThread = threading.Thread(target = EvenList, args = (Data,) )
    OddThread = threading.Thread(target = OddList, args = (Data,))

    EvenThread.start()
    OddThread.start()

    EvenThread.join()
    OddThread.join()

    end_time = time.perf_counter()

    print("Exit from the main")

    print(f"Time is required : {end_time - start_time:.4f} seconds")

if __name__ == "__main__":
    main()

