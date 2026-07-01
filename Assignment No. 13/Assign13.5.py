""" 5. Write a program which accepts marks and displays grade.
Condition Example:
"""

def Grade(Marks):
    if Marks >= 75:
        print("Your grade is Distiction")
    
    elif Marks >= 60:
        print("Your grade is Fisrt Class")

    elif Marks >= 50:
        print("Your grade is Second Class")

    else:
        print("You are Fail")

def main():
    No = int(input("Enter The Grade :"))

    Ret = Grade(No)

if __name__ == "__main__":
    main()

# • ≥ 75 → Distinction
# • ≥ 60 → First Class
# • ≥ 50 → Second Class
# • < 50 → Fail