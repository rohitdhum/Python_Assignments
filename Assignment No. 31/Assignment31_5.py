""" 5:Write a program that accepts a directory name from the user and
counts the number of files inside it every five minutes.
"""

import os
import schedule
import time
import datetime

def DirecotoryName(DirectoryPath):
    if not os.path.exists(DirectoryPath):
        print(f"Error : File {DirectoryPath} does not exists")
        return

    FileCount = 0

    for FolderName, SubFolder, FileName in os.walk(DirectoryPath):
        FileCount += len(FileName)

    Time = datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")

    fobj = open("DirectoryCountLog.txt", "a")

    fobj.write("_" * 40 + "\n")
    fobj.write(f"Directory OPath : {DirectoryPath}\n")
    fobj.write(f"Number of files : {FileCount}\n")
    fobj.write(f"Date and time : {Time}\n")
    fobj.write("_" * 40 + "\n")

    fobj.close()

    print(f"Success: Directory scan appended to DirectoryCountLog.txt at {Time}")
    
def main():
    print("....Directory File Counter Automation Started....")

    DirInput = input("Enter the directory path :")

    DirecotoryName(DirInput)

    schedule.every(5).minutes.do(DirecotoryName, DirectoryPath = DirInput)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()

"""
Write the result into:
DirectoryCountLog.txt
Each entry should contain:
• Directory path
• Number of files
• Date and time
"""