"""print(1) 
print(2)
print(3) 
print(4) 
print(5) """

# The same task can be done using for loops
for i in range(1,6):
    print(i)

# understanding while loop

i = 1
while(i<6):
    print(i)
    i += 1

# print 1 to 50 using while loop

num = 1
while(num<=50):
    print(num)
    num +=1

# print the content of a list

list  = ["Happy",12,2.4,["Happy","Is"],True]
print(len(list))
i =0
while(i < len(list)):
    print(list[i])
    i+=1 

# get all even numbers till 10
for n in range(0,11,2):
    print(n)

# using for loop with list
list1 = ["Happy",12,2.4,["Happy","Is"],True]
for l in list1:
    print(l)

# using for loop with tuple
t =(6,2,54,1313)
for i in t:
    print(i)

# using for loop with string
s ="Harry"
for i in s:
    print(i) # string ka each character

# print character of string in reverse
s ="Harry"
for m in range(len(s)-1,-1,-1):
    print(s[m])

# use of else with for loop
list3 = [1,2,3,4,5]
for i in list3:
    print(i)
else:
    print("done")

# break statement

for i in range(100):
    if (i == 9):
        break # Exit the loop right now 
    print(i)

# continue statement

for i in range(20):
    if (i == 9):
        continue # skip this iteration 
    print(i)

# pass statement

for i in range(60):
    pass  # this helps us work on further analysis while keeping this part on hold


i =0
while(i<40):
    print(i)
    i+=1