import sys
import os
from PIL import Image, ImageOps

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")


user_input_raw0 = sys.argv[1]
user_input_raw1 = sys.argv[2]
user_input0 = user_input_raw0.lower()
user_input1 = user_input_raw1.lower()

if not user_input0.endswith((".jpg", ".jpeg", ".png")):
    sys.exit("Invalid output")
if not user_input1.endswith((".jpg", ".jpeg", ".png")):
    sys.exit("Invalid output")

tuple0 = os.path.splitext(user_input0)
tuple1 = os.path.splitext(user_input1)
extension0 = tuple0[1]
extension1 = tuple1[1]

if extension1 != extension0:
    sys.exit("Input and output have different extensions")

try:
    photo = Image.open(user_input_raw0)
    shirt = Image.open("shirt.png")
    size = shirt.size
    photo = ImageOps.fit(photo, size)
    photo.paste(shirt, shirt)
    photo.save(user_input_raw1)

except FileNotFoundError:
    sys.exit(f"Could not read {user_input_raw0}")
