'''def search(l,n):
    for i in range(len(l)):
        if l[i] == n: 
            return i 
  
    return -1

l=[]
x=int(input('how many elements: '))
for i in range(x):
    e=int(input('enter the no. : '))
    l.append(e)
    
item=int(input('element to be found: '))
search(l,item)'''

def linearSearch(array, n, x):

    # Going through array sequencially
    for i in range(0, n):
        if (array[i] == x):
            return i
    return -1


array = [2, 4, 0, 1, 9]
x = 1
n = len(array)
result = linearSearch(array, n, x)
if(result == -1):
    print("Element not found")
else:
    print("Element found at index: ", result)

