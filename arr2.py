"""ReverseArrayGroup"""
def reverse(a,a_size):
    temp = 0
    while(temp<a_size):
        start = temp
        end = min(temp + n - 1, a_size - 1)
        while (start < end):
            a[start], a[end] = a[end], a[start]
            start+= 1
            end-=1
        temp+= n
a = [5,23,5,23,1,23,5,136,7,56]
n = 2
a_size = len(a)
reverse(a, a_size, n)
for i in range(0, a_size):
        print(a[i], end =" ")


"""ArrayRotate"""
def rotations(a, n, a_size):
     for i in range(n):
          rotate(a, a_size)
def rotate(a, a_size):
    temp = a[0]
    for i in range(a_size-1):
          a[i] = a[i + 1]
    a[a_size-1] = temp
def printArray(a, a_size):
    for i in range(a_size):
         print("% d"% a[i], end =" ")
    print("\n")

a = [12,12,31,85,2,3,53,56323]
printArray(a,len(a))
rotations(a, 2, len(a))
printArray(a, len(a))

"""LeadersInArray"""
def leaders(a, a_size):
    currentmax = a[a_size-1]
    print(currentmax)
    for i in range(a_size-2, -1, -1):
        if currentmax < a[i]:
            print(a[i])
            currentmax = a[i]
a = [16, 17, 4, 3, 5, 245]

leaders(a, len(a))
