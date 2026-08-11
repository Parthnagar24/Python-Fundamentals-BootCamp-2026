number = int(input("Enter a number:"))
print(f"{number} \n 'The multiplication table of number:'")

for num in range(1,11):
    print(f" {number} X {num} = {number * num}")               


number2 = int(input("Enter a number:"))
print(f"{number2} \n 'The multiplication table of number:'")

i = 1
while(i<=10):
    print(f" {number2} X {i} = {number2 * i}") 
    i+=1