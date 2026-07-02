""" 5. Write a lambda function which accepts one number and returns True if number is even
otherwise False.
"""

def main():
    EvenNumber = lambda No : No % 2 == 0

    Value1= int(input("Enter number :"))
    Ret  = EvenNumber(Value1)
    print(Ret)

if __name__ == "__main__":
    main()