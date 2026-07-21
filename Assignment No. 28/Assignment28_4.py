""" Q4) Copy File Contents into Another File
Problem Statement:
Write a program which accepts two file names from the user.
• First file is an existing file
• Second file is a new file
Copy all contents from the first file into the second file.
"""
import os
import sys

def Files(FileName1, FileName2):
   if not os.path.exists(FileName1):
      print("Error File is not present")
      return 
   
   fobj1 = open(FileName1, "r")
   fobj2 = open(FileName2, "w")

   for Line in fobj1:
      fobj2.write(Line)

   fobj1.close()
   fobj2.close()
   return

def main():
   if len(sys.argv) != 3:
      print("Error : Please provide two file name")
      print("Usage: python script.py <filename1> <FileName2>")
      return
    
   FileName1 = sys.argv[1]
   FileName2 = sys.argv[2]

   Files(FileName1, FileName2)

   print(f"Content of {FileName1} copied into {FileName2}")
 
if __name__ == "__main__":
   main()

"""
Input:
ABC.txt Demo.txt

Expected Output:
Contents of ABC.txt copied into Demo.txt.
"""