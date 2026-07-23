""" 6: Write a script that schedules the following tasks:
• Print Lunch Time! every day at 1:00 PM.
• Print Wrap up work every day at 6:00 PM.
Both tasks should be handled by separate functions.
"""

import schedule
import time
import datetime

def Disp1():
    print("Lunch Time!", datetime.datetime.now())

def Disp2():
    print("Wrap up work", datetime.datetime.now())

def main(): 
    print("....Program is started....")

    schedule.every().day.at("13:00").do(Disp1)

    schedule.every().day.at("18:00").do(Disp2)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()