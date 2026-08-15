def smallest_digit(n):
    sd = None

    while n >0:
        digit = n%10
        if sd is None or digit < sd :
            sd = digit
        n = n//10
    return sd
        

result = smallest_digit(n=58342)
print(result)