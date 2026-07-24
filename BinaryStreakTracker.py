# Step 1: Create a Binary Array
binary_scores = [1, 1, 0, 1, 1, 1, 0, 1, 1]

# Step 2 & 3: Build a Streak Counter and Track the Best Streak
current_streak = 0
best_streak = 0

for value in binary_scores:
    if value == 1:
        current_streak += 1
        if current_streak > best_streak:
            best_streak = current_streak
    else:
        current_streak = 0

# Step 4
numbers = [4, 0, 7, 0, 2, 8, 0, 5]

read_pointer = 0
write_pointer = 0

while read_pointer < len(numbers):
    if numbers[read_pointer] != 0:
        numbers[write_pointer] = numbers[read_pointer]
        write_pointer += 1
    read_pointer += 1

# Step 5
while write_pointer < len(numbers):
    numbers[write_pointer] = 0
    write_pointer += 1

# Step 6
print("Binary Scores:", binary_scores)
print("Longest streak of 1s:", best_streak)
print()
print("Array after moving non-zero values to the front:")
print(numbers)
