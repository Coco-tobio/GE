'''file=open("a.txt",'a')
n=int(input("enter the no. of records:"))
for i in range(n):
     s1=str(input("enter the name of the student:"))
     s2=str(input("enter the roll no.:"))
     s3=str(input("enter the stream:"))
     s4=str(input("enter the 10th percentage:"))
     s5=s1+" "+s2+" "+s3+" "+s4+"\n "
     file.write(s5)
file.close()

file=open("a.txt",'r')
s=file.read()
s=s.replace("gita","shi")
file.close()
file=open("a.txt",'w')
file.write(s)
file.close()'''

file=open("a.txt",'r')
while str:
    str=file.readline()
    print(str)
file.close()

file=open("a.txt",'a')
n=int(input("enter the no. of records to append:"))
for i in range(n):
     s1=(input("enter the name of the student:"))
     s2=(input("enter the roll no.:"))
     s3=(input("enter the stream:"))
     s4=(input("enter the 10th percentage:"))
     s5=s1+" "+s2+" "+s3+" "+s4+"\n "
     file.write(s5)
file.close()

file=open("a.txt",'r')
while str:
    str=file.readline()
    print(str)
    print()
file.close()
