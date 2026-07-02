""" 9. Write a lambda function which accepts two numbers and returns multiplication.
"""

def main():
    Multiplication = lambda No1, No2 : No1 * No2

    Value1 = int(input("Enter first number :"))
    Value2 = int(input("Enter second number :"))

    Ret = Multiplication(Value1, Value2)
    print("Multiplicatin is :", Ret)

if __name__ == "__main__":
    main()