""" 6. Write a lambda function which accepts one number and returns True if number is odd
otherwise False.
"""

def main():
    OddNumber = lambda No : No % 2 == 1 

    Value1 = int(input("Enter Number :"))
    Ret = OddNumber(Value1)
    print(Ret)

if __name__ == "__main__":
    main()