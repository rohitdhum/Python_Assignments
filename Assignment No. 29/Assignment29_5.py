""" Q5) Frequency of a String in File
Problem Statement:
Write a program which accepts a file name and one string from the user and returns the frequency (count of
occurrences) of that string in the file.
"""

import os
import sys

def FrequencyCount(FileName, String):
    if not os.path.exists(FileName):
        print(f"Error file is {FileName} does not exist")
        return
    
    fobj1 = open(FileName, "r")
    Content = fobj1.read()
    fobj1.close()

    Frequency = Content.count(String)
    return Frequency

def main():
    if len(sys.argv) != 3:
        print("Error: Please provide a file and string.")
        print("Usage: python Assignment29_5.py <file1> <String>")
        return
    
    File = sys.argv[1]
    Str = sys.argv[2] 

    print(f"Count how many times {Str} appears in {File}")

    TotalFrequency = FrequencyCount(File, Str)

    print(f"Frequency : {TotalFrequency}")

if __name__ == "__main__":
    main()

"""
Input:
Demo.txt Marvellous
Expected Output:
Count how many times "Marvellous" appears in Demo.txt.
"""