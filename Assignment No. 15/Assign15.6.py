""" 6. Write a lambda function using reduce() which accepts a list of numbers and returns the minimum
element.
"""
from functools import reduce 

MinimumElement = lambda No1, No2 : No1 if No1 < No2 else No2    # min(No1, No2) -> Allowed

def main():
    Data  = [1,2,25,40,60,70,100]

    RData = reduce(MinimumElement, Data)

    print("Original Data :", Data)
    print("Minimum Element :", RData)

if __name__ == "__main__":
    main()