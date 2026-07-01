""" 2. Write a program which accepts one number and prints sum of first N natural numbers.
"""

def SumOfNaturalNumber(No):
    Sum = 0

    for i in range(1,No+1):
        Sum +=i
    return Sum

def main():
    Value1 = int(input("Enter number :"))
    
    Ret = SumOfNaturalNumber(Value1)

    print(Ret)

if __name__ == "__main__":
    main()

# Input: 5
# Output: 15