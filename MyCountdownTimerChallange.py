
print("=== RECURSION DEMONSTRATION PROGRAM ===\n")



def countdown(number):
    if number == 0:
        print("Time is up!")
        return

    print(number)
    countdown(number - 1)



def build_and_unwind(level):
    if level == 0:
        print("Reached the bottom.")
        return

    print(f"Building level {level}")
    build_and_unwind(level - 1)
    print(f"Unwinding level {level}")



def count_up(number):
    if number > 10:
        return

    print(number)
    count_up(number + 1)



def factorial(number):
    if number == 0 or number == 1:
        return 1

    return number * factorial(number - 1)



def unsafe_countdown(number):
    print(number)



print("\n--- Countdown Demo ---")
countdown(5)

print("\n--- Build and Unwind Demo ---")
build_and_unwind(3)

print("\n--- Count Up Demo ---")
count_up(1)

print("\n--- Factorial Demo ---")
print("Factorial of 5 =", factorial(5))

print("\n--- Unsafe Countdown Demo ---")
unsafe_countdown(5)