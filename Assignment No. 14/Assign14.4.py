""" 4. Write a lambda function which accepts two numbers and returns minimum number.
"""

def main():
    MinimumNumber = lambda No1, No2 : No1 if No1 < No2 else No2
    Value1 = int(input("Enter first number :"))
    Value2 = int(input("Enter second number :"))

    Ret = MinimumNumber(Value1, Value2)
    print("Minimum number is :", Ret)

if __name__ == "__main__":
    main()