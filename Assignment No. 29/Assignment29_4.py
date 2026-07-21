""" Q4) Compare Two Files (Command Line)
Problem Statement:
Write a program which accepts two file names through command line arguments and compares the contents of
both files.
• If both files contain the same contents, display Success
• Otherwise display Failure
"""

import os
import sys

def SameContents(FileName1, FileName2):
    if not os.path.exists(FileName1):
        print(f"Error file is {FileName1} does not exist")
        return
    
    if not os.path.exists(FileName2):
        print(f"Error file is {FileName2} does not exist")
        return
    
    fobj1 = open(FileName1, "r")
    Content1 = fobj1.read()

    fobj2 = open(FileName2, "r")
    Content2 = fobj2.read()

    fobj1.close()
    fobj2.close()

    if Content1 == Content2:
        print("Success")

    else:
        print("Failure")

def main():
    if len(sys.argv) < 3:
        print("Error: Please provide two file names as command line arguments.")
        print("Usage: python Assignment29_4.py <file1> <file2>")
        return
    
    File1 = sys.argv[1]
    File2 = sys.argv[2]

    SameContents(File1, File2)

if __name__ == "__main__":
    main()

"""
Input (Command Line):
Demo.txt Hello.txt
Expected Output:
Success OR Failure
"""