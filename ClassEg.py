class Person:
    def SetValue(self,name,age):
        self.name=name
        self.age=age

    def GetValue(self):
        print("The name of a person is {} and the age is {}".format(name,age))
        # print("The name of a person is ",self.name," and the age is",self.age,".")

obj=Person()
name=(input("Enter the name of person:"))
age=(input("Enter the age of person:"))
obj.SetValue(name,age)
obj.GetValue()
