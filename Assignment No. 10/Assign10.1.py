""" 1. Write a program which accepts one number and prints multiplication table of that
number.
"""

def Table(No):
    for i in range(1,11):
        print(No * i, end = " ")

def main():
    Value1 = int(input("Enter number :"))
    Ret = Table(Value1)

if __name__ == "__main__":
    main()

# Input: 4
# Output: 4 8 12 16 20 24 28 32 36 40
