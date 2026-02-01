def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
        if plate[0:2].isalpha() == True and len(plate) >= 2 and len(plate) <= 6:
            digit_seen = False

            for character in plate:
                number = character.isdigit()
                if character == '0' and digit_seen == False:
                    return False
                if number == True:
                    digit_seen = True
                if digit_seen == True and character.isalpha() == True:
                    return False
                if character.isalpha() == False and character.isdigit() == False:
                    return False

        else:
            return False

        return True

main()
