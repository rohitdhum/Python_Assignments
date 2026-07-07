""" 4.Write a program which accept N numbers from user and store it into List. Accept one another
number from user and return frequency of that number from List.
"""

def Frequency(Number, Target):
    count = 0

    for i in Number:
        if i  == Target:
            count += 1
    return count

def main():
    Value = int(input("Number of Elements :"))

    InputElements = input("Input Elements :")

    List = [int(x) for x in InputElements.split()][:Value]

    SearchElements = int(input("Element to search :"))

    Ret = Frequency(List, SearchElements)

    print(f"Output Frequency {Ret}")

if __name__ == "__main":
    main()

"""
Input : Number of elements : 11
Input Elements : 13 5 45 7 4 56 5 34 2 5 65
Element to search : 5
Output : 3
"""