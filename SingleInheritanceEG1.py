class One:
    def add(a,b):
        c=a+b
        print("The value of a is {} and value of b is {} then the addition of two numbers is {}".format(a,b,c))

class Two(One):
    def sub(a,b):
        d=a-b
        print("The value of a is {} and value of b is {} then the addition of two numbers is {}".format(a,b,d))

# Instance method we need to use self
obj=Two()
obj.add(2,3)
obj.sub(6,3)

#Calling with class name
Two.add(2,3)
Two.sub(9,4)