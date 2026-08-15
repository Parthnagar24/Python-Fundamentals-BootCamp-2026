def sum_digits(n):
    total_of_digit = 0

    while (n >0):
        digit = n % 10  # get the last digit
        total_of_digit += digit
        n = n //10 # remove the last digit
        print(total_of_digit)
    return total_of_digit

result = sum_digits(n = 58342)
print(result)