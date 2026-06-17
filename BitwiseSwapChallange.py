# Step 1
a = 10
b = 20

print("Before swap:")
print("a =", a, "b =", b)

a = a + b
b = a - b
a = a - b

print("After swap:")
print("a =", a, "b =", b)

# Step 2
x = 5
y = 9

print("\nBefore XOR swap:")
print("x =", x, "y =", y)

x = x ^ y
y = x ^ y
x = x ^ y

print("After XOR swap:")
print("x =", x, "y =", y)

# Step 3
num = 7

print("\nLeft Shift Examples:")
print("Original:", num)
print("num << 1 =", num << 1)  # multiply by 2
print("num << 2 =", num << 2)  # multiply by 4
print("num << 3 =", num << 3)  # multiply by 8

# Step 4
n1 = -10
n2 = 15

different_signs = (n1 < 0) ^ (n2 < 0)

print("\nDifferent Signs Check:")
print("n1 =", n1, "n2 =", n2)
print("Different signs?", different_signs)

# Step 5
dividend = 23
divisor = 4

quotient = 0
remainder = dividend

while remainder >= divisor:
    remainder -= divisor
    quotient += 1

print("\nDivision Without /")
print("Dividend:", dividend)
print("Divisor:", divisor)
print("Quotient:", quotient)
print("Remainder:", remainder)

# Step 6
print("\nProgram Complete!")