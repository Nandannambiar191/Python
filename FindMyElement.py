def binary_search(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return -1


arr = [32, 45, 63, 77, 82]
print("Sorted array is", arr)

key = 63

result = binary_search(arr, key)

if result != -1:
    print("Element", key, "is present at index", result)
else:
    print("Element is not present in the array")