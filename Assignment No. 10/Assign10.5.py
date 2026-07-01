""" 5.Write a program which accepts one number and prints all odd numbers till that number.
"""

def Odd(No):
    for i in range(1,No+1):
        if(i %2 == 1):
            print(i, end = " ")

def main():
    Value1 = int (input("Enter number"))

    Ret = Odd(Value1)

if __name__ == "__main__":
    main()