""" 1. Write a program which accepts one number and checks whether it is prime or not.
"""

def Prime(No):
    if No <= 1:
        return False
    
    for i in range(2, int(No**0.5)+1):
        if No % i == 0:
            return False
    return True

def main():
    Value1 = int(input("Enter number :"))

    if Prime(Value1):
        print("Prime Number")

    else:
        print("Not a Prime Number :")

if __name__ == "__main__":
    main()

# Input: 11
# Output: Prime Number