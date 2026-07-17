# -----------------------------
# Part 1: Stair Climbing
# -----------------------------
def stair_ways(n):
    if n == 0:
        return 1          # Reached the top
    if n < 0:
        return 0          # Invalid path

    return stair_ways(n - 1) + stair_ways(n - 2)


# -----------------------------
# Part 2: Trace the Call Tree
# -----------------------------
def trace_stair_ways(n, depth=0):
    print(" " * depth + f"stair_ways({n})")

    if n == 0:
        print(" " * depth + "return 1")
        return 1

    if n < 0:
        print(" " * depth + "return 0")
        return 0

    left = trace_stair_ways(n - 1, depth + 2)
    right = trace_stair_ways(n - 2, depth + 2)

    result = left + right
    print(" " * depth + f"return {result}")
    return result


# -----------------------------
# Part 3: Generate Balanced Braces
# -----------------------------
def generate_braces(current, open_left, close_left):
    if len(current) == 2 * total_pairs:
        print(current)
        return

    # Add an opening brace
    if open_left < total_pairs:
        generate_braces(current + "{", open_left + 1, close_left)

    # Add a closing brace
    if close_left < open_left:
        generate_braces(current + "}", open_left, close_left + 1)


# -----------------------------
# Main Program
# -----------------------------
n = 4
print("Number of ways to climb", n, "stairs:", stair_ways(n))

print("\nTracing recursion:")
trace_stair_ways(n)

print("\nBalanced braces:")
total_pairs = 3
generate_braces("", 0, 0)