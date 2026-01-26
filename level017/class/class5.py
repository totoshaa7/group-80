nums = [1, 2, 3, 4, 5, 6, 8, 9]
sum_even = 0

for n in nums:
    if n % 2 == 0:
        sum_even += n

print(sum_even)