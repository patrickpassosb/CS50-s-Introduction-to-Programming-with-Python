import re
import sys


def main():
    if len(sys.argv) == 2:
        ip = sys.argv[1]
    else:
        ip = input("IPv4 Address: ")
    print(validate(ip))


def validate(ip):
    pattern = r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$"
    match = re.fullmatch(pattern, ip)
    if not match:
        return False
    parts = ip.split(".")
    if len(parts) != 4:
        return False
    for part in parts:
        if len(part) > 1 and part.startswith("0"):
            return False
        value = int(part)
        if value < 0 or value > 255:
            return False
    else:
        return True


if __name__ == "__main__":
    main()
