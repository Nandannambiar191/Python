"""SortedArrayRecursion"""
def checkSorted(a):
    length = len(a)
    if length == 1 or length == 0:
        return True
    return a[0] <= a[1] and checkSorted(a[1:])
a = [1,2,3,5,6,8,2]
if checkSorted(a):
    print("\nYes given array is sorted")
else:
    print("\nNo given array is not sorted")

"""RecursiveArraySum"""
def arrayTotalSum(a):
    length = len(a)
    if length == 1:
        return a[0]
    return a[0] + arrayTotalSum(a[1:])
a = [1,2,3,6]
print("Array total sum: ",arrayTotalSum(a))

"""LargestArrayElement"""
def MaxElementArray(a):
 
    # Calculating length of array
    length = len(a)
 
    # If array length is 1 just return the element
    if length == 1:
        return a[0]
 
    # Return the largest number among current largest and current element
    return max(a[0],MaxElementArray(a[1:]))
 
a = [1,2,234,234,745,3,6,653]
 
# Displaying result
print("Largest element of array: ",MaxElementArray(a))
