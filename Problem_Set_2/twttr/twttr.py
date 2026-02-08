input = input("Input: ")
vowels = "aeiouAEIOU"
print("Output: ", end="")

for letter in input:
    if letter not in vowels:
        print(letter, end="")

print()
