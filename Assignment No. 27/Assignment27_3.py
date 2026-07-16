""" 3: Write a Python program to implement a class named Numbers with the following
specifications:
• The class should contain one instance variable:
◦ Value
• Define a constructor (__init__) that accepts a number from the user and initializes Value.
• Implement the following instance methods:
◦ ChkPrime() – returns True if the number is prime, otherwise returns False
◦ ChkPerfect() – returns True if the number is perfect, otherwise returns False
◦ Factors() – displays all factors of the number
◦ SumFactors() – returns the sum of all factors
• Create multiple objects and call all methods.
"""

class Numbers:
    def __init__(self, Value):
        self.Value = int(input(Value))

    def ChkPrime(self):
        if self.Value <= 1:
            return False
        for i in range(2, int(self.Value ** 0.5) + 1):
            if self.Value % i == 0:
                return False
        return True
    
    def ChkPerfect(self):
        if self.Value <= 1:
            return False
        
        PerfectNumber = sum(i for i in range(1, self.Value) if self.Value % i == 0)
        return PerfectNumber == self.Value
    
    def Factors(self):
        FactorList = [i for i in range(1, self.Value + 1) if self.Value % i == 0]
        print(f"Factors of {self.Value} :{FactorList}")
    
    def SumFactors(self):
        return sum(i for i in range(1, self.Value + 1) if self.Value % i == 0)
    
print("_____Object 1_____")
Obj1 = Numbers("Enter a number :")

Obj1.ChkPrime()
print(f"The number is prime :{Obj1.ChkPrime()}")

Obj1.ChkPerfect()
print(f"The number is perfect :{Obj1.ChkPerfect()}")

Obj1.Factors()

Obj1.SumFactors()
print(f"The sum of factors is :{Obj1.SumFactors()}")

print("_____Object 2_____")
Obj2 = Numbers("Enter a number :")

Obj2.ChkPrime()
print(f"The number is prime :{Obj2.ChkPrime()}")

Obj2.ChkPerfect()
print(f"The number is perfect :{Obj2.ChkPerfect()}")

Obj2.Factors()

Obj2.SumFactors()
print(f"The sum of factors is :{Obj2.SumFactors()}")

            

        