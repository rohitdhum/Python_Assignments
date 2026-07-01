""" 2. Write a program which accepts one number and prints its factors.
"""

def Factors(No):
    for i in range (1, No+1):
        if No % i == 0:
            print(i, end = " ")

def main():
    Num = int(input("Enter number :"))
    Factors(Num)

if __name__ == "__main__":
    main()
    
# Input: 12
# Output: 1 2 3 4 6 12