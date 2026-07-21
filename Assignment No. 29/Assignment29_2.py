""" Q2) Display File Contents
Problem Statement:
Write a program which accepts a file name from the user, opens that file, and displays the entire contents on the
console.
"""

import os
import sys

def ContentsOfFiles(FileName):
    if not os.path.exists(FileName):
        print("Error file is not present")
        return
    
    fobj = open(FileName, "r")

    Content = fobj.read()
    print(f"Display the contents of {FileName} on console \n{Content}")

def main():
    if len(sys.argv) != 2:
        print("Error: Please provide a correct file name")
        print("Usage: python script.py <filename1>")
        return
    
    FileName = sys.argv[1]

    ContentsOfFiles(FileName)

if __name__ == "__main__":
    main()

"""
Input:
Demo.txt
Expected Output:
Display contents of Demo.txt on console.
"""