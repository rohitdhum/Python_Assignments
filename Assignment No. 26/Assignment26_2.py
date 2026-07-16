""" 2: Write a Python program to implement a class named Circle with the following
requirements:
• The class should contain three instance variables: Radius, Area, and Circumference.
• The class should contain one class variable named PI, initialized to 3.14.
• Define a constructor (__init__) that initializes all instance variables to 0.0.
• Implement the following instance methods:
◦ Accept() – accepts the radius of the circle from the user.
◦ CalculateArea() – calculates the area of the circle and stores it in the Area variable.
◦ CalculateCircumference() – calculates the circumference of the circle and stores it in
the Circumference variable.
◦ Display() – displays the values of Radius, Area, and Circumference.
• Create multiple objects of the Circle class and invoke all the instance methods for each object.
"""

class Circle:
    # Class variable
    PI = 3.14

    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0

    def Accept(self):
        self.Radius = float(input("Enter the radius :"))

    def CalculateArea(self):
        self.Area = Circle.PI * (self.Radius ** 2)

    def CalculateCircumference(self):
        self.Circumference = 2 * Circle.PI * self.Radius

    def Display(self):
        print("Value of Radius :", self.Radius)
        print("Value of Area :", self.Area)
        print("Value of Circumference :", self.Circumference)

print("_____Object 1_____")
Obj1 = Circle()
Obj1.Accept()
Obj1.CalculateArea()
Obj1.CalculateCircumference()
Obj1.Display()

print("_____Object 2_____")
Obj2 = Circle()
Obj2.Accept()
Obj2.CalculateArea()
Obj2.CalculateCircumference()
Obj2.Display()





