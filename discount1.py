sale=float(input("enter the sales amount:"))
if sale>10000:
    discount=0.10*sale
    print("the discount is:",discount)
else:
    discount=.05*sale
    print("the discount is:",discount)
