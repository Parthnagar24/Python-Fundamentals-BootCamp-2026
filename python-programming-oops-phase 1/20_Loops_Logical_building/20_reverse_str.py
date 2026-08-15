word = "python"
reverse = ""

for char in word:
    reverse = char + reverse
    print(reverse)
print(reverse)


word = "madam"
reverse = ""

for char in word:
    reverse = char + reverse

if word == reverse:
    print("Palindrome")
else:
    print("Not palindrome")