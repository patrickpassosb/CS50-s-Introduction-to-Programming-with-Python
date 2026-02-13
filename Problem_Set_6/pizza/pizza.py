import sys
import csv
from tabulate import tabulate

if len(sys.argv) < 2:
    sys.exit("Missing command-line argument")
elif len(sys.argv) >= 3:
    sys.exit("Too many command-line arguments")


user_input = sys.argv[1]
list = []

if not user_input.endswith(".csv"):
    sys.exit("Not a csv file")
try:
    with open(user_input, "r") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            list.append(row)

except FileNotFoundError:
    sys.exit("File does not exist")


print(tabulate(list, headers="keys", tablefmt="grid"))
