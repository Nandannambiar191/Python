"""UnderstandingBinarySearch"""
def binarySearch(arr, l, r, x):
    while l <= r:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    return -1
arr = [2, 3, 4, 10, 40]
x = 10
result = binarySearch(arr, 0, len(arr) - 1, x)

if result != -1:
    print("Element {} is present at index {}".format(x, result))

else:
    print("Element is not present in array")

"""RecursiveBinarySearch"""
def binarySearch(arr, l, r, x):
    if r >= l:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return mid
        elif arr [mid] > x:
            return binarySearch(arr, l, mid-1, x)
        else:
            return binarySearch(arr, mid + 1, r, x)
    else:
        return -1
arr = [2, 3, 4, 10, 40]
x = 10
result = binarySearch(arr, 0, len(arr)-1, x)
if result != -1:
    print("Element {} is present at index {}".format(x, result))

else:
    print("Element is not present in array")


""" SmallestMissingElement"""

def findSmallestMissing(nums, left=None, right=None):

    if left is None and right is None:
        (left, right) = (0, len(nums) - 1)
    if left > right:
        return left
    mid = left + (right - left) // 2
    if nums[mid] == mid:
        return findSmallestMissing(nums, mid + 1, right)
    else:
        return findSmallestMissing(nums, left, mid - 1)
        
nums = [0, 1, 2, 6, 9, 11, 15]
print('The smallest missing element is', findSmallestMissing(nums))
        