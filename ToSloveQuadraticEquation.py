#Sloving qudartic equation

import cmath
import math
def SQE(a,b,c):
    D=b**2-4*a*c

# Distinct roots
    if(D>0):
        s1=(-b + math.sqrt(D)) / (2*a)
        s2=(-b - math.sqrt(D)) / (2*a)
        return s1,s2
    
# Real root
    elif D==0:
        x=-b/(2*a)
        return x

# Complex root
    else:
        s1=(-b + cmath.sqrt(D)) / (2*a)
        s2=(-b + cmath.sqrt(D)) / (2*a)
        return s1,s2

a=(float(input("Enter coffiecient of a: ")))
b=(float(input("Enter coffiecient of b: ")))
c=(float(input("Enter coffiecient of c: ")))

root=SQE(a,b,c)

if isinstance (root,tuple):
    print("The quadratic equation has two distinct roots:")
    print("s1",root[0])
    print("s2",root[0])

else:
    print("The quadratic equation has one real root:")
    print("x",root[0])