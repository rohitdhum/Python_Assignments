""" 3. Write a program which accept one number from user and return its factorial.
"""

def Factorial(No):
    Fact = 1

    for i in range(1, No+1):
        Fact = Fact * i
    return Fact
    
def main():
    Value = int(input("Enter Number :"))
    Ret = Factorial(Value)
    print("Factorial is :", Ret)

if __name__ == "__main__":
    main()

# Input : 5             Output : 120