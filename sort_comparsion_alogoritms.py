"""Sort01Array"""
A = [0,1,0,1,1,1]
n = len(A)
def sort(A, n):
    count = 0
    for i in range(0, n):
        if A[i] == 0:
            count = count + 1
    for i in range(0, count):
        A[i] = 0
    for i in range(count, n):
        A[i] = 1
sort(A, n)
print("Sorted array is:")
for i in range(0, n):
    print(A[i], end=" ")

    
"""UnionOfTwoSortedArrays"""       
A1 = [1,2,8,9]
A2 = [2,3,5,7]
m = len(A1)
n = len(A2)
def union(A1, A2, m, n):
    i = 0 
    j = 0
    while i < m and j < n:
        if A1[i] < A2[j]:
            print(A1[i], end=" ")
            i = i + 1
        elif A2[j] < A1[i]:
            print(A2[j], end=" ")
            j = j + 1
        else:
            print(A2[j], end=" ")
            i = i + 1
            j = j + 1
    while i < m:
        print(A[i], end=" ")
        i = i + 1
    while j < n:
        print(A[j], end=" ")
        j = j + 1
union(A1, A2, m, n)

