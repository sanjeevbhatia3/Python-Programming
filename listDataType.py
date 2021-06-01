# Ordered sequence of objects

# create empty list
numbers = []

# create list with elements
numbers_list = [1, 2, 3, 4, 5]

# print list
print(numbers_list)

# check the type of list variable
print(type(numbers_list))

# grab last item from the list
item = numbers_list[-1]
print(item)

# create list with different object types (integer, float, string)
my_list = [2, 3, "hi", "hello", 3.14, 3, 4, 3, 5, 6, 3, 3]

# get length of the list
print(len(my_list))

# list are mutable (you can change element in the list)
my_list[2] = 'morning'
print(my_list)

# append method (to add element in the list)
my_list.append("apple")
print(my_list)

# merge two list
second_list = [6, 7.13, "Oliver"]
my_list.extend(second_list)
print(my_list)

# insert element into the list at given in dex
my_list.insert(3, "Facebook")
print(my_list)

# delete element from the list
deleted_item = my_list.pop()
print(deleted_item)
print(my_list)

# delete element from given index
deleted_item = my_list.pop(3)
print(deleted_item)
print(my_list)

# delete entire list
my_list.clear()
print(my_list)

# get the index location of given element
print(my_list.index("hello"))

# get the count of given element in the list
print(my_list.count(3))

# reverse method
number_list = [1,2,3,4,5]
number_list.reverse()
print(number_list)

# sort method
item_list = [2,6,1,8,3,8,4,9]
item_list.sort()
print(item_list)

# join method
greet = ["Hi", 'good', 'morning!']
print(" ".join(greet))

# slicing [start:stop:step]
new_list = my_list[2:4]
print(new_list)

# print reverse list
print(my_list[::-1])

# nested list
chess_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(chess_list[0][1])



