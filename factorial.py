z=int(input("enter the no.: "))
fact=1
a=1
if z==0:
    print('fact is 1')
else:
    while a<=z:
        fact*=a
        a+=1
    print('fact is: ',fact)
