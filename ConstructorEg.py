class Car:
    def __init__(self,Name,Cost):
        self.Name=Name
        self.Cost=Cost
    
    def Print(self):
        print("The car name is {} and the car cost is {}:".format(Name,Cost))

Name=input("Enter the name of car:")
Cost=input("Enter the cost of car:")

obj=Car(Name,Cost)
obj.Print()

