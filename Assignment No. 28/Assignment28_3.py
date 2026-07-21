""" Q3) Display File Line by Line
Problem Statement:
Write a program which accepts a file name from the user and displays the contents of the file line by line on the
screen.
"""

import os
import sys

def DisplayFile(FileName):
    if not os.path.exists(FileName):
        print("Error File is not present")
        return
    
    fobj = open(FileName, "r")

    for Dis in fobj:
        print(Dis, end="")

    fobj.close()
    return 

def main():
    if len(sys.argv) < 2:
        print("Error : Please provide a file name")
        print("Usage: python script.py <filename>")
        return
    
    MainFile = sys.argv[1]

    print(f"Display each line of {MainFile} on by one")
    
    DisplayFile(MainFile)

if __name__ == "__main__":
    main()

"""
Input:
Demo.txt
Expected Output:
Display each line of Demo.txt one by one.
"""