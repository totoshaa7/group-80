age = int(input("შეიყვანეთ ასაკი: "))

if age > 18:
    print("adult")
elif age >= 13 and age <= 18:
    print("teen")
else:
    print("child")