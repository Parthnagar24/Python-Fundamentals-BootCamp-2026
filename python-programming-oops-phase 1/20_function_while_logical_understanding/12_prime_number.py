def is_prime(n):

    # Numbers below 2 are not prime
    if n < 2:
        return False

    i = 2

    # Check divisors from 2 up to n-1
    while i < n:

        # If n is perfectly divisible by i,
        # then n has another factor → not prime
        if n % i == 0:
            return False

        i += 1

    # No divisor was found
    return True


result = is_prime(17)
result2 = is_prime(9)
print(result,result2)