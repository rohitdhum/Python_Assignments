""" 2: Write a Python program to implement a class named BankAccount with the following
requirements:
• The class should contain two instance variables:
◦ Name (Account holder name)
◦ Amount (Account balance)
• The class should contain one class variable:
◦ ROI (Rate of Interest), initialized to 10.5
• Define a constructor (__init__) that accepts Name and initial Amount.
• Implement the following instance methods:
◦ Display() – displays account holder name and current balance
◦ Deposit() – accepts an amount from the user and adds it to balance
◦ Withdraw() – accepts an amount from the user and subtracts it from balance
(Ensure withdrawal is allowed only if sufficient balance exists)
◦ CalculateInterest() – calculates and returns interest using formula:
Interest = (Amount * ROI) / 100
• Create multiple objects and demonstrate all methods.
"""

class BankAccount:
    # Class Variable
    ROI = 10.5

    def __init__(self, Name, Amount):
        self.Name = Name
        self.Amount = float(Amount)

    def Display(self):
        print(f"Account holder name {self.Name}\nCurrent balance {self.Amount}")

    def Deposit(self):
        Value = float(input("Enter the amount deposit :"))
        self.Amount += Value
        print("Amount is successfully deposited", Value)

    def Withdraw(self):
        Value = float(input("Enter the withraw amount :"))
        if Value > self.Amount:
            print("Error : Insufficient Balance")
        else:
            self.Amount -= Value
            print("Amount is withraw succussesfully", Value)

    def CalculateInterest(self):
        Interest = (self.Amount * BankAccount.ROI) / 100
        return Interest
    
print("_____Creating Account 1_____")
Obj1 = BankAccount("Rohit Dhumal", 5000)
Obj1.Display()

Obj1.Deposit()
Obj1.Display()

Obj1.Withdraw()
Obj1.Display()

Interest = Obj1.CalculateInterest()
print(f"Rate of interest is :{BankAccount.ROI}%, ROI :{Interest}")

print("_____Creating Account 2_____")
Obj2 = BankAccount("Sainath Gije", 7000)
Obj2.Display()

Obj2.Deposit()
Obj2.Display()

Obj2.Withdraw()
Obj2.Display()

Interest = Obj2.CalculateInterest()
print(f"Rate of interest is :{BankAccount.ROI}%, ROI :{Interest}")


