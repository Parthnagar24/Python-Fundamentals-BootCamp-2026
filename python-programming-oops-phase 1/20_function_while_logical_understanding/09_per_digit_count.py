def count_per_digit(n,target):
    cpd = 0
  
    while n >0:
        digit = n % 10
        if digit == target:
            cpd +=1
        n =n //10

    return cpd

result = count_per_digit(582342,2)
result2 = count_per_digit(582342,5)
result3 = count_per_digit(582342,4)
print(result,result2,result3)