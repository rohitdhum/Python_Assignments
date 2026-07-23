""" 3: Write a program that scans a specified directory every minute.
The task should display:
• Directory name
• Number of files
• Number of subdirectories
• Date and time of scanning
Use the os module.
"""

import os
import schedule
import time
import datetime

def Display(DirectoryPath):
    if not os.path.isdir(DirectoryPath):
        print(f"Error :The directory file {DirectoryPath} does not exists")
        return

    FileCount = 0
    SubCount = 0

    for FolderName, SubFolder, FileName in os.walk(DirectoryPath):
        FileCount += len(FileName)

        if FolderName != DirectoryPath:
            SubCount += 1

    Time = datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")

    print("_" * 40)
    print(f"Directory Scanned : {DirectoryPath}")
    print(f"Total Files : {FileCount}")
    print(f"Total Subdirectories : {SubCount}")
    print(f"Scan Time :{Time}")
    print("_" * 40)

def main():
    print("....Program is started....")

    DirInput = input("Enter the directory path :")

    schedule.every(1).minutes.do(Display, DirectoryPath = DirInput)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()

"""
Example output:
Directory Scanned: E:/Data
Total Files: 15
Total Subdirectories: 4
Scan Time: 25-07-2026 04:30:00 PM
"""
