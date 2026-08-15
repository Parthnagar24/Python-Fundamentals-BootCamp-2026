def product_digit(n):
    prod = 1

    while n>0:
        digit = n % 10
        prod *=digit
        n =n //10

    return prod

result = product_digit(n=1234556)
print(result)