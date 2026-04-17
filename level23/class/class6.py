sentence = input("შეიყვანე წინადადება: ")
symbol = input("შეიყვანე სიმბოლო: ")

for i in range(len(sentence)):
    if sentence[i] == symbol:
        print(i)