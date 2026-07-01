""" 1. Write a program which accepts length and width of rectangle and prints area.
"""

def AreaOfRectangular(Length, Width):
    Area  = Length * Width 
    print("Area of Rectangular :", Area)

def main():
    Value1 = int(input("Enter Length :"))
    Value2 = int(input("Enter Width :"))

    Ret = AreaOfRectangular(Value1, Value2)

if __name__ == "__main__":
    main()