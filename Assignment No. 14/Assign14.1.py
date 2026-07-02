""" 1. Write a lambda function which accepts one number and returns square of that number.
"""

def main():
    SquareNumber = lambda No : No * No

    No = int(input("Enter number :"))
    
    square = SquareNumber(No)
    print("Square is :", square)

if __name__ == "__main__":
    main()