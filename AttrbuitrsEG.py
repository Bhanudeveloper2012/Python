class Car:
    cost_of_car=10000000
    def car(self):
        self.name="Audi"
        self.maxspeed=150
        

c=Car()
c.car()
print("Car name is {} and car maxspeed is {} and cost of car is {}".format(c.name,c.maxspeed,Car.cost_of_car))


c1=Car()
c1.car()
c1.name="BWM"
c1.maxspeed=180
print("Car name is {} and car maxspeed is {} and cost of car is {}".format(c1.name,c1.maxspeed,c1.cost_of_car))