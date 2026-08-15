def count_digits(n):
    even_count = 0
    odd_count = 0

    while n > 0:
        digit = n % 10
        if digit% 2 ==0:
            even_count +=1
        else:
            odd_count +=1
        n =n //10

    return even_count,odd_count

result = count_digits(n=58342)
print(result)
print(type(result))