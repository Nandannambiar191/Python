"""SortListByFrequency&Index"""
class Data:
    def __init__(self, value, index, count = 0):
        self.value = value
        self.index = index 
        self.count = count
def sort(arr):
    if arr is None or len(arr) < 2:
        return
    hm = {}
    for i in range(len(arr)):
        hm.setdefault(arr[i], Data(arr[i], i)).count += 1
    value = [*hm.values()]
    value.sort(key=lambda x: (-x.count, x.index))
    k = 0
    for data in value:
        for j in range(data.count):
            arr[k] = data.value
            k += 1
arr = [3, 3, 1, 1, 1, 8, 3, 6, 1, 7, 8]
print("Original:", arr)
sort(arr)
print("Sorted:", arr)


"""SortInOneSwap"""
def sortArray(A):
    if len (A) <= 1:
        return
    x = -1
    y = -1
    prev = A[0]
    for i in range(1, len(A)):
        if prev > A[i]:
            if x == -1:
                x = i - 1
                y = i
            else:
                y = i
                prev = A[i]
                swap(A, x, y)
def swap(a, i, j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp
a = [3, 5, 6, 9, 8, 7]
print("Original Array:", a)
sortArray(a)
print("Sorted Array:" , a)                
