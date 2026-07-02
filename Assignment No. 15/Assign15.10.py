""" 10.Write a lambda function using filter() which accepts a list of numbers and returns the count of even
numbers.
"""

CountEvenNumber = lambda No : No % 2  == 0

def main():
    Data = [1,2,3,4,5,6,7,8,9,10]

    FData = len(list(filter(CountEvenNumber, Data)))

    print("Original Data :", Data)
    print("Count of even numbers :", FData)

if __name__ == "__main__":
    main()