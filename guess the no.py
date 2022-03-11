import random
n=random.randint(1,100)
ctr=0
while ctr<5:
    guess=int(input("guess the no. in range 1-100..:"))
    if guess==n:
        print("you win!!:)")
        break
    else:
        ctr+=1
if not ctr<5:
    print("you lose \n the no. was: ",n)
    
