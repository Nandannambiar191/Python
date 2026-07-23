# Step 1
prices = [100, 180, 260, 310, 40, 535, 695]
print("Stock Prices:", prices)

# Step 2
profit = 0

for i in range(1, len(prices)):
    if prices[i] > prices[i - 1]:
        profit += prices[i] - prices[i - 1]

print("Stock Buy-Sell Profit:", profit)

# Step 3
total_profit = 0

for i in range(1, len(prices)):
    difference = prices[i] - prices[i - 1]
    if difference > 0:
        total_profit += difference

print("Total Positive Difference Profit:", total_profit)

# Step 4
heights = [4, 2, 0, 3, 2, 5]

left_tallest = [0] * len(heights)
left_tallest[0] = heights[0]

for i in range(1, len(heights)):
    left_tallest[i] = max(left_tallest[i - 1], heights[i])

print("Heights:", heights)
print("Left Tallest:", left_tallest)

# Step 5
right_tallest = [0] * len(heights)
right_tallest[-1] = heights[-1]

for i in range(len(heights) - 2, -1, -1):
    right_tallest[i] = max(right_tallest[i + 1], heights[i])

print("Right Tallest:", right_tallest)

# Step 6
water = 0

for i in range(len(heights)):
    trapped = min(left_tallest[i], right_tallest[i]) - heights[i]
    water += trapped

# Step 7: 
print("Total Stock Profit:", profit)
print("Left Tallest:", left_tallest)
print("Right Tallest:", right_tallest)
print("Total Rainwater Trapped:", water)
