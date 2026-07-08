""" 5: Design a Python application that creates two threads named Thread1 and Thread2.
• Thread1 should display numbers from 1 to 50.
• Thread2 should display numbers from 50 to 1 in reverse order.
• Ensure that:
◦ Thread2 starts execution only after Thread1 has completed.
• Use appropriate thread synchronization
"""

import threading
import time

def DisplaySequence():
    ThreadName = threading.current_thread().name
    print(f"Thread is started : {ThreadName}")

    for i in range(1,51):
        print(i)
    
    print(f"{ThreadName} : finished")

def DisplayReverse():
    ThreadName = threading.current_thread().name
    print(f"Thread is started : {ThreadName}")

    for i in range (50,0,-1):
        print(i)

    print(f"{ThreadName} : finished")

def main():
    start_time = time.perf_counter()
    
    Thread1 = threading.Thread(target = DisplaySequence, name = "Thread1")
    Thread2 = threading.Thread(target = DisplayReverse, name = "Thread2")

    Thread1.start()
    Thread1.join()

    Thread2.start()
    Thread2.join()

    end_time = time.perf_counter()

    print("Exit from the main")

    print(f"Time is required : {end_time - start_time:.4f}")

if __name__ == "__main__":
    main()