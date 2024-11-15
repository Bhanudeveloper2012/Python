factorial_Number=int(input("Enter the number for which you want to find factorial:"))
res=1
if(factorial_Number==0):
        print("The factorial of given num is {}".format(1))
elif(factorial_Number>0):
        for i in range(1,factorial_Number+1):
                res=res*i
        print("The factorial of {} is: {}".format(factorial_Number,res))
          
else:
        print("No output") 
