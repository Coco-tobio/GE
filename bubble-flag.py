n=int(input("enter the number of elements:"))
lst=[]
for  i in range(n):
    element=int(input("enter the element:"))
    lst.append(element)
flag=False
length=len(lst)
for a in range (length-1):
    for b in range (0,length-a-1):
        if lst[b]>lst[b+1]:
            lst[b],lst[b+1]=lst[b+1],lst[b]
            flag=True
if flag==True:
    print (lst)
