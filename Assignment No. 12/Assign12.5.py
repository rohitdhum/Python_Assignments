""" 5. Write a program which accepts one number and prints that many numbers in reverse
order.
"""

def Reverse(No):
    for i in range(No, 0, -1):
        print(i, end = " ")

def main():
    Value1 = int(input("Enter number :"))
    Ret = Reverse(Value1)

if __name__ == "__main__":
    main()
    
# Input: 5
# Output: 5 4 3 2 1