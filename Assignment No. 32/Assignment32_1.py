""" 1: Write a program that creates a new text file every minute.
The filename should contain the current timestamp.
Example:
File_25_07_2026_16_30_00.txt
Write the following information into the file:
• Filename
• Creation date
• Creation time
"""

import schedule
import time
import datetime

def Display():
    Now = datetime.datetime.now()
    TimeStamp = Now.strftime("%d_%m_%Y_%H_%M_%S")
    Date = Now.strftime("%d_%m_%Y")
    Time = Now.strftime("%H:%M:%S")

    FileName = f"File_{TimeStamp}.txt"

    fobj = open(FileName, "w")
    fobj.write(f"FileName :{FileName}\n")
    fobj.write(f"Creation date :{Date}\n")
    fobj.write(f"Creation time :{Time}\n")

    fobj.close()

    print(f"File is Successfully created :{FileName}")

def main():
    print("....Program is started....")

    schedule.every(1).minutes.do(Display)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()