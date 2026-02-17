import re
import sys


def main():
    if len(sys.argv) == 2:
        s = sys.argv[1]
    else:
        s = input("Text: ")
    print(count(s))


def count(s):
    pattern = r"(\bum\b)"
    match = re.findall(pattern, s, re.IGNORECASE)
    count = len(match)
    return count


if __name__ == "__main__":
    main()
