def armstrong(n):
    original = n
    arm = 0

    while n>0:
        digit = n% 10
        arm = arm + (digit*digit*digit)
        n = n//10

    if original == arm:
        return True
    else:
        return False
    

user = int(input("Enter the number:"))
result = armstrong(user)
print(result)