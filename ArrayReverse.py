arr = [6, 5, 4, 3, 2, 1]

print("Original array :", arr)


reversed_arr = []

for i in range(len(arr) - 1, -1, -1):
    reversed_arr.append(arr[i])

print("Reversed array :", reversed_arr)