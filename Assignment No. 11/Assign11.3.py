""" 3. Write a program which accepts one number and prints sum of digits.
"""

def Count(No):
    No = abs(No)

    Sum = 0
    while No > 0:
        Ans = No % 10
        Sum += Ans
        No //= 10
    return Sum


def main():
    Value1 = int(input("Enter number :"))
    Ret = Count(Value1)
    print(Ret)

if __name__ == "__main__":
    main()

# Input: 123
# Output: 6

