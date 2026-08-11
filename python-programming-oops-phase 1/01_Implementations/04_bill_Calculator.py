rice = 250
oil = 180
sugar = 90

print(f"Product rice is ${rice}, oil is ${oil}, sugar is ${sugar}.")

bill = rice + oil + sugar
print(f"Total bill is ${bill}.")

gst = bill * 18/100
print(f"GST amount is ${gst}.")
final_bill = bill + gst

print(f"Total bill after adding GST is ${final_bill}.")