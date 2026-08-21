n = int(input("Enter size of array: "))

arr = []

print("Start entering elements of array, each element in a new line:")

for i in range(n):
    arr.append(int(input()))

# Bubble Sort
for i in range(n - 1):
    for j in range(n - 1 - i):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print("Sorted Array:")

for x in arr:
    print(x, end=" ")