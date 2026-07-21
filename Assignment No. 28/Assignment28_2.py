""" Q2) Count Words in a File
Problem Statement:
Write a program which accepts a file name from the user and counts the total number of words in that file.
"""

import os
import sys

def CountWords(FileName):
    if not os.path.exists(FileName):
        print("Error File is not present")
        return
    
    fobj = open(FileName, "r")
    count = 0

    for Line in fobj:
        Words = Line.split()
        count += len(Words)
    
    fobj.close()
    return count

def main():
    if len(sys.argv) < 2:
        print("Error : Please provide a file name")
        print("Usage: python script.py <filename>")
        return
    
    MainFile = sys.argv[1]

    TotalWords = CountWords(MainFile)

    print(f"Total Number of Words in {MainFile} : {TotalWords}")

if __name__ == "__main__":
    main()

"""
Input:
Demo.txt
Expected Output:
Total number of words in Demo.txt.
"""