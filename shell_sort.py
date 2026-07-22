"""ShellSort"""
# Shell sort in python
A = [9, 8, 3, 7, 5, 6, 4, 1]
# initialising n
n = len(A)
# Rearrange elements at each n/2, n/4, ... intervals
interval = n // 2
while interval > 0:
    for i in range(interval, n):
        temp = A[i]
        j = i
        while j >= interval and A[j - interval] > temp:
            A[j] = A[j - interval]
            j -= interval
        A[j] = temp
    interval //=2
print(A)

"""LargestNumber"""
# Shell sort in python
# Program to find the intersection of two sorted arrays

# initializing two arrays

A1 = [1, 2, 4, 5, 6, 8, 10]

A2 = [2, 3, 5, 7, 10, 15]

m = len(A1)

n = len(A2)

i, j = 0, 0
while i < m and j < n:
    if A1[i] < A2[j]:
        i += 1
    elif A2[j] < A1[i]:
        j += 1
    else:
        print(A2[j],end=" ")
        j += 1
        i += 1