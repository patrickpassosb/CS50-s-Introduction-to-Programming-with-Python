def convert(s):
        s = s.replace(":)", "🙂")
        s = s.replace(":(", "🙁")
        return s

s = input("write something ")
print(convert(s))
