""" 
2: Write a Python program that displays the current date and time
after every one minute.
Use the datetime module.
"""

import schedule
import time
import datetime

def Display():
    print("Current Date is :", datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p"))    

def main():
    print("....Program is started....")

    schedule.every(1).minutes.do(Display)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()

"""
Expected output:
Current Date and Time: 25-07-2026 04:30:00 PM
"""