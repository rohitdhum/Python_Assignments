""" 8. Write a lambda function using filter() which accepts a list of numbers and returns a list of numbers
divisible by both 3 and 5.
"""

DivisibleNumber = lambda No : No % 3 == 0 and No % 5 == 0

def main():
    Data = [2,3,5,12,15,10,13,18,45]

    FData = list(filter(DivisibleNumber, Data))

    print("Original Data", Data)
    print("Divisible by 3 And 5 Elemets :", FData)

if __name__ == "__main__":
    main()