def DM(Div):
    for i in range(1,Div+1):
        if Div%i == 0:
            print(i,end=" ")



Div=int(input("Enter the number:"))
DM(Div)
