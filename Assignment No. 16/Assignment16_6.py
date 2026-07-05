""" 6.Write a program which accept number from user and check whether that number is positive or
negative or zero.
"""
def NumberCheck(No):
    if No > 0 :
        print("Number is Positive")

    elif No < 0:
        print("Number is Negative")

    else:
        print("Number is Zero")

def main():
    Value = int(input("Enter number :"))
    Ret = NumberCheck(Value)

if __name__ =="__main__":
    main()
    
""" 
Input : 11 Output : Positive Number
Input : -8 Output : Negative Number
Input : 0 Output : Zero
"""