print("Array Energy Tracker")
print("\n")


# Step 2
energy_levels = [4, -2, 3, -7, 5, 2, -1, 6, -4]

print("\nEnergy Array:")
print(energy_levels)

# Step 3
print("\nSubarrays and Their Sums:")
print("energy_levels[0:3] =", energy_levels[0:3], "Sum =", sum(energy_levels[0:3]))
print("energy_levels[2:6] =", energy_levels[2:6], "Sum =", sum(energy_levels[2:6]))
print("energy_levels[4:]  =", energy_levels[4:], "Sum =", sum(energy_levels[4:]))

# Step 4
print("\nRunning Sum:")
running_sum = 0

for value in energy_levels:
    running_sum += value
    print("Added", value, "-> Running Sum =", running_sum)

# Step 5
print("\nRunning Sum with Reset:")
running_sum = 0

for value in energy_levels:
    running_sum += value

    if running_sum < 0:
        running_sum = 0

    print("After", value, "-> Running Sum =", running_sum)

# Step 6
print("\nTracking Maximum:")
running_sum = 0
max_so_far = 0

for value in energy_levels:
    running_sum += value

    if running_sum < 0:
        running_sum = 0

    if running_sum > max_so_far:
        max_so_far = running_sum

    print("Running Sum =", running_sum, "| Max So Far =", max_so_far)

# Step 7
def kadane(arr):
    running_sum = 0
    max_so_far = 0

    for value in arr:
        running_sum += value

        if running_sum < 0:
            running_sum = 0

        if running_sum > max_so_far:
            max_so_far = running_sum

    return max_so_far

# Step 8
answer = kadane(energy_levels)

print("\n")
print("Maximum Subarray Sum:", answer)

