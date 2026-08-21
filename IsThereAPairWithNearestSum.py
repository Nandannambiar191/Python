arr = [7, 18, 65, 84, 87, 91, 99, 113]

min_diff = float('inf')
pair = ()

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        diff = abs(arr[i] - arr[j])

        if diff < min_diff:
            min_diff = diff
            pair = (arr[i], arr[j])

print("The closest pair is", pair[0], "and", pair[1])