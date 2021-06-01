# set
# create empty set
my_set = set()
print(my_set)

# add item in the set
my_set.add(1)
print(my_set)

# add more item in the set
my_set.add(2)
my_set.add(3)
my_set.add(4)
my_set.add(5)

# try to add duplicate item in the set
my_set.add(4)
print(my_set)

# extract unique items from list using set
my_list = [1,2,3,4,5,2,3,4,6,8,5,9]
my_new_set = set(my_list)
print(my_new_set)

# set does not support indexing. It will throw error
print(my_set[0])

# in method to check item in the set
print(3 in my_set)  # True
print(10 in my_set)  # False

######################################################################
# Tuple
# create tuple
colors = ('red', 'green', 'yellow', 'orange', 'yellow', 'yellow', 'yellow')
print(colors)

# indexing allowed in tuple
print(colors[2])

# count and index methods
print(colors.index('green'))
print(colors.count('yellow'))

# use tuple as key in dictionary
inventory = {('macbook', '13 inch'): 10,
             ('macbook', '15 inch'): 4}



