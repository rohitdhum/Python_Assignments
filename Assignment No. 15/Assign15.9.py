""" 9. Write a lambda function using reduce() which accepts a list of numbers and returns the product of all
elements.
"""

from functools import reduce

ProductOfElements = lambda No1, No2 : No1 * No2

def main():
    Data = [1,2,3,4,5]

    RData = reduce(ProductOfElements, Data)

    print("Oroginal Data :", Data)
    print("Product of all Elements :", RData)

if __name__ == "__main__":
    main()

