text = input("camelCase: ")
i = 0

for c in text:

    if c.isupper() and i > 0:
        print("_" + c.lower(), end="")
    elif c.isupper() and i == 0:
        print(c.lower(), end="")
    else:
        print(c, end="")
    i += 1

print()
