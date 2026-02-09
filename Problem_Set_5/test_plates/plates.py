def main():
    s = input("Plate: ")

    if is_valid(s):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False

    if not s[0].isalpha() or not s[1].isalpha():
        return False

    digit_seen = False

    for character in s:
        if character.isdigit():
            if digit_seen == False:
                if character == "0":
                    return False
            digit_seen = True
        elif character.isalpha() == True:
            if digit_seen == True:
                return False
        else:
            return False

    return True


if __name__ == "__main__":
    main()
