num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if num1 > num2:
    big = num1
else:
    big = num2
while True:
    if big % num1 == 0 and big % num2 == 0:
        print("LCM is:", big)
        break
    big += 1