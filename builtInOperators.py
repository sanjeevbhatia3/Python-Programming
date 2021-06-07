# range function
my_list = [1,2,3,4,5]
# (start-optional, stop, step-optional)
for num in range(5):
    print(num)
for num in range(2, 5):
    print(num)
for num in range(2,10,3):
    print(num)

num_list = list(range(1,11))
print(num_list)

# enumerate (This is really useful when you
# want to get index and value at that index)

name = "mickey"
for item in enumerate(name):
    print(item)

for index, value in enumerate(name):
    print(f'{value} is at index {index}')

# Zip (zip together lists)
num = [1,2,3]
name = ["John", "Mike", "Jake"]
for item in zip(num,name):
    print(item)

# Zip is only go upto length of smallest list
num = [1,2,3,4,5,6,7,8]
names = ["John", "Mike", "Jake"]
for item in zip(num,names):
    print(item)

# in operator
num = ['a','b','c']
print('b' in num) #-> True
print('x' in num) #-> False

name = {'first_name': 'John', 'last_name': 'Oliver'}
print('first_name' in name)
print('middle_name' in name)

print('John' in name.values())
print('Mike' in name.values())

#min
num = [3,4,7,1,7,9,5]
print(min(num))
#max
print(max(num))

# random library
print("random library")
from random import randint
i = 1
while i <= 5:
    random_num = randint(1, 10)
    print(random_num)
    i += 1

from random import choice
for num in range(5):
    names = ["John", "Mike", "Jake"]
    print(choice(names))

# input (to get user input)
name = input("Enter your name:")
print("Hello " + name.strip())

# default is string, typecast for int
age = int(input("Enter your age:"))
print(f"you are {age} years old.")


#sorted
my_list = [1,3,7,2,9,4,45,5,6]
sorted_list = sorted(my_list)
print(sorted_list)
