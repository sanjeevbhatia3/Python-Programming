# decorator function
def car_description(input_func):
    def car_details():
        print(f'My car color is blue')
        input_func()
        print(f'Car has BOSS music system')
    return car_details


# original function
@car_description
def my_car():
    print(f'Car model is Tesla Model-X')


my_car()

# car_info = car_description(my_car)
# car_info()
