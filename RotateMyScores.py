# Step 1

print("===== ARRAY OPERATIONS =====")

# Step 2

print("\nStep 2: Reverse Scores Using Two Pointers")

scores = [85, 90, 78, 92, 88, 76]

print("Original List:", scores)

start = 0
end = len(scores) - 1

while start < end:
    temp = scores[start]
    scores[start] = scores[end]
    scores[end] = temp

    start += 1
    end -= 1

print("Reversed List:", scores)

# Step 3

print("\nStep 3: Reverse Scores in Groups")

scores = [85, 90, 78, 92, 88, 76, 95, 80]
groupSize = 3

print("Original List:", scores)

i = 0

while i < len(scores):
    start = i
    end = min(i + groupSize - 1, len(scores) - 1)

    while start < end:
        temp = scores[start]
        scores[start] = scores[end]
        scores[end] = temp

        start += 1
        end -= 1

    i += groupSize

print("Group Reversed List:", scores)

# Step 4

print("\nStep 4: Left Rotate by 1")

scores = [85, 90, 78, 92, 88, 76]

print("Original List:", scores)

temp = scores[0]

for i in range(len(scores) - 1):
    scores[i] = scores[i + 1]

scores[len(scores) - 1] = temp

print("After Left Rotate by 1:", scores)

# Step 5

print("\nStep 5: Left Rotate by n")

scores = [85, 90, 78, 92, 88, 76]
n = 2

print("Original List:", scores)

n = n % len(scores)

count = 0

while count < n:
    temp = scores[0]

    for i in range(len(scores) - 1):
        scores[i] = scores[i + 1]

    scores[len(scores) - 1] = temp

    count += 1

print("After Left Rotate by", n, ":", scores)

# Step 6

print("\nStep 6: Find Leaders in an Array")

scores = [16, 17, 4, 3, 5, 2]

print("Array:", scores)

leaders = []

maxRight = scores[len(scores) - 1]
leaders.append(maxRight)

i = len(scores) - 2

while i >= 0:
    if scores[i] > maxRight:
        maxRight = scores[i]
        leaders.append(scores[i])

    i -= 1

start = 0
end = len(leaders) - 1

while start < end:
    temp = leaders[start]
    leaders[start] = leaders[end]
    leaders[end] = temp

    start += 1
    end -= 1

print("Leaders:", leaders)

# Step 7

print("\nStep 7: Program Finished Successfully!")
print("Change the scores, group size, or n value to test different results.")