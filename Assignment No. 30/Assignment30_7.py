""" 7: Write a Python program that performs a file backup every hour.
The program should:
1. Accept the source file path.
2. Accept the destination directory path.
3. Copy the source file to the destination directory.
4. Add the current date and time to the backup filename.
5. Write the backup operation details into:
backup_log.txt
Example backup filename:
Data_25_07_2026_16_30_00.txt
Example log entry:
Backup completed successfully at 25-07-2026 04:30:00 PM
Use the shutil module for file copying.
"""

import os
import sys
import schedule
import time
import datetime
import shutil

SourceFile = ""
DestDirectory = ""
LogFile = "backup_log.txt"

def Backup():
    BaseName, FileExtension = os.path.splitext(os.path.basename(SourceFile))

    TimestampFilename = datetime.datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
    TimestampLog = datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")

    BackupFilename = f"{BaseName}_{TimestampFilename}{FileExtension}"
    DestinationPath = os.path.join(DestDirectory, BackupFilename)

    os.makedirs(DestDirectory, exist_ok=True)

    shutil.copy2(SourceFile, DestinationPath)

    LogEntry = f"Backup completed successfully at {TimestampLog}\n"
     
    fobj = open(LogFile, "a") 
    fobj.write(LogEntry)

    fobj.close()

    print(f"[{TimestampLog}] {LogEntry.strip()} -> {BackupFilename}")

def main():
    global SourceFile, DestDirectory

    print("....Program is started....")

    if len(sys.argv) < 3:
        print("Usage: python script.py <source_file_path> <destination_directory_path>")
        return
    
    SourceFile = sys.argv[1]
    DestDirectory = sys.argv[2]

    schedule.every(1).minutes.do(Backup)

    print(f"\nB ackup service successfully schedule for : {SourceFile}")
    print(f"Backup will save to {DestDirectory}")

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()