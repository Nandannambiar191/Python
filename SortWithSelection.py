n = int(input("Enter size of array: "))

arr = []

print("Start entering elements of array, each element in a new line:")

for i in range(n):
    num = int(input())
    arr.append(num)

for i in range(n - 1):
    min_index = i

    for j in range(i + 1, n):
        if arr[j] < arr[min_index]:
            min_index = j

    temp = arr[i]
    arr[i] = arr[min_index]
    arr[min_index] = temp

print("Sorted Array:")

for i in range(n):
    print(arr[i], end=" ")