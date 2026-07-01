""" 2. Write a program which accepts radius of circle and prints area of circle.
"""

def RadiusOfCircle(Radius):
    PI = 3.14
    Radius = PI * (Radius* Radius)
    print("Area of Circle :", Radius)

def main():
    Value1 = float(input("Enter Radius :"))

    Ret  = RadiusOfCircle(Value1)

if __name__ == "__main__":
    main()