# Step 1 & 2
items = ["A", "B", "C"]
n = len(items)
total_subsets = 2 ** n

print("Items:", items)
print("Number of subsets:", total_subsets)
print()

# Step 3
print("Binary Mask Table")
mask = 0
while mask < total_subsets:
    print(mask, "->", format(mask, f"0{n}b"))
    mask += 1

print()

# Step 4
print("Bit Probes")
for j in range(n):
    probe = 1 << j
    print(f"j = {j}, probe = {probe}, binary = {format(probe, f'0{n}b')}")

print()

# Step 5
print("Power Set")
for mask in range(total_subsets):
    subset = []

    for j in range(n):
        probe = 1 << j

        if mask & probe:
            subset.append(items[j])

    print(format(mask, f"0{n}b"), "->", subset)

print()

# Step 6
def bit_difference(a, b):
    diff = 0

    while a > 0 or b > 0:
        if (a & 1) != (b & 1):
            diff += 1

        a >>= 1
        b >>= 1

    return diff

# Step 7
print("Bit Difference Tests")
print("bit_difference(5, 3) =", bit_difference(5, 3))
print("bit_difference(7, 0) =", bit_difference(7, 0))
print("bit_difference(10, 15) =", bit_difference(10, 15))