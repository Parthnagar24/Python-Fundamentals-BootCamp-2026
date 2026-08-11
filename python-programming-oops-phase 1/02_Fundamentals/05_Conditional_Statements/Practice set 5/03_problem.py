p1 = "make a lot of money"
p2 = "buy now"
p3 ="subcribe this"
p4 = "click this"

t = input("enter")

if (p1 in t or p2 in t or p3 in t or p4 in t):
    print("spam")
else:
    print("not spam")