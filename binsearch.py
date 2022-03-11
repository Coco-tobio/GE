l=eval(input("enter the list"))
x=int(input("enter the element to be searched: "))

def bisearch(l,x):
    start=0
    last=len(l)
    while start<=last:
        mid=((start+last)//2)
        if l[mid]==x:
            return mid
        elif l[mid]<x:
            start=mid+1
        elif l[mid]>x:
            last=mid-1
    return-1

result=bisearch(l,x)
if result!=-1:
    print("element found",result)
else:
    print("element not found")
