# Step 1: Create a list of scores
score_list = [45, 60, 75, 88, 92]

# Step 2: Show the list shrinking recursively
def show_shrink(score_list):
    print(score_list)
    if len(score_list) == 1:   # Base case
        return
    show_shrink(score_list[1:])

# Step 3: Check whether the list is sorted
def is_sorted(score_list):
    if len(score_list) <= 1:   # Base case
        return True

    if score_list[0] > score_list[1]:
        return False

    return is_sorted(score_list[1:])

# Step 4: Calculate the recursive sum
def recursive_sum(score_list):
    if score_list == []:       # Base case
        return 0

    return score_list[0] + recursive_sum(score_list[1:])

# Step 5: Find the largest score
def largest_score(score_list):
    if len(score_list) == 1:   # Base case
        return score_list[0]

    largest_tail = largest_score(score_list[1:])

    if score_list[0] > largest_tail:
        return score_list[0]
    else:
        return largest_tail

# Step 6: Run and test the program
print("Shrinking list:")
show_shrink(score_list)

print("\nIs sorted?", is_sorted(score_list))
print("Sum:", recursive_sum(score_list))
print("Largest score:", largest_score(score_list))

# Test with an unsorted list
unsorted_list = [45, 88, 60, 92, 75]
print("\nTesting unsorted list:", unsorted_list)
print("Is sorted?", is_sorted(unsorted_list))
print("Sum:", recursive_sum(unsorted_list))
print("Largest score:", largest_score(unsorted_list))