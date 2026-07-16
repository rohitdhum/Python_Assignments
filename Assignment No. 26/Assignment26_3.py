""" 3: Write a Python program to implement a class named Arithmetic with the following
characteristics:
• The class should contain two instance variables: Value1 and Value2.
• Define a constructor (__init__) that initializes all instance variables to 0.
• Implement the following instance methods:
◦ Accept() – accepts values for Value1 and Value2 from the user.
◦ Addition() – returns the addition of Value1 and Value2.
◦ Subtraction() – returns the subtraction of Value1 and Value2.
◦ Multiplication() – returns the multiplication of Value1 and Value2.
◦ Division() – returns the division of Value1 and Value2 (handle division by zero
properly).

• Create multiple objects of the Arithmetic class and invoke all the instance methods.
"""

class Arithematic:

    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0

    def Accept(self):
        self.Value1 = float(input("Enter first number :"))
        self.Value2 = float(input("Enter second number :"))

    def Addition(self):
        return self.Value1 + self.Value2
    
    def Substraction(self):
        return self.Value1 - self.Value2
    
    def Multipliocation(self):
        return self.Value1 * self.Value2
    
    def Division(self):
        if self.Value2 == 0:
            return "Error : Division by zero not allowed"
        return self.Value1 / self.Value2
        
print("_____Object 1_____")
Obj1 = Arithematic()
Obj1.Accept()

Ret = Obj1.Addition()
print("Addition is :", Ret)

Ret = Obj1.Substraction()
print("Substraction is :", Ret)

Ret = Obj1.Multipliocation()
print("Multiplication is :", Ret)

Ret = Obj1.Division()
print("Division is :", Ret)

print("_____Object 2_____")
Obj2 = Arithematic()
Obj2.Accept()

Ret = Obj2.Addition()
print("Addition is :", Ret)

Ret = Obj2.Substraction()
print("Substraction is :", Ret)

Ret = Obj2.Multipliocation()
print("Multiplication is :", Ret)

Ret = Obj2.Division()
print("Division is :", Ret)


        