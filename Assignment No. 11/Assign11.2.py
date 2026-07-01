""" 2.Write a program which accepts one number and prints count of digits in that number.
"""

def Count(No):
    No = abs(No)

    if No  == 0:
        return 1
    
    count = 0
    while No > 0:
        count +=1
        No //= 10
    return count

def main():
    Value1 = int(input("Enter Number :"))
    Ret = Count(Value1)
    print(Ret)

if __name__ == "__main__":
    main()

# Input: 7521
# Output: 4