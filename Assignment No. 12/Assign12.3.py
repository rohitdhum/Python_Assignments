""" 3. Write a program which accepts two numbers and prints addition, subtraction,
multiplication and division.
"""
def Numbers(No1, No2):

    print("Addition is :",No1 + No2)
    print("Substraction is :",No1 - No2)
    print("Multiplication is :",No1 * No2)
    print("Division is :",No1 / No2)

def main():
    Value1 = float(input("Enter first number :")) 
    Value2 = float(input("Enter second number :"))

    Ret = Numbers(Value1, Value2)

if __name__ == "__main__":
    main()