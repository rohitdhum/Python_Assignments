""" 3: Design a Python application where multiple threads update a shared variable.
• Use a Lock to avoid race conditions.
• Each thread should increment the shared counter multiple times.
• Display the final value of the counter after all threads complete execution.
"""

import threading
import time

counter = 0
Lock = threading.Lock()

def Display():
    global counter

    for i in range(50000):

        Lock.acquire()

        counter = counter + 1 

        Lock.release()

def main():
    start_time = time.perf_counter()

    global counter

    print("start the program")

    Thread1 = threading.Thread(target = Display)
    Thread2 = threading.Thread(target = Display)

    Thread1.start()
    Thread2.start()

    Thread1.join()
    Thread2.join()

    end_time = time.perf_counter()

    print("All threads executions completed :")
    print(f"Final value of counter : {counter}")

    print(f"Time is required : {end_time - start_time:.4f}")

if __name__ == "__main__":
    main()