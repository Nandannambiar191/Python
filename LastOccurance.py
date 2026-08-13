arr = [1, 2, 3, 4, 1, 5, 1, 4]
target = 1
last_index = -1
for i in range(len(arr)):
    if arr[i] == target:
        last_index = i
if last_index != -1:
    print("Last occurrence of the element", target, "is index", last_index)
else:
    print("Element not found")