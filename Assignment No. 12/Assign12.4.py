""" 4. Write a program which accepts one number and prints that many numbers starting
from 1.
"""
def Number(No):
    for i in range (1,No+1):
        print(i, end = " ")

def main():
    Value1 = int(input("Enter number :"))    
    Ret  = Number(Value1)

if __name__ == "__main__":
    main()

# Input: 5
# Output: 1 2 3 4 5