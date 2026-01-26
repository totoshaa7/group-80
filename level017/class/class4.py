names = ["giorgi", "nino", "ana", "giorgi", "luka", "giorgi"]

user_name = input("შეიყვანე შენი სახელი: ")
count = 0

for name in names:
    if name == user_name:
        print("user name")
        count += 1

print(count)
