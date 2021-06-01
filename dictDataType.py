# dictionary key-value pair mapping

# create empty dictionary
my_dict = {}
print(my_dict)

# create dictionary with key-value pairs
name_dict = {'first_name': 'John', 'last_name': 'Oliver'}

# grab value of given key
print(name_dict['first_name'])

# nested dictionary
grocery = {'milk': 1, 'fruits': {'apple': 4, 'orange': 5, 'banana': 6}, 'items': [10, 20, 30]}
print(grocery['fruits']['orange'])
print(grocery['items'][0])

# add item to the dictionary
grocery['drink'] = 'wine'
print(grocery)

# get all keys from the dictionary
print(grocery.keys())

# get all values from the dictionary
print(grocery.values())

# get all key-value pair from the dictionary
print(grocery.items())

# if key is not define in dictionary
print(grocery['juice'])  # this will give keyError
print(grocery.get('juice'))

# checking key in dictionary with if-else
if 'milk' in grocery:
    print(grocery['milk'])
else:
    print("Key is not defined")

# remove element from the dictionary
grocery.pop('items')
print(grocery)

# delete entire dictionary
grocery.clear()
print(grocery)
