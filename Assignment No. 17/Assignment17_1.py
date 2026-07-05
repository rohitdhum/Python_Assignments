""" 1.Create on module named as Arithmetic which contains 4 functions as Add() for addition, Sub()
for subtraction, Mult() for multiplication and Div() for division. All functions accepts two
parameters as number and perform the operation. Write on python program which call all the
functions from Arithmetic module by accepting the parameters from user.
"""

import Arithematic

def main():
    No1 = int(input("Enter First Number :"))
    No2 = int(input("Enter Second Number :"))

    print(f"Addition is :{Arithematic.Add(No1, No2)}")
    print(f"Substraction is :{Arithematic.Sub(No1,No2)}")
    print(f"Division is :{Arithematic.Div(No1, No2)}")
    print(f"Multiplication is :{Arithematic.Mult(No1, No2)}")
    
if __name__ == "__main__":
    main()