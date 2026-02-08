def main():
    word = input("Input: ")
    shortened = shorten(word)
    print(f"Output: {shortened}")


def shorten(word):
    vowels = "aeiouAEIOU"
    result = ""
    for letter in word:
        if letter not in vowels:
            result += letter
    return result


if __name__ == "__main__":
    main()
