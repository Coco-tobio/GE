list=eval(input("enter the list"))
x=len(list)
for i in range(x-1):
    for j in range(0,x-i-1):
        if list[j]>list[j+1]:
            list[j],list[j+1]=list[j+1],list[j]
            print("the list is", list)
