def factorial(n):

    if n == 1 or n ==0 :
        return 1
    else:
        return factorial(n-1) * n

user = int(input("Enter the number:"))
result = factorial(user)
print(result)


def factorial(n):
    result = 1

    while n > 0:
        result = result * n
        n = n - 1

    return result

user = int(input("Enter the number: "))
result = factorial(user)
print(result)