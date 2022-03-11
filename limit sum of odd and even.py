ctr=1
even=0
odd=0
n=int(input("enter the limit:"))
while(ctr<=n):
    if ctr%2==0:
        even+=ctr
    else:
        odd+=ctr
    ctr+=1
print("the sum of even no.:",even)
print("the sum of odd no.:",odd)
