""" 4. Write a lambda function using reduce() which accepts a list of numbers and returns the addition of
all elements.
"""
from functools import reduce

AdditionOfElements = lambda No1, No2 : No1 + No2

def main():
    Data = [11,21,51,101]

    RData = reduce(AdditionOfElements, Data)

    print("Original Data :", Data)
    print("Addition of All Elements :", RData)

if __name__ == "__main__":
    main()