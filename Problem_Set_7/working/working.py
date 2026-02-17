import re
import sys


def main():
    if len(sys.argv) == 2:
        s = sys.argv[1]
    else:
        s = input("Hours: ")
    print(convert(s))


def convert(s):
    pattern = r"^([1-9]|1[0-2])(?::([0-5][0-9]))?\s(AM|PM)\sto\s([1-9]|1[0-2])(?::([0-5][0-9]))?\s(AM|PM)$"
    match = re.fullmatch(pattern, s)
    if match:
        start_hour = int(match.group(1))
        if match.group(2) == None:
            start_minute = 0
        else:
            start_minute = int(match.group(2))
        start_period = match.group(3)
        end_hour = int(match.group(4))
        if match.group(5) == None:
            end_minute = 0
        else:
            end_minute = int(match.group(5))
        end_period = match.group(6)
        if start_period == "AM":
            if start_hour == 12:
                start_hour = 0
        if start_period == "PM":
            if start_hour != 12:
                start_hour += 12
        if end_period == "AM":
            if end_hour == 12:
                end_hour = 0
        if end_period == "PM":
            if end_hour != 12:
                end_hour += 12

        return f"{start_hour:02}:{start_minute:02} to {end_hour:02}:{end_minute:02}"

    else:
        raise ValueError


if __name__ == "__main__":
    main()
