"""1to10Recurssion """
def print1to10(n):
    if(n>10):
        return
    print(n)
    print1to10(n+1)
 
print1to10(1)

"""FactorialRecurssion""" 
def fac(n):
    if(n==1 or n==0):
        return 1
    return n * fac(n-1)
n = int(input("Enter your number : "))
print ("Factorial of", n, "is : ",fac(n))
