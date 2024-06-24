a = input()
for i in a:
    if i.upper() == i and i.isalpha():
        print(i.lower(), end="")
    elif i.lower() == i and i.isalpha():
        print(i.upper(), end="")
    else:
        print(i, end="")
