""" 3. Write a program which accepts one number and prints factorial of that number.
"""

def Factorial(No):
    Ans = 1

    for i in range(1, No+1):
        Ans *=i
    return Ans

def main():
    Value1 = int(input("Enter number :"))

    Ret = Factorial(Value1)

    print(Ret)

if __name__ == "__main__":
    main()
    
# Input: 5
# Output: 120