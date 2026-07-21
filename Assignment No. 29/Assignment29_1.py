""" Q1) Check File Exists in Current Directory
Problem Statement:
Write a program which accepts a file name from the user and checks whether that file exists in the current
directory or not.
"""

import os
import sys

def Directory(FileName):
    if os.path.exists(FileName):
        return True

    else:
        return False

def main():
    if len(sys.argv) != 2:
        print("Error: Please provide a correct file name and word")
        print("Usage: python script.py <filename1> <word>")
        return
    
    FileName = sys.argv[1]

    ExistsFile = Directory(FileName)
    
    if ExistsFile:
        print(f"The file {FileName} is exists in the current directory")
    
    else:
        print(f"The file {FileName} is not exists in the current directory")

if __name__ == "__main__":
    main()

"""
Input:
Demo.txt
Expected Output:
Display whether Demo.txt exists or not.
"""