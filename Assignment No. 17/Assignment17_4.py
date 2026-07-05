""" 4.Write a program which accept one number form user and return addition of its factors.
"""

def Addition(No):
    Add = 0

    for i in range(1, No):
        if No % i == 0:
            Add = Add + i

    return Add

def main():
    Value = int(input("Enter Number :"))
    Ret = Addition(Value)
    print("Addition of its Factors is :", Ret)

if __name__ == "__main__":
    main()

# Input : 12         Output : 16 (1+2+3+4+6)