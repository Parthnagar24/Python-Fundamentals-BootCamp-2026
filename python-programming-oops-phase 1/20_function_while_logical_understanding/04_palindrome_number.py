def palindrome_number(n):
    original = n
    reverse = 0

    while n >0:
        digit = n % 10 # get the last digit
        reverse = reverse * 10 + digit
        n = n //10 # remove last digit

    if original == reverse:
        return True
    else:
        return False

print("Case 1:")
result = palindrome_number(n=1221)
print(result)

print("Case 2:")
result2 = palindrome_number(n=12431)
print(result2)
