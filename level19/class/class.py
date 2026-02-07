# 1 slicing არის მეთოდი, რომლის საშუალებითაც შეგვიძლია სიიდან, სტრინგიდან ან სხვა მიმდევრობიდან
# ამოვიღოთ გარკვეული ნაწილი
# indexing  გვიბრუნებს მხოლოდ ერთ კონკრეტულ ელემენტს 
# slicing  გვიბრუნებს ერთზე მეტ ელემენტს, ანუ ნაწილს
#2
my_list = [10, 20, 30, 40, 50, 60]
print(my_list[-3:])


#3
name = input("Enter your name: ")
print(name[1:4])


#4
my_surname = "Meskhishvili"  
user_surname = input("Enter your surname: ")

if user_surname[:5] == my_surname[:5]:
    print("Almost same")
else:
    print("Bye")


#5
items = [1, 2, 3, 4, 5, 6, 7]
items[2] = "Random"
print(items[:4])

#7

surname = input("Enter your surname: ")
choice = input("Do you want to reverse it? (yes/no): ")

if choice.lower() == "yes":
    print(surname[::-1])
else:
    print(surname)