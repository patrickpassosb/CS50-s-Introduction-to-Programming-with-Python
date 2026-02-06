while True:
    try:
        fraction = input("Fraction: ").strip()
        x_and_y = fraction.split("/")
        if len(x_and_y) != 2:
            continue
        x = int(x_and_y[0])
        y = int(x_and_y[1])
        if x > y or x < 0 or y <= 0:
            continue
        percentage = round(x / y * 100)
        if percentage <= 1:
            print("E")
            break
        elif percentage >= 99:
            print("F")
            break
        else:
            print(str(percentage) + "%")
            break

    except (ValueError, ZeroDivisionError):
        pass
