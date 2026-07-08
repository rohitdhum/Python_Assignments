""" 1: Design a Python application that creates two separate threads named Even and Odd.
• The Even thread should display the first 10 even numbers.
• The Odd thread should display the first 10 odd numbers.
• Both threads should execute independently using the threading module.
• Ensure proper thread creation and execution.
"""

import threading
import time

def Even():
    for i in range(10):
        No = i * 2
        print(f"Even thread :{No}")


def Odd():
    for i in range(10):
        No = (i * 2) + 1
        print(f"Odd threads : {No}")

def main():
    start_time = time.perf_counter()

    EvenThread = threading.Thread(target = Even)

    OddThread = threading.Thread(target = Odd)

    EvenThread.start()
    OddThread.start()

    EvenThread.join()
    OddThread.join()

    end_time = time.perf_counter()

    print(f"Time required is :{end_time - start_time:.4f} seconds")

if __name__ == "__main__":
    main()