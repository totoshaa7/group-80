my_name = "Toto"  

name = input("შეიყვანე შენი სახელი: ")
age = int(input("შეიყვანე შენი ასაკი: "))
height = float(input("შეიყვანე შენი სიმაღლე (მაგ: 1.95): "))

if age > 18 and name == my_name and height > 1.85:
    print("პირობა შესრულებულია ✅")
else:
    print("პირობა არ შესრულდა ❌")