def reverse(n):
    reverse_number = 0

    while n > 0:
        digit = n % 10 # get the last digit
        reverse_number = reverse_number * 10 + digit
        n = n //10 # remove last digit
        print(reverse_number)
    return reverse_number

result = reverse(n =58342)
print(result)