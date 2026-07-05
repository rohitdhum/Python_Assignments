""" 9. Write a program which display first 10 even numbers on screen.
"""

def Even(No):
    for i in range(1,21):
        if i % 2 == 0:
            print(i, end = " ")
    
def main():
    Even(20)

if __name__ =="__main__":
    main()

# Output : 2 4 6 8 10 12 14 16 18 20