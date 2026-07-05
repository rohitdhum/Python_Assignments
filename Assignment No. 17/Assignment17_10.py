""" 10. Write a program which accept number from user and return addition of digits in that number.
"""

def SumOfDigits(No):
    No = abs(No)

    count = 0

    while No > 0:
        count += No % 10
        No //= 10
 
    return count

def main():
    Value = int(input("Enter Number :"))

    Ret = SumOfDigits(Value)

    print(f"Output :{Ret}")

if __name__ == "__main__":
    main()

# Input : 5187934      Output : 37