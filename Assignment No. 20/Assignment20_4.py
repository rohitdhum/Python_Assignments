""" 4: Design a Python application that creates three threads named Small, Capital, and
Digits.
• All threads should accept a string as input.
• The Small thread should count and display the number of lowercase characters.
• The Capital thread should count and display the number of uppercase characters.
• The Digits thread should count and display the number of numeric digits.
• Each thread must also display:
◦ Thread ID
◦ Thread Name
"""

import threading
import time

def Small(No):
    print(f"Thread ID  of Small thread is :{threading.get_ident()}")
    print(f"Threading Name of Small thread is :{threading.current_thread().name}")

    count = 0
    for char in No:
        if char.islower():
            count += 1

    print(f"Lowercase character count :{count}\n")

def Capital(No):
    print(f"Thread ID  of capital thread is :{threading.get_ident()}")
    print(f"Threading Name of Capital thread is :{threading.current_thread().name}")

    count = 0
    for char in No:
        if char.isupper():
            count += 1
    
    print(f"Uppercase character count :{count}\n")

def Digits(No):
    print(f"Thread ID  of Digits thread is :{threading.get_ident()}")
    print(f"Threading Name of Digits thread is :{threading.current_thread().name}")

    count = 0
    for char in No:
        if char.isdigit():
            count += 1

    print(f"Numeric digit count :{count}\n")


def main():
    String = input("Enter a string :")

    start_time = time.perf_counter()

    SmallThread = threading.Thread(target = Small, name = "Small", args = (String,))
    CapitalThread = threading.Thread(target = Capital, name = "Capital", args = (String,))
    DigitsThread = threading.Thread(target = Digits, name = "Digits", args = (String,))

    SmallThread.start()
    CapitalThread.start()
    DigitsThread.start()

    SmallThread.join()
    CapitalThread.join()
    DigitsThread.join()

    end_time = time.perf_counter()

    print("Exit from the main")

    print(f"Required time is : {end_time - start_time:.4f} seconds")

if __name__ == "__main__":
    main()