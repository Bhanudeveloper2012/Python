#To find the square of a number
Sqon=int(input("Enter the number your want to find the square of number:"))
res=0

res=Sqon*Sqon

print("The number your enter is {} and the square of the number is {}".format(Sqon,res))

#To find the cube of a number
Sqon1=int(input("Enter the number your want to find the cube of number:"))
res1=0

res1=Sqon1*Sqon1*Sqon1

print("The number your enter is {} and the cube of the number is {}".format(Sqon1,res1))

# To find square of any number
Base=int(input("Enter the base number:"))
Power=int(input("Enter the power number:"))

res2=1

for i in range(Power):
    res2=res2*Base
print("The square of number is:",res2)

#To find square of number by using while loop
Base1=int(input("Enter the base number:"))
Power1=int(input("Enter the power number:"))
res3=1

while(Power1!=0):
    res3=res3*Base1
    Power1=Power1-1
print(res3)