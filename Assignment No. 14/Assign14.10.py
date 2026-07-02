""" 10. Write a lambda function which accepts three numbers and returns largest number.
"""

def main():
    LargestNumber  = lambda No1, No2, No3 : max(No1, No2, No3)

    Value1 = int(input("Enter first number :"))
    Value2 = int(input("Enter second number :"))
    Value3 = int(input("Enter thirsd number :"))

    Ret = LargestNumber(Value1, Value2, Value3)

    print("Largest Number is :", Ret)

if __name__ == "__main__":
    main()