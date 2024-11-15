#By using while loop
r=0
while(r<5):
    if(r==3):
        r=r+1
        break
    print(r)
    r=r+1

#By using for loop
for i in range(1,8):
    if(i==4):
        break
    print(i)
    i+=1