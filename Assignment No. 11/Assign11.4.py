""" 4. Write a program which accepts one number and prints reverse of that number.
"""

def ReverseNumber(No):
    Negative = No < 0
    No = abs(No)

    Num = 0
    while No > 0:
        Ans = No % 10
        Num = (Num * 10) + Ans
        No = No // 10
    return -Num if Negative else Num
    
def main():
    Value1 = int(input("Enter number :"))
    Ret  = ReverseNumber(Value1)
    print(Ret)

if __name__ == "__main__":
    main()

# Input: 123
# Output: 321