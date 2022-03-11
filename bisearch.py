#def bsearch(lst,item):
def bsearch(lst,item):
    start=0
    last=len(lst)-1
    flag=False
    while start<=last and not flag:
        mid=int((start+last)//2)
        if lst[mid]==item:
            flag=True
        else:
            if item<lst[mid]:
                last=mid-1
            else:
                start=mid+1
    return flag

lst=[]
n=int(input("Enter the number of elements in list:"))
for i in range (n):
    element=int(input("\nEnter the element:"))
    lst.append(element)
item=int(input("Enter the element need to be searched:"))
print(bsearch(lst, item))


