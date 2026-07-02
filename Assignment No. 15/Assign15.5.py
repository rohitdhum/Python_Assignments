""" 5. Write a lambda function using reduce() which accepts a list of numbers and returns the maximum
element.
"""
from functools import reduce

MaximumElements = lambda No1, No2 : No1 if No1 > No2 else No2    # max(No1, No2) -> Allowed
def main():
    Data = [10,20,30,40,50,60,70,80,90,100]

    RData = reduce(MaximumElements, Data)

    print("Original Data :", Data)
    print("Maximum Element :", RData)

if __name__ == "__main__":
    main()