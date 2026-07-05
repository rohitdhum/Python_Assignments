""" 1.Create on module named as Arithmetic which contains 4 functions as Add() for addition, Sub()
for subtraction, Mult() for multiplication and Div() for division. All functions accepts two
parameters as number and perform the operation. Write on python program which call all the
functions from Arithmetic module by accepting the parameters from user.
"""
# Arithematic.py -> Module 

def Add(No1, No2):
    return (No1 + No2)

def Sub(No1, No2):
    return (No1 - No2)

def Div(No1, No2):
    if No2 == 0:
        return ("Error : Division by Zero")
    return (No1 / No2)

def Mult(No1, No2):
    return (No1 * No2)
