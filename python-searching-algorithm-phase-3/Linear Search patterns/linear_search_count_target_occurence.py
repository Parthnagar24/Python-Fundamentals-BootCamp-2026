def linear_search(numbers,target):
    count = 0

    for i in range(len(numbers)):
        if numbers[i] == target:
            count +=1
    return count

numbers = [12, 25, 7, 25, 30, 25, 15]
result = linear_search(numbers,25)
print(result)