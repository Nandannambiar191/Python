# Step 1: Print the Program Title
print("Stack Frame Visualizer")


# Step 2: Linear Recursion
def linear_recursion(n):
    if n == 0:
        return
    print("Linear:", n)
    linear_recursion(n - 1)


# Step 3: Tail Recursion
def tail_recursion(n):
    if n == 0:
        return
    print("Tail:", n)
    tail_recursion(n - 1)


# Step 4: Head Recursion
def head_recursion(n):
    if n == 0:
        return
    head_recursion(n - 1)
    print("Head:", n)


# Step 5: Increasing-Decreasing Recursion
def increasing_decreasing(n):
    if n == 0:
        return
    print("Down:", n)
    increasing_decreasing(n - 1)
    print("Up:", n)


# Step 6: Tree Recursion
def tree_recursion(n):
    if n == 0:
        return
    print("Tree:", n)
    tree_recursion(n - 1)
    tree_recursion(n - 1)


# Step 7: Final Summary
print("\nSummary")
print("Linear Recursion: One recursive call at each level.")
print("Tail Recursion: Recursive call is the last operation.")
print("Head Recursion: Work is done after the recursive call returns.")
print("Increasing-Decreasing: Prints while going down and again while coming back.")
print("Tree Recursion: Makes two recursive calls at each level, creating branches.")


# Step 8: Run and Test
print("Linear Recursion")
linear_recursion(3)

print("\nTail Recursion")
tail_recursion(3)

print("\nHead Recursion")
head_recursion(3)

print("\nIncreasing-Decreasing Recursion")
increasing_decreasing(3)

print("\nTree Recursion")
tree_recursion(3)
