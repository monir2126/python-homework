text = input("Enter a text: ")

text = text.replace(" ", "")
text = text.lower()

letters = set(text)

print("Number of different characters:", len(letters))