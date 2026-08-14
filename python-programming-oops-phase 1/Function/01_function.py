#receives a list of numbers and returns the total sum.

def calculate_total(numbers):
    total = 0

    for num in numbers:
        total += num
        
    return total

ctotal = calculate_total([1,2,3,4,5])
print(ctotal)


#return how many positive numbers are in the list.

def count_positive(numbers):
    count = 0

    for num in numbers:
        if num > 0 :
            count+= 1
    return count

positive = count_positive([1,-2,3,-4,-5])
print(positive)


#should return the sum of only the even numbers.
def sum_even(numbers):
    total = 0
    for num in numbers:
        if num% 2==0:
            total += num
    return total

even_total = sum_even([1,2,3,4,5])
print(even_total)