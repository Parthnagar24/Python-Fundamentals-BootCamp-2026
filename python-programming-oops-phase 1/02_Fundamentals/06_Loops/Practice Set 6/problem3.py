# prime number  divided by 1 or self

n = int(input("Enter the number:"))

for i in range(2,n):
    if n%i == 0:
        print("Not a Prime Number")
        break
else:
    print("Number is prime")                                      