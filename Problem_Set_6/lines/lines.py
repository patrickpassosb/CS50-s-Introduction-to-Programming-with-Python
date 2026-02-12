import sys

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")
if len(sys.argv) >= 3:
    sys.exit("Too many command-line arguments")

user_input = sys.argv[1]

if not user_input.endswith(".py"):
    sys.exit("Not a Python file")

n_lines = 0

with open(user_input) as file:
    for line in file:
        clean_line = line.strip()
        if clean_line and not clean_line.startswith("#"):
            n_lines += 1

print(n_lines)
