""" 7. Write a lambda function which accepts one number and returns True if divisible by 5.
"""

def main():
    TrueValue = lambda No : No % 5 == 0

    Value1  = int(input("Enter Number :"))
    Ret = TrueValue(Value1)
    print(Ret)

if __name__ == "__main__":
    main()