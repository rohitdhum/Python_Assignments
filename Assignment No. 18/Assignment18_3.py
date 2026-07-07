""" 3.Write a program which accept N numbers from user and store it into List. Return Minimum
number from that List.
"""

def Minimum_Number(No):
    if not No:
        return None
    
    minimum = No[0]

    for i in No:
        if i < minimum:
            minimum = i
    return minimum

def main():
    Value = int(input("Number of Elemnents :"))

    Input_Value = input("Input Elements :")

    List = [int(x) for x in Input_Value.split()]
    Ret = Minimum_Number(List)

    print("Output :", Ret)

if __name__ == "__main__":
    main()

"""
Input : Number of elements : 4
Input Elements : 13 5 45 7
Output : 5
"""