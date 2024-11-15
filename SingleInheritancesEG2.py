class SIP:
    TI='SI'
    def Add(a,b):
        c=a+b
        print("The value of a is {},the value of b is {} and the sum of these two numbers is {}".format(a,b,c))

class SIC(SIP):
    def DIV(d,e):
        f=d/e
        print("The value of d is {},the value of e is {} and the qutionet of these two numbers is {}".format(d,e,f))

SIC.Add(3,5)
SIC.DIV(10,5)
print(SIC.TI)