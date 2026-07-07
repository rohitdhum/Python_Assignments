""" 5.Write a program which accept N numbers from user and store it into List. Return addition of all
prime numbers from that List. Main python file accepts N numbers from user and pass each
number to ChkPrime() function which is part of our user defined module named as
MarvellousNum. Name of the function from main python file should be ListPrime().
"""

import MarvellousNum

def ListPrime(No):

    SumOfPrime = 0

    for i in No:
        if MarvellousNum.ChkPrime(i):
            SumOfPrime += i

    return SumOfPrime

def main():
    Value = int(input("Number of Elements :"))

    InputElements = input("Input Elements :")

    List = [int(x) for x in InputElements.split()]

    if len(List) != Value:
        print(f"Warning : Expected {Value} elements, but got {len(List)}")

    Ret = ListPrime(List)

    print("Output", Ret)


if __name__ == "__main__":
    main()

"""
Input : Number of elements : 11
Input Elements : 13 5 45 7 4 56 10 34 2 5 8
Output : 32 (13 + 5 + 7 +2 + 5)
"""