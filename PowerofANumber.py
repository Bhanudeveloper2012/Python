# #By using for loop
Base=int(input("Enter the base value:"))
power=int(input("Enter the power value"))
res=1

for i in range(power):
    res=res*Base
print(res)

#By using while loop
Base1=int(input("Enter the base value:"))
Power1=int(input("Enter the power value:"))
ans=1

while(Power1!=0):
    ans=ans*Base1
    Power1=Power1-1
print(ans)

#By using recursion

def PN(Base2,Power2):
    if Power2 == 1:
        return Base2
    else:
        return Base2*PN(Base2,Power2-1)

ans=PN(2,3)
print(ans)