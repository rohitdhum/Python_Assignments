""" 8. Write a program which accept number from user and print that number of “*” on screen.
"""

def Star(No):
    
    for i in range(No):
        print("*", end = " ")

def main():
    Value =int(input("Enter number :"))
    Ret = Star(Value)

if __name__ == "__main__":
    main()

# Input : 5 Output : * * * * *