list1=eval(input("Enter your list:"))

 
def insertion_sort(list1):
    for i in range(1, len(list1)):
        value=list1[i]
        j=i-1
        while j>=0 and value<list1[j]:
            list1[j+1]=list1[j] #creating room for the value
            j=j-1
        list1[j+1]=value
    return list1

 

a=insertion_sort(list1)
print ('The sorted list is', a)
 
         
               
