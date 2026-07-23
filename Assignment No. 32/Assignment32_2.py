""" 2: Write a Python program that monitors the size of a specified file
every 30 seconds.
Write the following details into:
FileSizeLog.txt
• File path
• File size in bytes
• Date and time
Handle the situation where the file does not exist.
"""

import os
import schedule
import time
import datetime

def SizeOfFile(FileName):
    if not os.path.exists(FileName):
        print(f"Error :File is {FileName} does not exists")
        return

    FileSize = os.path.getsize(FileName)

    Now = datetime.datetime.now().strftime("%d-%m-%Y_ %I:%M:%S %p")

    LogFile = "FileSizeLog.txt"

    fobj = open(LogFile, "a") 
    fobj.write(f"File path :{os.path.abspath(FileName)}\n")
    fobj.write(f"File size :{FileSize} in bytes\n")
    fobj.write(f"Date and time :{Now}\n")
    fobj.write("_" * 40 + "\n")
    
    fobj.close()

    print(f"Loged details for {FileName} successfully")

def main():
    print("....Program is strated....")

    FileLogName = "Demo.txt"
    schedule.every(30).seconds.do(SizeOfFile, FileName = FileLogName )

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()