""" Q5) Search a Word in File
Problem Statement:
Write a program which accepts a file name and a word from the user and checks whether that word is present in
the file or not.
"""

import os
import sys

def CheckWord(FileName, Word):
    if not os.path.exists(FileName):
        print("Error File is not present")
        return
    
    fobj1 = open(FileName, "r")
    Found = False

    for Line in fobj1:
        WordsLine = Line.split()

        if Word in WordsLine:
            Found = True
            break

    fobj1.close()
    return Found

def main():
    if len(sys.argv) != 3:
        print("Error : Please provide a correct file name and word")
        print("Usage: python script.py <filename1> <word>")
        return
    
    FileName = sys.argv[1]
    word = sys.argv[2]

    SpecificWord = CheckWord(FileName, word)

    if SpecificWord:
        print(f"The Word {word} is found in {FileName}")

    else:
        print(f"The Word {word} is not found in {FileName}")

if __name__ == "__main__":
    main()

"""
Input:
Demo.txt Marvellous
Expected Output:
Display whether the word Marvellous is found in Demo.txt or not.
"""