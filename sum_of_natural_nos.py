"""Write a Python program for printing the sum of the first ten natural numbers using the 
while loop."""


j = int(input("Enter a Number: "))
sum = 0
for d in range(1,j+1): 
    sum+=d
    print(sum)