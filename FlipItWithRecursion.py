# Step 1
num = 4827
print("Digits:")
temp = num
while temp > 0:
    digit = temp % 10
    print(digit)
    temp = temp // 10


# Step 2
def count_digits(num):
    if num < 10:
        return 1
    return 1 + count_digits(num // 10)


# Step 3
def reverse_number(num):
    if num < 10:
        return num

    digits = count_digits(num)
    last_digit = num % 10

    return last_digit * (10 ** (digits - 1)) + reverse_number(num // 10)


# Step 4
def reverse_string(text):
    if len(text) <= 1:
        return text
    return reverse_string(text[1:]) + text[0]


# Step 5
def is_power_of_4(num):
    if num <= 0:
        return False
    if num == 1:
        return True
    if num % 4 != 0:
        return False
    return is_power_of_4(num // 4)


# Step 6 and 7
print("\nTesting Functions:")

print("Count Digits:", count_digits(4827))
print("Reverse Number:", reverse_number(4827))
print("Reverse String:", reverse_string("hello"))

print("64 is power of 4:", is_power_of_4(64))
print("20 is power of 4:", is_power_of_4(20))
print("1 is power of 4:", is_power_of_4(1))
print("-4 is power of 4:", is_power_of_4(-4))