customername = input("Enter your name: ").strip().title()
productname = input("Enter the product name: ").strip().title()
quantity = int(input("Enter the quantity: "))
price = float(input("Enter the price per unit: "))

total = quantity * price
print(f"Total cost for {quantity} {productname}(s): ${total:.2f}")