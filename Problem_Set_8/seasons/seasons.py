from datetime import date
import sys
import inflect

p = inflect.engine()


def main():
    if len(sys.argv) == 2:
        user_input = sys.argv[1]
    else:
        user_input = input("Date of birth: ")
    minutes = calculate_minutes(user_input)
    result = convert_to_words(minutes)
    print(result)


def calculate_minutes(user_input):
    try:
        birth = date.fromisoformat(user_input)
        today = date.today()
        delta = today - birth
        minutes = delta.days * 1440
        return minutes
    except ValueError:
        sys.exit(1)


def convert_to_words(minutes):
    sentence = p.number_to_words(minutes, andword="")
    return sentence.capitalize() + " minutes"


if __name__ == "__main__":
    main()
