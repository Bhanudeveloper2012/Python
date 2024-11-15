#By uisng while loop
t=8
while(t>0):
    if(t==3):
        t-=1
        continue
    print(t)
    t-=1

#By using for loop
for i in range(-1,7):
    if(i==4):
        i+=1
        continue
    print(i)
    i+=1