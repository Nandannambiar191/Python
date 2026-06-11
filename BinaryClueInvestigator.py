# Step 1
print("BinaryClueInvestigator")
print("\n")

# Step 2
a = 12
b = 12


print("a ^ a =", a ^ a)
print("a ^ 0 =", a ^ 0)

if (a ^ b) == 0:
    print("a and b are equal")
print("\n")

# Step 3
nums = [3, 5, 3, 7, 5]

result = 0
for num in nums:
    result ^= num


print("Remaining number:", result)
print("\n")

# Step 4
nums2 = [4, 2, 4, 2, 9]

odd = 0
for num in nums2:
    odd ^= num


print("Odd-occurring number:", odd)
print("\n")

# Step 5
nums3 = [1, 2, 3, 2, 3, 1, 5, 7]

xor_of_two = 0
for num in nums3:
    xor_of_two ^= num


print("Combined XOR:", xor_of_two)
print("\n")

# Step 6
rightmost_set_bit = xor_of_two & -xor_of_two


print("Rightmost set bit:", rightmost_set_bit)
print("\n")

# Step 7
x = 0
y = 0

for num in nums3:
    if num & rightmost_set_bit:
        x ^= num
    else:
        y ^= num


print("First odd-occurring number:", x)
print("Second odd-occurring number:", y)
print("\n")
