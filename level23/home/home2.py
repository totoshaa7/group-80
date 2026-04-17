my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

index = int(input("შეიყვანე ინდექსი (1-5): "))

element = my_list.pop(index)  
my_list.insert(0, "change") 

print("3)", my_list)