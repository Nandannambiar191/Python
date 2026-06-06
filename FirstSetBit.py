n = int(input("Enter a number: "))

p = 1
while (n & 1) == 0:
    n >>= 1
    p += 1

print(p)