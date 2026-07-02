""" 1. Write a lambda function using map() which accepts a list of numbers and returns a list of squares of
each number.
"""

Square = lambda No : No * No 

def main():
    Data  = [1,2,3,4,5,6,7,8,9,10]

    MData = list(map(Square, Data))

    print("Original List :", Data)
    print("Square List :", MData)

if __name__ == "__main__":
    main()