class Vehicle:
    def __init__(self):
        raise NotImplementedError("Do not create raw Vehicle objects")

    def __str__(self):
        return self.name

class Motorcycle(Vehicle):
    def __init__(self):
        self.name = "Suzuki Slasher"
        self.wheels = 2

class Car(Vehicle):
    def __init__(self):
        self.name = "Ranger Rover Sport"
        self.wheels = 4

test_car = Car()
print(test_car)

test_motorcycle = Motorcycle()
print(test_motorcycle)

test_error = Vehicle()
