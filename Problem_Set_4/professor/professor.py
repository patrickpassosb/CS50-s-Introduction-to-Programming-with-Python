import random


def main():
    level = get_level()
    score = 0

    for i in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        attempts = 0

        while attempts < 3:
            user_answer_str = input(f"{x} + {y} = ")
            try:
                user_answer = int(user_answer_str)
            except ValueError:
                print("EEE")
                attempts += 1
                continue

            answer = x + y

            if answer == user_answer:
                score += 1
                break
            if answer != user_answer:
                print("EEE")
                attempts += 1

        if attempts == 3:
            print(f"{x} + {y} = {answer}")

    print(f"Score: {score}")

def get_level():
    while True:
        level_str = input("")
        try:
            level = int(level_str)

            if level not in [1, 2, 3]:
                continue
            else:
                return level

        except ValueError:
            print("Must be an integer")
            continue

def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    if level == 2:
        return random.randint(10, 99)
    if level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError

if __name__ == "__main__":
    main()
