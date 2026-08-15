def perfect(n):

    # Store the original number
    original = n

    # This will store the sum of proper divisors
    total = 0

    # Start checking from 1
    i = 1

    # We don't include n itself
    while i < n:

        # Check whether i divides n exactly
        if n % i == 0:
            total += i

        # Move to the next possible divisor
        i += 1

    # If sum of divisors equals original number
    if total == original:
        return True
    else:
        return False


result = perfect(6)
print(result)