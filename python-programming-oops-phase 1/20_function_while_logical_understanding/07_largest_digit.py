def largest_digit(n):
    ld = None

    while n >0:
        digit = n%10
        if ld is None or digit > ld :
            ld = digit
        n = n//10
    return ld
        

result = largest_digit(n=58342)
print(result)