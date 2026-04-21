import numpy as np
from sympy import *

subjects = ["Functions", "Matrices", "Calculus", "Statistics", "Algebra"]
x, y, z = symbols("x y z")

def main():

    subject = input("Which subject will you choose? ").capitalize()


    if subject in subjects:
        print(f"You choose {subject}")
        generate_exercise(subject)


    print(subject)


def generate_exercise(subject: str) -> str:
    if subject == "Algebra":
        



if __name__ == "__main__":
    main()