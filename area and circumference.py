print("1. the area of the circle")
print("2. the circumference of the circle")
num=int(input("enter the choice"))
r=float(input("enter the radius:"))
if num==1:
    area=(3.14*r*r)
    print("the area is: ",area)
elif num==2:
    c=(2*3.14*r)
    print("the circumference is: ",c)
elif num==12:
    area=(3.14*r*r)
    c=(2*(3.14)*r)
    print("the area is: ",area,"the circumference is: ",c)
    
