def longgest_word(words):
    longgest=words[0]
    for word in words:
        if len(word)>len(longgest):
            longgest=word
    return longgest
words=input("Enter words whit space: ").split()
print("The longgest word is:",longgest_word(words))