""" 4: Write a program that creates a new log file after every ten minutes.
The filename should contain the current date and time.
"""

import schedule
import time
import datetime

def LogFile():
    FileNameTime = datetime.datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
    FileName = f"MarvellousLog_{FileNameTime}.txt"
    InsideTime = datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")

    fobj = open(FileName, "w")
    fobj.write("Log file created successfully\n")
    fobj.write(f"Creation Time :{InsideTime}\n")

    fobj.close()

    print(f"Success : Log file created {FileName}")

def main():
    print("....LogFile Automation Program is Stated....")

    LogFile()

    schedule.every(30).minutes.do(LogFile)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()

"""
Example:
MarvellousLog_25_07_2026_16_30_00.txt
The file should contain:
Log file created successfully.
Creation Time: 25-07-2026 04:30:00 PM
"""