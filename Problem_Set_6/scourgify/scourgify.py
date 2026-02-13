import sys
import csv

if len(sys.argv) < 3:
    sys.exit("Missing command-line argument")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

input_file = sys.argv[1]
output_file = sys.argv[2]

try:
    with open(input_file, "r") as infile, open(output_file, "w", newline="") as outfile:
        fieldnames = ["first", "last", "house"]
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        reader = csv.DictReader(infile)
        writer.writeheader()
        for row in reader:
            name = row["name"]
            last, first_space = name.split(",")
            first = first_space.strip()
            new_dict = {"first": first, "last": last, "house": row["house"]}
            writer.writerow(new_dict)

except FileNotFoundError:
    sys.exit(f"Could not read {input_file}")
