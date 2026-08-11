word = input("Enter a word: ")
length = len(word)

password = word.replace(word, "*" * length)
print(f"The password is: {password}")