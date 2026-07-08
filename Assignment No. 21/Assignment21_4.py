""" 10: Design a Python application that creates two threads.
• Thread 1 should compute the sum of elements from a list.
• Thread 2 should compute the product of elements from the same list.
• Return the results to the main thread and display them.
"""

import threading
import time

def SumOfElements(numbers, results):
    TotalSum = sum(numbers)

    results["sum"] = TotalSum
    print("Thread1 (Sum) execution is completed")

def ProductOfElements(numbers, results):
    if not numbers:
        results["product"] = 0
        return
    
    TotalProduct = 1
    for i in numbers:
        TotalProduct *= i

    results["product"] = TotalProduct
    print("Thread2 (Product) execution is completed")

def main():
    start_time = time.perf_counter()

    Data = [1,2,3,4,5,6,7,8,9]
    print(f"Input data List {Data}\n")

    Result = {"sum": None, "product": None}

    Thread1 = threading.Thread(target = SumOfElements, args = (Data, Result))
    Thread2 = threading.Thread(target = ProductOfElements, args = (Data, Result))

    Thread1.start()
    Thread2.start()

    Thread1.join()
    Thread2.join()

    end_time = time.perf_counter()

    print(f"Final sum of elements from main thread :{Result["sum"]}")
    print(f"Final product of elements from main thread :{Result["product"]}")
    print("Exit from main thread")
    
    print(f"Time is required : {end_time - start_time:.4f}")

if __name__ == "__main__":
    main()