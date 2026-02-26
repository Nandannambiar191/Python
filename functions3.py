"""
factorial of n
"""
def factorial(v):
    if v == 1:
        return v
    else:
        return v * factorial(v-1)
d = int(input("Enter a Number"))
if d < 0:
    print("Factorial of negative number is not possible")
elif d == 0:
    print("Factorial of 0 is 1")
else:
    print(factorial(d))
    