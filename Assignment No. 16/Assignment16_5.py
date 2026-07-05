""" 5.Write a program which display 10 to 1 on screen.
"""
def Display():
    No = 10

    for i in range(No, 0, -1):
        print(i, end = " ")

def main():
    Display()

if __name__ == "__main__":
    main()
# Output : 10 9 8 7 6 5 4 3 2 1