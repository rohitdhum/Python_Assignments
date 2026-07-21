""" Q3) Copy File Contents into a New File (Command Line)
Problem Statement:
Write a program which accepts an existing file name through command line arguments, creates a new file
named Demo.txt, and copies all contents from the given file into Demo.txt.
"""

import os
import sys

def ContentOfFile(FileName1, FileName2):
    if not os.path.exists(FileName1):
        print(f"{FileName1} is not present")
        return
    
    fobj1 = open(FileName1, "r")
    fobj2 = open(FileName2, "w")
    
    for Line in fobj1:
        fobj2.write(Line)

    fobj1.close()
    fobj2.close()

def main():
    if len(sys.argv) < 2:
        print("Error: Please provide the input file name as a command line argument.")
        print("Usage: python Assignment29_3.py <filename1> <FileName2> ")
        return
    
    FileName1 = sys.argv[1]
    FileName2 = "Demo.txt"

    ContentOfFile(FileName1, FileName2)

    print(f"Successfully copied contents of {FileName1} into {FileName2}")

if __name__ == "__main__":
    main()

"""
Input (Command Line):
ABC.txt
Expected Output:
Create Demo.txt and copy contents of ABC.txt into Demo.txt.
"""