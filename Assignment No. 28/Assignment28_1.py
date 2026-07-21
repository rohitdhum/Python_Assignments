"""Q1) Count Lines in a File
Problem Statement:
Write a program which accepts a file name from the user and counts how many lines are present in the file.
"""

import os
import sys

def CountLines(FileName):
    if not os.path.exists(FileName):
        print("Error File is not present")
        return None
    
    fobj = open(FileName, "r")
    count = 0

    for Line in fobj:
        count += 1

    fobj.close()
    return count

def main():
    if len(sys.argv) < 2:
        print("Error: Please provide a file name.")
        print("Usage: python script.py <filename>")
        return
    
    MainFile = sys.argv[1]

    TotalLines = CountLines(MainFile)

    print(f"Total number of lines in {MainFile} is : {TotalLines}")

if __name__ == "__main__":
    main()

""" 
Input:
Demo.txt
Expected Output:
Total number of lines in Demo.txt.
"""