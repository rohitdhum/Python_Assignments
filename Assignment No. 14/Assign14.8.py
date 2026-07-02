"""  8. Write a lambda function which accepts two numbers and returns addition.
"""

def main():
    Addition = lambda No1, No2 : No1 + No2

    Value1 = int(input("Enter first number :"))
    Value2 = int(input("Enter second number :"))

    Ret  = Addition(Value1, Value2)
    print("Addition is :", Ret)

if __name__ == "__main__":
    main()