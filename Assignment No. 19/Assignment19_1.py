""" 1.Write a program which contains one lambda function which accepts one parameter and return
power of two.
"""

Power = lambda No: 2 ** No 

def main():
    Value = int(input("Enter Number :"))

    Ret = Power(Value)

    print("Output :", Ret)

if __name__ == "__main__":
    main()

# Input : 4       Output : 16
# Input : 6       Output : 64