class HIP:
    def FOAN(num):
        res=1
        if num==0:
            print("The factorial of a number is one")
        elif num>0:
            for i in range(1,num+1):
                res=res*i
            print("The factorial of a number is:",res)
        else:
            print("Enter a valid Number")

class HID1(HIP):
    def FOAN1(Num):
        res1=1
        if (Num==0 or Num==1):
            print("The number your is {} and factorial of the number is {}".format(Num,1))
        elif(Num>0):
            for i in range(1,Num+1):
                res1=res1*i
            print("The given number is {} and the factorial is :{}".format(Num,res1))
        else:
            print("Enter a vaild number")

class HID2(HIP):
    def FOAN2(NUM):
        res2=1
        for i in range(1,NUM+1):
            res2=res2*i
        print("The given number is {} and the factorial is :{}".format(NUM,res2))

HID1.FOAN(5)
HID1.FOAN1(7)
HID2.FOAN(4)
HID2.FOAN2(0)