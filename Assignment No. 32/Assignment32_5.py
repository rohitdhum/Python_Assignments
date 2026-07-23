""" 5: Write a program that deletes all empty files from a specified
directory every hour.
The program should:
• Scan the directory recursively
• Detect files whose size is zero bytes
• Delete the empty files
• Store deleted file paths in a log file
• Handle permission errors
Test the program only on a sample directory.
"""

import os
import schedule
import time
import datetime

def DeleteEmptyFiles(DirectoryPath, LogFile="delete_log.txt"):
    if not os.path.exists(DirectoryPath):
        print(f"Error :Target directory {DirectoryPath} does not exist.")
        return

    timestamp = datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")
    
    fobj = open(LogFile, "a")
    fobj.write(f"\nCleanup Scan Initiated At :{timestamp}\n")
    print(f"\nScanning for empty files at {timestamp}")

    DeletedCount = 0

    for FolderName, SubFolders, FileNames in os.walk(DirectoryPath):
        for filename in FileNames:
            FilePath = os.path.join(FolderName, filename)

            try:
                if os.path.isfile(FilePath) and os.path.getsize(FilePath) == 0:
                    os.remove(FilePath)
                    DeletedCount += 1
                    
                    log_msg = f"[DELETED] Empty File: {FilePath}"
                    print(log_msg)
                    fobj.write(log_msg + "\n")

            except PermissionError:
                ErrorMsg = f"[PERMISSION DENIED] Cannot access or delete: {FilePath}"
                print(ErrorMsg)
                fobj.write(ErrorMsg + "\n")

            except FileNotFoundError:
                pass

    fobj.write(f"Total empty files removed :{DeletedCount}\n")

    fobj.close()
    
def main():
    print("....Program is started....")

    Input = input("Enter the directory path :")

    if not os.path.exists(Input):
        print("Error :Specified directory does not exist")
        return

    schedule.every(10).seconds.do(DeleteEmptyFiles, DirectoryPath = Input)

    DeleteEmptyFiles(Input)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
