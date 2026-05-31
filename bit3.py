""" 2EqualNumbers"""
# Program to check if user input numbers are equal without using any comparison operator. 
 
def checkIfSame(number1, number2):
 
# User XOR operator as a^a is always 0 
 if ((number1 ^ number2) != 0):
    print("Numbers are not equal")
 else:
    print("Both numbers are equal")
 
# Taking input
number1 = int(input("Enter first number to compare : "))
number2 = int(input("Enter second number to compare : "))
 
checkIfSame(number1, number2)

"""OneOddOccuring """ 
# Program to find the element not making a pair
 
# Function to calculate the number that is odd occurring 
 
def OddOccurring(arr):
 
    # Initialize result
    res = 0
     
    # Traverse the array
    for element in arr:
        # XOR with the result
        res = res ^ element
 
    return res
 
# Initialize our array
arr = []
 
# Take array size as input
n = int(input("Enter array size : "))
 
# Take array element input 
while(n):
    num = int(input("Enter number : "))
    arr.append(num)
    n-=1
 
print("\n\nOdd occurring number is : ",OddOccurring(arr))

"""TwoOddOccrring""" 

# Program to find two numbers that are odd occurring 
 
def printTwoOdd(arr, size):
     
    # xorof2 will hold xor of the 2 odd occurring numbers
    xorof2 = arr[0]
 
    # These will hold 2 odd occurring numbers
    x = 0
    y = 0
 
    # This will hold the rightmost set bot from xorof2
    Set_bit = 0
 
    for i in range(1, size):
        xorof2 = xorof2 ^ arr[i]
 
    setbit = xorof2 & ~(xorof2 - 1)
    
    # If number is haivng set bit at location we need then XOR it with x else y
    for i in range(size):
        if(arr[i] & setbit):
            x = x ^ arr[i]
        else:
            y = y ^ arr[i]
 
    print("The two ODD elements are", x, "&", y)
 
# Create an empty array
arr = []
 
# Take array size and elements as input
arr_size = int(input("Enter size of the array : "))
for i in range(0,arr_size):
    z = int(input("Enter element : "))
    arr.append(z)
    
printTwoOdd(arr, arr_size)

