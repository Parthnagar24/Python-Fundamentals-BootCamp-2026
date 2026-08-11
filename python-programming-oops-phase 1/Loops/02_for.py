# sum of elements inside a list
num = [5,10,15]
total = 0

for i in num : # num = 5 10 15
    total += i 
    # when num 5 total 5
    # when num 10 total 15
    # when num 15 total 30
    print(total) # 5 15 30
print(total) # final value = 30


# count total number of elements in list

numbers = [5, 10, 15, 20]
count = 0

for num in numbers: # 5 10 15 20
    count += 1 
    # when num 5 present count = 1
    # when num 10 present count = 2
    # when num 15 present count =3
    # when num 20 present count = 4
    print(count) # 1 2 3 4 
print(count) # final count = 4


numbers = [5, 10, 15, 20, 22]
count = 0

for num in numbers: # 5 10 15 20 22
    if num % 2 == 0:
      # when num is 5 remainder <> 0 so ignore
      # when num is 10 remainder is 0 accept
      # when num is 15 remainder <> 0 so ignore
      # when num is 20 remainder is 0 accept
      # when num is 22 remainder is 0 accept
        count += 1 
        # for num 10 count = 1
        # for num 20 count = 2
        # for num 22 count = 3
        print(count) # 1 2 3
print(count) # final count = 3


#sum of even elements in list

numbers = [5, 10, 15, 20, 22]
total = 0

for num in numbers:
    if num % 2 ==0:
        '''
        when num is 5 10 remainder<>0 ignore
        when num is 10 20 22 remainder is 0 accept
        '''
        total+=num 
        '''
        for 10 total is 10
        for 20 total is 10 + 20 =30
        for 22 total is 30 + 22 =52
        '''
        print(total)# 10 30 52
print(total) #final result is 52


numbers = [15, 42, 8, 73, 29]

largest = numbers[0]  # 15

for num in numbers: # 15 42 8 73 29
    if num > largest:
        '''
        15 > 15 false
        42 > 15 true
        8 > 42 false
        73 > 42 true
        29 > 73 false
        '''
        largest = num
        print(largest) # 42 73
print(largest) #73






numbers = [10, 25, 30, 15, 40, 5]
largest = None

for num in numbers:
        if (num % 2 == 0) :
            if largest is None or num > largest:
                largest = num
                print(largest)
print(largest)


#smallest odd element
numbers = [10, 25, 30, 15, 40, 5]
smallest = None

for num in numbers:
        if (num % 2 != 0) :
            if smallest is None or num < smallest:
                smallest= num
                print(smallest)
print(smallest)



#highest salary below 80,000
salaries = [45000, 72000, 38000, 95000, 61000, 52000]
high = None

for i in salaries:
    if high is None or (i < 80000 and i >high):
        high = i
        print(high)
print(high)


a = [10,12,14,21,22,3]
for i in a:
     if i % 2 !=0:
          continue
     print(i)


b = [10,-12,-14,-21,22,3]
for i in b:
     if i< 0:
          continue
     print(i)

for i in range(2):
    for j in range(3):
        print(i, j)

for i in range(4):
    for j in range(5):
        print("Hello")

for i in range(3):
    for j in range(2):
        print("*")

for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)


numbers = [12, 7, 20, 15, 30, 9, 40]
count =0
#Count how many numbers are greater than 15.
for i in numbers:
    if i>15: # 20 30 40
        count +=1 # for 20--1  30--2  40--2
        print(count) # 1 2 3 
print(count)# final count 3



sales = [12000, 45000, 18000, 75000, 30000]
#Calculate the total sales only for values ≥ 30,000.
sum = 0

for i in sales:
    if i >=30000:  # total 3 numbers > =
        sum +=i 
        print(sum)
print(sum)


marks = [85, 62, 91, 45, 78, 55]
#Find how many students scored between 60 and 90 inclusive.
count= 0

for i in marks:
    if i>=60 and i<=90:
        count+=1
        print(count)
print(count)


scores = [45, 82, 67, 91, 74, 88]
#Find the highest score below 90.
l =None
for i in scores: 
    if i <90:
        if l is None or i > l:
            l =i
            print(l)
print(l)

for i in range(1, 4):
    for j in range(1, 4):
        if i + j == 4:
            print(i, j)