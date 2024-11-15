#By using function calling
def add():
    a=2
    b=3
    c=a+b
    print(c)
add()

#By using parameters
def add1(a,b):
    print("The value of a:",a)
    print("The value of b:",b)
    c=a/b
    d=a%b
    print(c)
    print(d)

add1(10,2)

#By using return
def sub():
    d=8
    e=4
    f=d-e
    return(f)

g=sub()
print(g)

#By using string data
def call(name1,age):
    print("Hello your name is {} and your age is {}".format(name1,age))

call("Villain",22)

#By taking input from user
def NA(Name_Variable,Age_Variable):
    print("your name is {} and your age is {}".format(Name_Variable,Age_Variable))

Name_Variable=input("Enter your name:")
Age_Variable=input("Enter your age:")

NA(Name_Variable,Age_Variable)