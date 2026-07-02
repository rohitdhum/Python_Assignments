""" 7. Write a lambda function using filter() which accepts a list of strings and returns a list of strings
having length greater than 5.
"""

ListOfString = lambda No : len(No) > 5 

def main():
    Data = ["Python", "Rohit", "Ram", "Ganesh", "Bhalchandra"]

    FData = list(filter(ListOfString, Data))

    print("Original Data :", Data)
    print("List of strings having length is grater than 5 :", FData)

if __name__ == "__main__":
    main()