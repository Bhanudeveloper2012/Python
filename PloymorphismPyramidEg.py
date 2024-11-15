class SK:
    def TPSAP(par):
        for i in range(1,par+1):
            for j in range(1,i+1):
                print("*",end=" ")
            print()

class SK1(SK):
    def TPSAP1(par1):
        for i in range(0,par1):
            for j in range(0,i+1):
                print("*",end=" ")
            print()
        

class SK2(SK):
    def TPSAP2(par2):
        for i in range(par2,0,-1):
            for j in range(0,i):
                print("*",end=" ")
            print()
    

class SK3(SK1,SK2):
    def TPSAP3(par3):
        for i in range(1,par3+1):
            for j in range(par3-i):
                print(" ",end="")
            for k in range(1,2*i):
                print("*",end="")
            print()
    
SK1.TPSAP(4)
SK1.TPSAP1(3)

SK2.TPSAP2(4)
SK2.TPSAP(6)

SK3.TPSAP3(5)
SK3.TPSAP2(4)
SK3.TPSAP(4)