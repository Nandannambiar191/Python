arr = [-4, 6, 2, 0, 0, 1, 1]
print("Full array:", arr)
print("Left of index 2 : ", arr[:2])
print("Right of index 2:", arr[3:])
print("Left sum at index 2:", sum(arr[:2]))
print("Right sum at index 2:", sum(arr[3:]))
print("\nBalance check:")
for i in range(len(arr)):
    L = sum(arr[:i])
    R = sum(arr[i + 1:])
    print("index", i, "-> left:", L, " right:", R)
print("\nEquilibrium point:")
for i in range(len(arr)):
    if sum(arr[:i]) == sum(arr[i + 1]):
        print("Index:", i, " Element:", arr[i])
nums = [3, 6, 2, 2, 56, 1, 0, 9]
target = 10
print("\nGrowing window (start = 1, target =",target, "):")
curr = 0
for j in range(1, len(nums)):
    curr = curr + nums[j]
    if curr >= target:
        break
print("\nSearching all windows:")