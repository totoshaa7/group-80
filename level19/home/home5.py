numbers = [1, 2, 3, 4, 5, 6]

n = int(input("შეიყვანე რიცხვი 1-5: "))

for i in range(n-1, len(numbers), n):
    print(numbers[i])