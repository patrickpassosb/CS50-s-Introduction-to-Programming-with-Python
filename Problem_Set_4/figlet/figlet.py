import sys
import random
from pyfiglet import Figlet

figlet = Figlet()

if len(sys.argv) != 1 and len(sys.argv) != 3:
    sys.exit("Must provide arguments")

if len(sys.argv) == 3:
    if sys.argv[1] != "-f" and sys.argv[1] != "--font":
        sys.exit("Must provide a font")
    if sys.argv[2] in figlet.getFonts():
        figlet.setFont(font=sys.argv[2])
    else:
        sys.exit("Must provide a valid font")
else:
    font = random.choice(figlet.getFonts())
    figlet.setFont(font=font)

user_input = input("Input: ")
print("Output:\n" + figlet.renderText(user_input))
