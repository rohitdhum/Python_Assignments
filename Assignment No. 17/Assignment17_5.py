"""5.Write a program which accept one number for user and check whether number is prime or not.
"""

def PrimeNumber(No):
    if No <= 1:
        return False
    
    for i in range(2, int(No ** 0.5) + 1):
        if No % i == 0:
            return False
        
    return True

def main():
    Value = int(input("Enter Number :"))

    if PrimeNumber(Value):
        print(" It is Prime Number")

    else:
        print("It is not Prime Number ")

if __name__ == "__main__":
    main()

# Input : 5          Output : It is Prime Number