"""BubbleSortWorking"""
def BubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j +1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
arr = [64, 34, 25, 12, 22, 11, 90]
BubbleSort(arr)
print("Sorted Array:")
for i in range(len(arr)):
    print("%d" %arr[i],end=" ")

"""OptimisedBubbleSort"""
def BubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swap = True
        if swap == False:
            break
arr = [64, 34, 25, 12, 22, 11, 90]
BubbleSort(arr)
print("Sorted array :")
for i in range(len(arr)):
    print("%d" %arr[i],end=" ")