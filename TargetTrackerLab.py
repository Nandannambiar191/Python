
arr = [1, 3, 5, 2, 2]
print("Array:", arr)


print("\nChecking for Equilibrium Point:")

found = False

for i in range(len(arr)):
    left = arr[:i]
    right = arr[i + 1:]

    left_sum = sum(left)
    right_sum = sum(right)

    print("Index:", i)
    print("Left:", left, "Sum =", left_sum)
    print("Right:", right, "Sum =", right_sum)

    if left_sum == right_sum:
        print("Equilibrium Index:", i)
        found = True
        break

if not found:
    print("No Equilibrium Index Found")


print("\nGrowing Window:")

for i in range(len(arr)):
    window = arr[:i + 1]
    print(window, "Sum =", sum(window))


target = 7

print("\nSearching for Target Sum:", target)

found = False

for i in range(len(arr)):
    for j in range(i, len(arr)):
        subarray = arr[i:j + 1]

        if sum(subarray) == target:
            print("Subarray Found:", subarray)
            found = True
            break

    if found:
        break

if not found:
    print("No Subarray Found")