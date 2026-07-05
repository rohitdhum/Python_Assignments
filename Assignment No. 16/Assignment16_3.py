""" 3. Write a program which contains one function named as Add() which accepts two numbers
from user and return addition of that two numbers.
"""

def Add(No1, No2):
    Addition = No1 + No2
    return Addition

def main():
    Value1 = int(input("Enter first number :"))
    Value2 = int(input("Enter second number :"))

    Ret = Add(Value1, Value2)

    print(f"Addition is :", Ret)

if __name__ == "__main__":
    main()

# Input : 11 5          Output : 16