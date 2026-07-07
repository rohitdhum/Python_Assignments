""" 2.Write a program which accept N numbers from user and store it into List. Return Maximum
number from that List.
""" 

def Maximum_Number(No):
    if not No:
        return None
    
    maximum = No[0]

    for i in No:
        if i > maximum:
            maximum = i
    return maximum

def main():
    Value = int(input("Number of Elements :"))
     
    Input_Value = input("Input Elemnents :")

    List = [int(x) for x in Input_Value.split()]

    Ret = Maximum_Number(List) 

    print("Output", Ret)

if __name__ == "__main__":
    main()
    
"""
Input : Number of elements : 7
Input Elements : 13 5 45 7 4 56 34
Output : 56
"""