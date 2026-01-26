# #list არის მონაცემთა ტიპი რომელიც საშუალებას გვაძლევს
# ერთ ცვლადში შევინახოთ რამდენიმე მნიშვნელობა
# სიას ვიყენებთ მაშინ როცა გვჭირდება ბევრი ელემენტის ერთად შენახვა
# და მათზე ციკლით ან ინდექსით მუშაობა#
#2
my_list = [10, 20, 30, 40, 50]
print(my_list[2])

#3 
numbers = [3, 5, 6, 9, 10, 12, 14, 15, 18, 20]

for num in numbers:
    if num % 3 == 0:
        print("divisible by 3")

#4 
text = "programming"
print(text[-3:])

#5
names = ["giorgi", "nino", "ana", "giorgi", "luka", "giorgi"]

user_name = input("შეიყვანე შენი სახელი: ")
count = 0

for name in names:
    if name == user_name:
        print("user name")
        count += 1

print(count)

#6
nums = [1, 2, 3, 4, 5, 6, 8, 9]
sum_even = 0

for n in nums:
    if n % 2 == 0:
        sum_even += n

print(sum_even)

#7
name_list = ["giorgi", "nino", "gabrieli", "ana", "luka"]

for name in name_list:
    if name.startswith("g"):
        print(name, True)