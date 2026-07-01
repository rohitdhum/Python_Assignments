""" 1. Write a program which accepts one character and checks whether it is vowel or
consonant.
"""
def Character(char):
    char = char.lower() 

    if char in ('a','e','i','o','u'):
        print("Vowel")
    else:
        print("Consonant")

def main():
    Value1 = input("Enter a Letter :")
    
    if len(Value1) == 1:
        Character(Value1)
    else:
        print("Enetr one character")
        
if __name__ == "__main__":
    main()

# Input: a
# Output: Vowel