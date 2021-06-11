class Vehicle:
    # Class attributes (They are same for all instances of the class)
    color = 'blue'

    # Initialize when you Create instance of the class
    # self connect init with the object of the class
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def car_description(self, battery):
        print(f'I love my {self.make} car and its {Vehicle.color} color')
        print(f'Car has a battery of {battery}')


my_car1 = Vehicle(make="Tesla", model="Model-X")
my_car2 = Vehicle("Tesla", "Model 3")

# calling attribute doesn't require parenthesis
print(my_car1.model)
print(my_car2.model)
print(my_car1.color)
print(my_car2.color)

# calling method required parenthesis
# my_car1.car_description()

# calling method required parenthesis
my_car1.car_description('75kWh')


# Inheritance
class Car:
    def __init__(self):
        print("Car Created")

    def music_system(self):
        print(f'Car has BOSS music system.')

    def tire_brand(self):
        print(f'Car comes with Bridgestone tires.')


class Tesla(Car):
    def __init__(self):
        Car.__init__(self)
        print(f'Tesla Created')

    def color(self):
        print(f'Car color is blue.')

    # you can overwrite method as well
    # def music_system(self):
    #     print(f'Car has Harman-Kardon music system.')


my_car = Tesla()
my_car.color()
my_car.music_system()
