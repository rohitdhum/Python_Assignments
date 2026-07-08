""" 2.Write a program which contains one lambda function which accepts two parameters and return
its multiplication.
"""

Multiplication = lambda No1, No2 : No1 * No2

def main():
    Value1 = int(input("Enter First Number :"))
    Value2 = int(input("ENter second number :"))

    Ret = Multiplication(Value1, Value2)

    print("Output is :", Ret)

if __name__ == "__main__":
    main()

# Input : 4 3      Output : 12
# Input : 6 3      Output : 18