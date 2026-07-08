""" 5.Write a program which contains filter(), map() and reduce() in it. Python application which
contains one list of numbers. List contains the numbers which are accepted from user. Filter
should filter out all prime numbers. Map function will multiply each number by 2. Reduce will
return Maximum number from that numbers. (You can also use normal functions instead of
lambda functions).
""" 

from functools import reduce

def Prime(No):
    if No < 2:
        return False
    for i in range(2, int(No ** 0.5) + 1):
        if No % i == 0:
            return False
    return True

def Multiply(No):
    return No * 2

def MaximumNumber(No1, No2):
    return No1 if No1 > No2 else No2            # max(No1, NO2) -> Allowed
 
def main():
    Data = [2, 70 , 11, 10, 17, 23, 31, 77]
    print("Input Data =", Data)

    FData = list(filter(Prime, Data))
    print("List after filter =", FData)

    MData= list(map(Multiply, FData))
    print("List after map =", MData)

    RData = reduce(MaximumNumber, MData)
    print("Output of reduce =", RData)

if __name__ == "__main__":
    main()

"""
Input List = [2, 70 , 11, 10, 17, 23, 31, 77]
List after filter = [2, 11, 17, 23, 31]
List after map = [4, 22, 34, 46, 62]
Output of reduce = 62
"""