""" 1.Write a program which accept N numbers from user and store it into List. Return addition of all
elements from that List.
"""

def Addition(No):
    return sum(No)
 
def main():
    Num = int(input("Number of elements :"))
    print("Input Elements :")

    Number_List = [int(x) for x in input().split()] [:Num]

    Ret = Addition(Number_List)
    print(f"Output :{Ret}")

if __name__ == "__main__":
    main()

"""
Input : Number of elements : 6
Input Elements : 13 5 45 7 4 56
Output : 130
"""