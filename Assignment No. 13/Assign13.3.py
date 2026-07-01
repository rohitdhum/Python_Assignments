""" 3. Write a program which accepts one number and checks whether it is perfect number or
not.
"""

def PerfectNUmber(No):
    Ans = 0

    for i in range(1,No):
        if No % i == 0:
            Ans += i
    
    if Ans == No:
        print("Perfect Number")
    else:
        print("Not a Perfect Number")

def main():
    Value1 = int(input("Entwer Number :"))
    Ret = PerfectNUmber(Value1)

if __name__ == "__main__":
    main()

# Input: 6
# Output: Perfect Number