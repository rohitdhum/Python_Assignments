""" 9. Write a program which accept number from user and return number of digits in that number.
"""

def Digits(No):
    No = abs(No)

    count = 0

    if No == 0:
        return 1
    
    while No > 0:
        count += 1
        No //= 10

    return count

def main():
    Value = int(input("Enter Number :"))

    Ret = Digits(Value)

    print(f"Output :{Ret}")

if __name__ == "__main__":
    main()

# Input : 5187934        Output : 7