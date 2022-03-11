file=open("a.txt",'r')
s=file.read()
s=s.replace("ash","ASH")
file.close()
file=open("a.txt",'w')
file.write(s)
file.close()

file=open("a.txt",'r')
while str:
    str=file.readline()
    print("\n")
    print(str)
file.close()
