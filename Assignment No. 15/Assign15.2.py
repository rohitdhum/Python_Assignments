""" 2. Write a lambda function using filter() which accepts a list of numbers and returns a list of even
numbers.
"""

EvenNumber = lambda No : No % 2 == 0

def main():
    Data = [1,2,3,4,5,6,7,8,9,10,15,20,25]

    FData = list(filter(EvenNumber, Data))

    print("Original Data :", Data)
    print("Even Numbers :", FData)

if __name__ == "__main__":
    main()