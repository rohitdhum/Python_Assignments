""" 4. Write a program which accepts one number and prints all even numbers till that
number.
"""
def Even(No):
    for i in range(1, No+1):
        if(i % 2 == 0):
            print(i, end = " ")
        
def main():
    Value1 = int(input("Enter number :"))

    Ret = Even(Value1)

if __name__ == "__main__":
    main()

# Input: 10
# Output: 2 4 6 8 10