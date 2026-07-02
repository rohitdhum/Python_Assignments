""" 2. Write a lambda function which accepts one number and returns cube of that number. 
"""

def main():
    CubeNumber = lambda No : No * No * No

    No  = int(input("Enter Number :"))
    cube = CubeNumber(No)
    print("Cube is :", cube)

if __name__ == "__main__":
    main()