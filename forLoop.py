# print every character in the string
name = 'john'
for each_char in name:
    print(each_char)

# print every word in the string
weather = 'Today is a nice sunny day'
weather_list = weather.split()
for each_word in weather_list:
    print(each_word)

# print every item in the list
my_list = [1,2,3,4,5,6,7,8,9,10]
for each_item in my_list:
    print(each_item)

# to print Hi for every item in the list
my_list = [1,2,3,4,5]
for _ in my_list:
    print("Hi")

# to print even and odd numbers in the list
num_list = [10, 23, 27, 30]
for num in num_list:
    if num % 2 == 1:
        print("Odd number: {}".format(num))
    else:
        print("Even number: {}".format(num))

# to get product of all numbers in the list
num_list = [1, 2, 3, 4]
product = 1
for num in num_list:
    product = product * num
print(product)

# list with tuple and tuple unpacking
info_list = [('John', 53), ('Mike', 47), ('Wade', 34)]
for person_name, person_age in info_list:
    print('{} is {} years old.'.format(person_name, person_age))
    print(f'{person_name} is {person_age} years old.')
    print(person_name)
    print(person_age)

# iterate over dictionary
my_dict = {'name': 'John', 'age': 53, 'hobbies':'running'}
for key,value in my_dict.items():
    print(key)
    print(value)