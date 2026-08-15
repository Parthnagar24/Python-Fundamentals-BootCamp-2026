def fibonacci(n):
    a = 0
    b = 1
    count = 0
    l = []
    
    while count < n:
        l.append(a)
        new = a+ b
        a = b
        b =new

        count += 1
    return l

result = fibonacci(n=5)
print(result)