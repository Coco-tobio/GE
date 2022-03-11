f=open('a.txt','r')
word=''
for i in f.readlines():
    for j in i.split():
        if len(j)>len(word):
            word=j
print("the word with max lenght is: ",word)
f.close()
    
