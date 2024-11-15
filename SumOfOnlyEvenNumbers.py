Number=int(input("Enter the number:"))
res=0

for i in range(1,Number+1):
    if(i%2==0):
        res=res+i
print(res)