def div(n):
    count = 0
    i = 1

    while i <= n:
        if n % i ==0:
            count +=1
            print(count)
        i+=1
    return count

result = div(12)
print(result)