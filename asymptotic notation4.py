""" Recursion Time Complexity"""
def prints(n):
    if n <= 0:
        return

    print("Codingal")
    prints(n // 2)
    prints(n // 2)

# call the function
prints(8)

""" GiveMe Some Space"""
def sum_n(n):
    return n * (n + 1) // 2  # integer result

print("Sum of first n numbers (n=5):", sum_n(5))

def array_sum(a):
    total = 0
    for i in a:
        total += i
    return total

# Examples
a = [12, 3, 4, 15]
print("Array sum:", array_sum(a))


def summ(n):
    if n <= 0:
        return 0
    return n + summ(n - 1)

print("Recursive sum (n=5):", summ(5))