class MIP1:
    def P1PON(p1):
        ans=0
        while (p1>0):
            r=p1%10
            ans=ans+10+r
            p1=p1//10
        
        if(ans==ans):
            print("The number you entered is palindrom")
        else:
            print("The number you entered is not palindrom")

class MIP1C1(MIP1):
    def MIP2PONWUS(p2):
        var1= p2[::-1]

        if(var1==p2):
            print("The word you entered is palindrom")
        else:
            print("The word you entered is not palindrom")


class MIP2C2(MIP1C1):
    def MIP3PONWUS(p3):
        var2=str(p3)
        res=var2[::-1]

        if(res==var2):
            print("The number you entered is palindrom")
        else:
            print("The number you entered is not palindrom")

MIP1.P1PON(454)
MIP1C1.MIP2PONWUS("DAD")
MIP2C2.MIP3PONWUS(577)