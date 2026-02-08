import emoji

emoji_text = input("Input: ")
output = emoji.emojize(emoji_text, language="alias")

print(f"Output: {output}")