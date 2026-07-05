""" 6. Write a program which accept one number and display below pattern.
"""

def  Display(No):
    for i in range(No,0,-1):
        print("*" * i)

def main():
    Value = int(input("Enter Number :"))

    Ret = Display(Value)

if __name__ == "__main__":
    main()

""" 
Input : 5
Output :
* * * * *
* * * *
* * *
* *
*
"""