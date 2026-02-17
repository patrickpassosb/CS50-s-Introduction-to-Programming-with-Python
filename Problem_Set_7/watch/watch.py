import re
import sys


def main():
    if len(sys.argv) == 2:
        html = sys.argv[1]
    else:
        html = input("HTML: ")
    print(parse(html))


def parse(html):
    pattern = r'<iframe.*?src="(?:https?://)?(?:www\.)?youtube\.com/embed/([^"]+)"'
    match = re.search(pattern, html)
    if match:
        id = match.group(1)
        return f"https://youtu.be/{id}"
    else:
        return None


if __name__ == "__main__":
    main()
