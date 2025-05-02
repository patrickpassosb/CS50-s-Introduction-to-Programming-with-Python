def main():
    time = input("What time is it? ")
    period = None
    if time.endswith("a.m."):
        period = "am"
        time = time.replace("a.m.", "")
    elif time.endswith("p.m."):
        period = "pm"
        time = time.replace("p.m.", "")

    hours, minutes = time.strip().split(":")
    hours = int(hours)

    if period == "am" and hours == 12:
        hours = 0
    elif period == "pm" and hours != 12:
        hours += 12

    time = f"{hours}:{minutes}"

    hour = convert(time)
    if 7 <= hour <= 8:
        print("breakfast time")
    elif 12 <= hour <= 13:
        print("lunch time")
    elif 18 <= hour <= 19:
        print("dinner time")


def convert(time):
    hours, minutes = time.split(":")
    hours = float(hours)
    minutes = float(minutes)
    total = hours + minutes / 60
    return total


if __name__ == "__main__":
    main()
