class PO1:
    def TCNIEORNOT(par1):
        if par1%2==0:
            print("The number is {} and it is  Even".format(par1))
        else:
            print("The number is {} and it is not Even".format(par1))

class PO2(PO1):
    def TCNIOORNOT(par2):
        if par2%2==1:
            print("The number is {} and it is odd".format(par2))
        else:
            print("The number is {} and it is not odd".format(par2))

class PO3(PO1):
    def TCNIPORNOT(par3):
        if par3<=1:
            print("The number {} is not prime".format(par3))
        
        for i in range(2,par3):
            if par3%i==0:
                print("The number {} is not prime".format(par3))
                break
            else:
                print("The number {} is prime".format(par3))
                break

PO3.TCNIPORNOT(1)
PO3.TCNIEORNOT(3)

PO2.TCNIOORNOT(6)
PO2.TCNIEORNOT(4)

