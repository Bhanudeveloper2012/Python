Number=input("Enter the number:")
ans_Even=0
ans_Odd=0

for i in Number:
    if(int(i)%2==0):
        ans_Even=ans_Even +int(i)
    else:
        ans_Odd=ans_Odd + int(i)
print("The sum of even numbers in {} is: {}".format(Number,ans_Even))
print("The sum of odd numbers in {} is: {}".format(Number,ans_Odd))

#Pre define values
Number1=[1,2,3,4,5,6]
Ans_Even=0
Ans_Odd=0

for i in Number1:
    if i%2==0:
        Ans_Even=Ans_Even+i
    else:
        Ans_Odd=Ans_Odd+i
    
print("The sum of even numbers in {} is: {}".format(Number1,Ans_Even))
print("The sum of odd numbers in {} is: {}".format(Number1,Ans_Odd))
