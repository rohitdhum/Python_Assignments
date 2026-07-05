""" 7. Write a program which contains one function that accept one number from user and returns
true if number is divisible by 5 otherwise return false.
"""

def Divisible(No):
    if No % 5 == 0:
        print(True)
    
    else:
        print("False")

def main():
    Value = int(input("Enter Number :"))
    Ret = Divisible(Value)

if __name__ == "__main__":
    main() 

# Input : 8 Output : False
# Input : 25 Output : True