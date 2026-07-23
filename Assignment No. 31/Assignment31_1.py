""" 1: Write a program that accepts:
• A message from the user
• A time interval in seconds
Schedule the program to display the message repeatedly after the specified interval.
"""

import schedule
import time
import datetime

def Disp1(Message):
    Time = datetime.datetime.now().strftime("%H:%M:%S")

    print(f"{Message} (Message printed at {Time})")

def main():
    print("....Program is started....")

    Msg = input("Enter Message :")

    while True:
        Interval = int(input("Enter interval time :"))

        if Interval > 0:
            break

        else:
            print("Error : Interval must be greater than zero...!")

    print(f"schedule task is run every {Interval} seconds\n")
    
    schedule.every(Interval).seconds.do(Disp1, Message = Msg)

    while True:
        schedule.run_pending()
        time.sleep(1)   

if __name__ == "__main__":
    main()

"""
Example input:
Enter message: Jay Ganesh
Enter interval in seconds: 5
Expected output:
Jay Ganesh
every five seconds.

Validate that the interval is greater than zero.
"""