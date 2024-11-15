from abc import ABC,abstractmethod

class Number1(ABC):
    @abstractmethod
    def Even(var1):
        pass

class Number2(Number1):
    def Odd(self,var2):
        if var2%2!=0:
            print("The number your entered is {} and it is Odd.".format(var2))
    def Even(self,var1):
        if var1%2==0:
            print("The number your entered is {} and it is Even.".format(var1))

obj=Number2()
obj.Odd(3)
obj.Even(4)
