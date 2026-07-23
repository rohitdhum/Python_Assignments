""" 3: Write a program that reads and displays the contents of a specified
text file every minute.
Handle the following conditions:
• File does not exist
• File is empty
• Permission is denied
• File cannot be opened
"""

import os
import stat
import schedule
import time

def Display(FileName):
    if not os.path.exists(FileName):
        print(f"Error file {FileName} is doest not exist")
        return

    if not os.path.isfile(FileName):
        print(f"Error :File cannot be opened")
        return

    try:    
        if os.path.getsize(FileName) == 0:
            print(f"Error :File {FileName} is empty")
            return

        fobj = open(FileName, "r")
        Data = fobj.read()
        print(Data)

        fobj.close()
        print("_" * 40)

    except PermissionError:
        print(f"Error :Permission is denied {FileName}")
        return

def main():
    Name = input("Enter the name of the file :")
    print("....Program is started....")

    schedule.every(1).minutes.do(Display, FileName = Name)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()