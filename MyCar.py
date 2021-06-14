import Vehicle
from car_package import car_features

def my_car():
    print(f'My car is ' + Vehicle.vehicle_brand())
    print(Vehicle.vehicle_color())
    car_features.music_system()

my_car()