""" 4: Write a program that copies all .txt files from one directory to
another every ten minutes.
The program should:
• Accept source and destination directories
• Validate both directories
• Copy only .txt files
• Maintain a log of copied files
• Avoid terminating if one file cannot be copied
"""

import os
import shutil
import schedule
import time
import datetime

def CopyTxtFiles(SourceDir, DestDir, LogFile="copy_log.txt"):
    if not os.path.exists(SourceDir):
        print(f"Error :Source directory {SourceDir} does not exist.")
        return
    
    if not os.path.exists(DestDir):
        print(f"Error :Destination directory {DestDir} does not exist.")
        return

    timestamp = datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")
    
    fobj = open(LogFile, "a")
    fobj.write(f"\n--- Scan Initiated At :{timestamp} ---\n")
    fobj.write(f"\nScanning for .txt files at {timestamp}...")

    copied_count = 0
  
    for filename in os.listdir(SourceDir):
 
        if filename.lower().endswith('.txt'):
            source_file_path = os.path.join(SourceDir, filename)
            dest_file_path = os.path.join(DestDir, filename)

            if os.path.isfile(source_file_path):
                try:
                    shutil.copy2(source_file_path, dest_file_path)
                    copied_count += 1
                        
                    log_msg = f"[SUCCESS] Copied :{filename} -> {DestDir}"
                    print(log_msg)
                    fobj.write(log_msg + "\n")
                        
                except Exception as e:
                    error_msg = f"[FAILURE] Could not copy {filename} Reason: {e}"
                    print(error_msg)
                    fobj.write(error_msg + "\n")
                        
    fobj.write(f"Total files successfully transferred in this cycle :{copied_count}\n")

    fobj.close()

def main():
    print("....Program is started....")

    Source = input("Enter Source directory path :")
    Destination = input("Enter Destination directory path :")
 
    if not os.path.exists(Source) or not os.path.exists(Destination):
        print("Initial Validation Failure :One or both directories do not exist")
        return

    schedule.every(10).minutes.do(CopyTxtFiles, SourceDir=Source, DestDir=Destination)

    CopyTxtFiles(Source, Destination)

    while True:
            schedule.run_pending()
            time.sleep(1)

if __name__ == "__main__":
    main()
