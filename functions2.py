"""Write a Python program to create a calculator. Create individual functions for different operators
 - addition, subtraction, division, multiplication and return the output value."""

def sub(a,b):
    return a - b

def add(a,b):
    return a + b

def mul(a,b):
    return a * b

def div(a,b):
    return a / b

def squ(a):
    return a**2
s = sub(8,10)
a = add(5,13)
m = mul(6,4)
d = div(26,3)
q = squ(18)
print(s,a,m,d,q)