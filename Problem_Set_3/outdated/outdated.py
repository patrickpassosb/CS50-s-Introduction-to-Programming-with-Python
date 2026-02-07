list = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:

    date = input("Date: ").strip()

    if "/" in date:

        try:
            month, day, year = date.split("/")
            month = int(month)
            day = int(day)
            year = int(year)

            if month < 1 or month > 12:
                continue
            if day < 1 or day > 31:
                continue
            if year < 0:
                continue

            print(f"{year}-{month:02}-{day:02}")
            break

        except (ValueError):
            continue
    else:
        try:
            if "," not in date:
                continue
            else:
                month_day_unstripped, year_unstripped = date.split(",")
                month_str, day_str = month_day_unstripped.strip().split(" ")

                if month_str in list:
                    month = list.index(month_str) + 1
                    day = int(day_str)
                    year_str = year_unstripped.strip()
                    year = int(year_str)

                else:
                    continue

                if day < 1 or day > 31:
                    continue
                if year < 0:
                    continue
                print(f"{year}-{month:02}-{day:02}")
                break

        except (ValueError):
            continue
