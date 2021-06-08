# methods for python objects
my_list = [1, 2, 3, 4, 5, 10]
print(my_list)
item = my_list.pop()
print(item)
my_list.insert(1, 100)
print(my_list)


# Function
def say_hello(name):
    print("Hello " + name)


# execute function
say_hello("Mike")


def say_hello(name="John"):
    print("Hello " + name)


# execute function
say_hello("Jake")
say_hello()


# return keyword
def add_num(a=2, b=4):
    return a + b


final_sum = add_num(4, 5)
print(final_sum)


def full_name(first_name, last_name):
    return first_name + " " + last_name


name = full_name("john", "oliver")
print(name)


# function with logic
# given number is odd/even
def even_odd(num):
    if num % 2 == 0:
        print(f"Given number is even")
    else:
        print(f"Given number is odd")


even_odd(8)


def check_vowel(given_string):
    for letter in given_string:
        if letter in 'aeiou':
            return True
        else:
            pass
    return False


print(check_vowel("red"))
print(check_vowel('mdn'))


# return multiple items
inventory = [('macbook', 3), ('chromeBook', 5), ('iphone', 20), ('ipad', 10)]
def inventory_check(inventory):
    max_inventory_item = ""
    current_inventory = 0
    for item, num in inventory:
        if num > current_inventory:
            current_inventory = num
            max_inventory_item = item
    return max_inventory_item, current_inventory


result = inventory_check(inventory)
print(result)


# value from one function to pass into another function
def full_name(first_name, last_name):
    return first_name + " " + last_name


name = full_name("john", "oliver")


def person_info(given_name=name):
    age = 53
    print(f'{given_name} is {age} years old.')


person_info()

# *args **kwargs
def num_sum(*args):
    print(sum(args))
num_sum(3,4,4,5,4)

# **kwargs
def fav_color(**kwargs):
    if 'color' in kwargs:
        print('My favorite color is {}.'.format(kwargs['color']))
    else:
        print('I did not find any color')


fav_color(color='red', juice='orange')


total = 0
def number():
    #global total
    total = 2
    total += 1


num = number()
print(total)

