numbers = [5, -3, 0, 7, -1, 0, 4, -6]

positive = 0
negative = 0
zero_count = 0

for num in numbers:
    if num > 0:
        positive += num
    elif num < 0:
        negative += 1
    else:
        zero_count += 1

print("Positive sum:", positive)
print("Negative count:", negative)

for i in range(zero_count):
    print("zero")
