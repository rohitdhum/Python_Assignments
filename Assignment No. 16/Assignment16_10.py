""" 10. Write a program which accept name from user and display length of its name.
"""

def Length(Name):
    return len(Name)

def main():
    Display = input("Input :")

    Ret = Length(Display)

    print("Output :", Ret)

if __name__ == "__main__":
    main()
    
# Input : Marvellous         Output : 10