""" 4. Write a program which accepts one number and prints binary equivalent.
"""

def BinaryEquivalent(No):
    if No ==  0:
        return "0"
    
    Binary = " "

    while No > 0:
        Remainder = No % 2
        Binary = str(Remainder) + Binary     
        No = No // 2
    return Binary  

def main():
    while True:
        Value1 = input("Enter a number :")
        if Value1.lower() == "exit":
            break

        Number  = int(Value1)
        Ret  = BinaryEquivalent(Number)
        print("Binary Equivalent :", Ret)

if __name__ == "__main__":
    main()