def s_e_d(n):
    total = 0

    while n>0:
        digit = n % 10
        if digit % 2 ==0:
            total +=digit
        n =n //10

    return total

result = s_e_d(n=1234556)
print(result)