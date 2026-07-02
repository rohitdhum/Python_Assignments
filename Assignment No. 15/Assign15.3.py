""" 3. Write a lambda function using filter() which accepts a list of numbers and returns a list of odd
numbers.
"""

OddNumber = lambda No : No % 2 == 1

def main():
    Data = [1,2,3,4,5,6,7,8,9,11,13,15,18,20]

    FData = list(filter(OddNumber, Data))

    print("Original Data :", Data)
    print("Odd Numbers :", FData)

if __name__ == "__main__":
    main()