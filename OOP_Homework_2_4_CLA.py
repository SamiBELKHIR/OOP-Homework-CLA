#Create a Vehicle class with max_speed and mileage instance attributes
#Create a child class Bus that will inherit all of the variables and methods 
#of the Vehicle class
class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed=max_speed
        self.mileage=mileage
example = Vehicle(260,36000)
print(example.mileage)

class Child_Bus(Vehicle):
    def __init__(self, max_speed, mileage):
        super().__init__(max_speed, mileage)

example_2 = Child_Bus(200,3600)
print(example_2.mileage)
