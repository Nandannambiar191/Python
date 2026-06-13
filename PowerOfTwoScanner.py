# Part 1

n = 16

print("n =", n, "->", bin(n))
print("n - 1 =", n - 1, "->", bin(n - 1))
print("n & (n - 1) =", n & (n - 1), "->", bin(n & (n - 1)))


# Part 2 

def is_power_of_2(num):
    return num > 0 and (num & (num - 1)) == 0


# Part 3

def is_power_of_4(num):
    if not is_power_of_2(num):
        return False

    position = 0

    while num > 1:
        num >>= 1
        position += 1

    return position % 2 == 0


# Part 4 

def is_power_of_8(num):
    if not is_power_of_2(num):
        return False

    position = 0

    while num > 1:
        num >>= 1
        position += 1

    return position % 3 == 0


# Part 5 

def binary_power(base, exponent):
    answer = 1

    while exponent > 0:
        if exponent & 1:
            answer *= base

        base *= base
        exponent >>= 1

    return answer


# Part 6

numbers = [1, 2, 4, 8, 16, 32]

for num in numbers:
    print(num, is_power_of_2(num), is_power_of_4(num), is_power_of_8(num))

print(binary_power(2, 5))
print(binary_power(3, 4))
print(binary_power(5, 3))