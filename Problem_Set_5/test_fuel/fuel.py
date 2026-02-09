def main():
    while True:
        try:
            fraction = input("Fraction: ").strip()
            percentage = convert(fraction)
            break
        except (ValueError, ZeroDivisionError):
            continue

    print(gauge(percentage))


def convert(fraction):
    x, y = fraction.split("/")

    x = int(x)
    y = int(y)

    if y == 0:
        raise ZeroDivisionError
    if x > y or x < 0:
        raise ValueError
    percentage = round(x / y * 100)

    return percentage


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return str(percentage) + "%"


if __name__ == "__main__":
    main()
