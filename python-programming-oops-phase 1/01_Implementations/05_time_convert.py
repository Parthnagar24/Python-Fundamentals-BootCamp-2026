second = int(input("Enter second (0-59): "))

hour = second // 60 // 60
print(f"{second} seconds is equal to {hour} hours")

minute = second // 60 % 60
print(f"{second} seconds is equal to {minute} minutes")
