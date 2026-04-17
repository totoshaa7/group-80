surname = input("შეიყვანე შენი გვარი: ")
case = input("რომელი case გინდა? (upper/lower/capitalize/none): ")

if case == "upper":
    print(surname.upper())
elif case == "lower":
    print(surname.lower())
elif case == "capitalize":
    print(surname.capitalize())
elif case == "none":
    print(surname)
else:
    print("incorrect input")