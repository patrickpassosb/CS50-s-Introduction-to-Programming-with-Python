import random

while True:
        level_str = input("Level: ")
        try:
            level = int(level_str)

            if level < 1:
                print("Must be a positive number")
                continue
            else:
                break
            
        except ValueError:
            print("Must be an integer")
            continue

n = random.randint(1, int(level))

while True:
    try:
        guess_str = input("Guess: ")
        guess = int(guess_str)
    except ValueError:
        print("Must be an integer")
        continue

    if guess < 1:
        continue
    if guess < n:
        print("Too small!")
        continue
    if guess > n:
        print("Too large!")
        continue
    if guess == n:
        print("Just right!")
        break
