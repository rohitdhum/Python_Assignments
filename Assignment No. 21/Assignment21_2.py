""" 2: Design a Python application that creates two threads.
• Thread 1 should calculate and display the maximum element from an list.
• Thread 2 should calculate and display the minimum element from the same list.
• The list should be accepted from the user.
"""

import threading
import time

def Maximum(No):
    if not No:
        print(" Thread1 : List is empty")
        return
    
    Maximum = max(No)
    print(f"Thread1 Maximum : {Maximum}")

def Minimum(No):
    if not No:
        print("Thread 2 : List is empty")
        return
    
    Minimum = min(No)
    print(f"Thread2 Minimum : {Minimum}")  

def main():
    InputData = input("Enter Numbers :")
    SplitData = InputData.split()
    Data = []

    for i in SplitData:
        if i.strip("-").isdigit():
            Data.append(int(i))

    print("Input Data :", Data)

    start_time = time.perf_counter()

    MaximumThread = threading.Thread(target = Maximum, args = (Data,)) 
    MinimumThread = threading.Thread(target = Minimum, args = (Data,))

    MaximumThread.start()
    MinimumThread.start()

    MaximumThread.join()
    MinimumThread.join()

    end_time = time.perf_counter()

    print("Exit from main thread")
    
    print(f"Time is required {end_time - start_time:.4f} seconds:")

if __name__ == "__main__":
    main()